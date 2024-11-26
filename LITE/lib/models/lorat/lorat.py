import os
from typing import Tuple
import torch
import torch.nn as nn
from timm.layers import trunc_normal_
from lib.models.modules.dinov2 import DinoVisionTransformer, interpolate_pos_encoding
from lib.models.modules.patch_embed import PatchEmbedNoSizeCheck
from lib.models.modules.head.mlp import MlpAnchorFreeHead
from timm.layers import to_2tuple
from lib.models.lorat.builder import build_dino_v2_backbone

class LoRATBaseline_DINOv2(nn.Module):
    def __init__(self, vit: DinoVisionTransformer,
                 template_feat_size: Tuple[int, int],
                 search_region_feat_size: Tuple[int, int]):
        super().__init__()
        assert template_feat_size[0] <= search_region_feat_size[0] and template_feat_size[1] <= search_region_feat_size[1]
        self.z_size = template_feat_size
        self.x_size = search_region_feat_size

        assert isinstance(vit, DinoVisionTransformer)
        self.patch_embed = PatchEmbedNoSizeCheck.build(vit.patch_embed)
        self.blocks = vit.blocks
        self.norm = vit.norm
        self.embed_dim = vit.embed_dim

        self.pos_embed = nn.Parameter(torch.empty(1, self.x_size[0] * self.x_size[1], self.embed_dim))
        self.pos_embed.data.copy_(interpolate_pos_encoding(vit.pos_embed.data[:, 1:, :],
                                                           self.x_size,
                                                           vit.patch_embed.patches_resolution,
                                                           num_prefix_tokens=0, interpolate_offset=0))

        self.token_type_embed = nn.Parameter(torch.empty(3, self.embed_dim))
        trunc_normal_(self.token_type_embed, std=.02)

        self.head = MlpAnchorFreeHead(self.embed_dim, self.x_size)

    def forward(self, z: torch.Tensor, x: torch.Tensor, z_feat_mask: torch.Tensor):
        z_feat = self._z_feat(z, z_feat_mask)
        x_feat = self._x_feat(x)
        x_feat = self._fusion(z_feat, x_feat)
        return self.head(x_feat)
    # score_map: [B, H, W]
    # boxes:     [B, H, W, 4]

    def _z_feat(self, z: torch.Tensor, z_feat_mask: torch.Tensor):
        z = self.patch_embed(z)
        z_W, z_H = self.z_size
        z = z + self.pos_embed.view(1, self.x_size[1], self.x_size[0], self.embed_dim)[:, : z_H, : z_W, :].reshape(1, z_H * z_W, self.embed_dim)
        z = z + self.token_type_embed[z_feat_mask.flatten(1)]
        return z

    def _x_feat(self, x: torch.Tensor):
        x = self.patch_embed(x)
        x = x + self.pos_embed
        x = x + self.token_type_embed[2].view(1, 1, self.embed_dim)
        return x

    def _fusion(self, z_feat: torch.Tensor, x_feat: torch.Tensor):
        fusion_feat = torch.cat((z_feat, x_feat), dim=1)
        for i in range(len(self.blocks)):
            fusion_feat = self.blocks[i](fusion_feat)
        fusion_feat = self.norm(fusion_feat)
        return fusion_feat[:, z_feat.shape[1]:, :]

    # def load_state_dict(self, state_dict: Mapping[str, Any], **kwargs):
    #     state_dict = lora_merge_state_dict(self, state_dict)
    #     return super().load_state_dict(state_dict, **kwargs)


def build_lorat(cfg, training=True):
    load_pretrained = cfg.MODEL.LOAD_PRETRAINED  # False
    backbone_build_params = {"name": cfg.MODEL.BACKBONE.TYPE, "acc": "default"}
    backbone = build_dino_v2_backbone(load_pretrained=load_pretrained, **backbone_build_params)

    stride = cfg.MODEL.BACKBONE.STRIDE
    feat_sz_z = int(cfg.DATA.TEMPLATE.SIZE / stride)
    feat_sz_x = int(cfg.DATA.SEARCH.SIZE / stride)

    model = LoRATBaseline_DINOv2(backbone, to_2tuple(feat_sz_z), to_2tuple(feat_sz_x))

    if training:
        ckpt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../", "pretrained", cfg.MODEL.PRETRAIN_FILE))
        missing_keys, unexpected_keys = model.load_state_dict(torch.load(ckpt_path), strict=True)
        print(f"missing_keys when load LoRAT whole model: {missing_keys}")
        print(f"unexpected_keys when load LoRAT whole model: {unexpected_keys}")

    return model


if __name__ == '__main__':
    import importlib
    config_module = importlib.import_module("lib.config.%s.config" % 'lorat')
    cfg = config_module.cfg
    config_module.update_config_from_file('')
    lorat = build_lorat(cfg, training=True)
    print(lorat)