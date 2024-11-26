# Lunar Tracking
The official implementation for the  paper \[[_NT-VOT211: A Large-Scale Benchmark for Night-time Visual Object Tracking_](www.google.com)\]

## Abstract
>Many existing visual object tracking benchmarks, such as TNL2k, TrackingNet, LaSOT, and GOT-10K, primarily
focus on daytime scenarios. However, the challenge of tracking small targets in low-light conditions has not been sufficiently addressed. This limitation is due to the absence of a largescale, meticulously annotated nighttime benchmark that could rigorously evaluate tracking algorithms designed for tiny targets. To bridge this gap, we introduce Lunar Tracking, a groundbreaking benchmark tailored to assess the performance of visual object tracking algorithms on tiny objects under lowlight conditions. The Lunar Tracking benchmark comprises 700 diverse videos with over 600,000 annotated frames featuring tiny targets, making it the largest of its kind for nighttime tracking and tiny object tracking. We also introduce a novel tracking algorithm designed to enhance low-light conditions by innovatively treating the light enhancement task as a ’dehazing’ process and modeling it as a two-step diffusion process. Our proposed module has set a new state-of-the-art (SOTA) across the Lunar Tracking benchmark and four additional benchmarks by reversing the diffusion process in a step-by-step manner.

## Download the dataset
To facilitate downloading, we have divided the dataset into 65 parts, each 1GB in size：

[LunarTracking 1/7](https://zenodo.org/records/14208796?preview=1&token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTczMjM2Mzc0MCwiZXhwIjo0ODYzMjgzMTk5fQ.eyJpZCI6ImMyNTU5YWI4LTFiYWEtNGY1MC05OGRlLTQ5MzgyN2M4MWVlMiIsImRhdGEiOnt9LCJyYW5kb20iOiIwMmEzMTIwZWJmNjE2NjlkZThlZjVlM2QzYjQ0OTAzMyJ9.UrJP8BYe_aj8gK98bvOhwCWPUIUbc2eYRYoe5ADayC-4s4bH3PH-KjRx6b8_SK3fvKvzWQvBQwDyol6C_f0JWw)

[LunarTracking 2/7](https://zenodo.org/records/14209468?preview=1&token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTczMjM2NTg0MywiZXhwIjo0ODYzMjgzMTk5fQ.eyJpZCI6IjlhMjJjNmY2LWQxYmMtNDk0MS04MmRjLTgxMzQ3ODI0NjExNyIsImRhdGEiOnt9LCJyYW5kb20iOiJjMjc1MGU1Mjg5MGJhMzJmYzhmYTZlMTMxNmM4ZDQ2MyJ9.ngQabbPnuYyeEFEV1xO2RrHFYMGMROLGs-6kP4dFZLCccaNRNGgR3_xIz3gnMER-l4i0QitBHBSrbxjwc6xypw)

[LunarTracking 3/7](https://zenodo.org/records/14209693?preview=1&token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTczMjM3MDkwMywiZXhwIjo0ODYzMjgzMTk5fQ.eyJpZCI6IjQ1ZTVlYmZjLTJhYmYtNGZkMy05NGM3LWE1ODg5NjZjMTc2ZSIsImRhdGEiOnt9LCJyYW5kb20iOiIzZjVkZGY1YWM5MGY5NzQ4ZjgxNmE5YzI4YzM0YWJkYSJ9.0maCFqOCSu_ZkLpWgCMEzkEcRL-P-XJhipXFfp1VFjxj78SxHnAytUYGedsfpyZjps_DZMgixpAPOzOjt13GeQ)

[LunarTracking 4/7](https://zenodo.org/records/14209780?preview=1&token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTczMjM3MTU0MiwiZXhwIjo0ODYzMjgzMTk5fQ.eyJpZCI6IjZhZTY1NDY0LTAwNTYtNDU3My05MDhhLTk5ODAxYjMyMmUwOSIsImRhdGEiOnt9LCJyYW5kb20iOiI1ZjJjNzdhNjBmYWIzZmM0NzQ1Njc3NWIzZDE0ZDE2ZiJ9.sYUjNWX_1BZYis8G6L-dm72Cph0ng25CuPry_SX-XibXb0cUF4meFVdpWX4_VGf-Pejp5YH4pxpGI9D66uetdg)


[LunarTracking 5/7](https://zenodo.org/records/14211015?preview=1&token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTczMjQzMDQwMCwiZXhwIjo0ODYzMjgzMTk5fQ.eyJpZCI6ImZkMzYxZWUwLTIwMTctNGEwMC1hYzhmLTgxZWRkY2Y2MDNmOSIsImRhdGEiOnt9LCJyYW5kb20iOiIxMGZiZWY5N2Y2YWE3YTZmMGI1YTY3NTBlN2I2OTU3NSJ9.15C39yhpH4qcSZCbW9i6egRqCrkZ3gUS-ecAboiZasTNpl8cunQcj_2DD-dh0yH4H-cigpb0scEB4I6KzxilsA)

[LunarTracking 6/7](https://zenodo.org/records/14211146?preview=1&token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTczMjQzMTIzNSwiZXhwIjo0ODYzMjgzMTk5fQ.eyJpZCI6IjAwNTY5NWU3LWZjMmQtNGQ0Zi1hZGJlLTlhYmUwMDI3NGRiNyIsImRhdGEiOnt9LCJyYW5kb20iOiI5NjFhODk1M2Q1ZmZjNDI3YjkxM2MzN2FmMzc4YTAyNyJ9.-2QM21cRuMTvdTAjzh1hipJ4uKKEcyzB6fg-Ie4gVLDXjiJD7UaUQXnaDnlDnXctQPJQKplwUmNmkYK9bXIdxw)


[LunarTracking 7/7](https://zenodo.org/records/14211448?preview=1&token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTczMjQzOTk3NiwiZXhwIjo0ODYzMjgzMTk5fQ.eyJpZCI6IjExYTQyYmFkLTE1NDUtNGUyZi05ZTkzLTgxMmM3NmZmMjYyYSIsImRhdGEiOnt9LCJyYW5kb20iOiJjYTZiZWQwYzhmMzgzODdjZDdkYzFiMjI5YjU1NGI3YSJ9.avFBuGIQdrHHNakaGMEAXxVhYocm1ic6PyNYmMUn_fdegn5lZlnsBo7U1mRp57jWk0I7Zfqyns0w65LWk6psQw)

## Run the code
Please check this tutorial to run our code.


# Citation
If you find our work valuable, please cite our paper.
```bibtex





```

# Maintenance
Please open a GitHub issue for any help. If you have any questions regarding the technical details, feel free to contact us.
# License
[MIT License](https://mit-license.org/)
