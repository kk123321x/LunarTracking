## Install the environment
```
conda create -n lorat python=3.9
conda activate lorat
bash install.sh
```


## Set project paths
Run the following command to set paths for this project
```
python tracking/create_default_local_file.py --workspace_dir . --data_dir ./data --save_dir ./output
```
After running this command, you can also modify paths by editing these two files
```
lib/train/admin/local.py  # paths about training
lib/test/evaluation/local.py  # paths about testing
```


## Training
This repository support the downstream fine-tuning of LoRAT, not the training from the scratch(i.e., we do not implement insert and merge methods of `LoRA`).  

Run:
```
bash xtrain.sh
```

## Evaluation
Download the model weights from [Quark Drive](https://pan.quark.cn/s/e71acbd77f77) 

Put the downloaded weights on `$PROJECT_ROOT$/pretrained`

Change the corresponding values of `lib/test/evaluation/local.py` to the actual benchmark saving paths

Run:
```
bash ytest.sh
```


## Test FLOPs, and Speed
```
# Profiling base_224
python tracking/profile_model.py --script lorat --config base_224
# Profiling base_378
python tracking/profile_model.py --script lorat --config base_378
# Profiling large_224
python tracking/profile_model.py --script lorat --config large_224
# Profiling large_378
python tracking/profile_model.py --script lorat --config large_378
# Profiling giant_224
python tracking/profile_model.py --script lorat --config giant_224
# Profiling giant_378
python tracking/profile_model.py --script lorat --config giant_378
```
