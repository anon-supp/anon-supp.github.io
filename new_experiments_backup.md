


# NEW EXPERIMENTS -- TABLES


## Runtime Reports — SphericalDreamer

@CURSOR: at the end of the site

| Stage | N=2 | | N=3 | | N=4 | |
|:------|:--------:|:-----:|:--------:|:-----:|:---------:|:-----:|
|       | Time     |   %   | Time     |   %   | Time      |   %   |
| **Total pipeline** | **29m 02s** | **100** | **47m 31s** | **100** | **1h 06m 21s** | **100** |
| Panorama Generation | 3m 55s | 13.5 | 5m 27s | 11.5 | 6m 37s | 10.0 |
| &ensp; Image Generation | 2m 49s | 9.7 | 3m 53s | 8.2 | 4m 33s | 6.9 |
| &ensp; Depth Estimation | 1m 04s | 3.7 | 1m 30s | 3.2 | 1m 59s | 3.0 |
| LDI Inpainting | 4m 17s | 14.8 | 5m 46s | 12.1 | 7m 49s | 11.8 |
| &ensp; SAM Foreground Masking | 40s | 2.3 | 57s | 2.0 | 1m 21s | 2.0 |
| &ensp; LAMA Inpainting | 36s | 2.1 | 26s | 0.9 | 38s | 1.0 |
| &ensp; FLUX Inpainting | 2m 40s | 9.2 | 3m 56s | 8.3 | 5m 14s | 7.9 |
| &ensp; Depth Inpainting | 0s | 0.0 | 0s | 0.0 | 0s | 0.0 |
| Generative Fusion | 8m 21s | 28.8 | 14m 20s | 30.2 | 20m 14s | 30.5 |
| &ensp; Point Cloud Rendering | 58s | 3.3 | 1m 56s | 4.1 | 3m 01s | 4.5 |
| &ensp; FLUX Inpainting | 1m 27s | 5.0 | 2m 58s | 6.2 | 4m 17s | 6.5 |
| &ensp; Depth Estimation | 36s | 2.1 | 1m 13s | 2.6 | 1m 42s | 2.6 |
| LDI Inpainting (intermediate viewpoint) | 2m 50s | 9.8 | 4m 42s | 9.9 | 6m 09s | 9.3 |
| &ensp; SAM Foreground Masking | 25s | 1.4 | 39s | 1.4 | 55s | 1.4 |
| &ensp; LAMA Inpainting | 34s | 2.0 | 34s | 1.2 | 36s | 0.9 |
| &ensp; FLUX Inpainting | 1m 39s | 5.7 | 3m 05s | 6.5 | 4m 10s | 6.3 |
| &ensp; Depth Inpainting | 0s | 0.0 | 0s | 0.0 | 0s | 0.0 |
| Harmonic Blending | 7m 23s | 25.4 | 14m 41s | 30.9 | 21m 43s | 32.7 |
| Video Rendering | 2m 16s | 7.8 | 2m 36s | 5.5 | 3m 50s | 5.8 |


## Evaluation of Geometry: comparison of depth models in the spherical domain.

@Cursor: In section D

| Model | AbsRel (↓) | RMSE (↓) | SI-RMSE (↓) | δ<1.25 (↑) | δ<1.25² (↑) | δ<1.25³ (↑) |
|:------|:----------:|:--------:|:----------:|:----------:|:-----------:|:-----------:|
| BiFuseV2_st3d | 1.0077 | 1.8958 | 1.0858 | 0.1736 | 0.3368 | 0.4906 |
| EGFormer_st3d | 0.8048 | 1.6097 | 0.8338 | 0.2107 | 0.3952 | 0.5744 |
| HoHoNet_st3d  | 1.1524 | 2.0839 | 1.1094 | 0.1711 | 0.3301 | 0.4723 |
| UniFuse_st3d  | 1.0445 | 1.9659 | 1.1372 | 0.1738 | 0.3250 | 0.4706 |
| **SphericalDreamer (via 360monodepth)** | **0.1605** | **0.6008** | **0.2039** | **0.7363** | **0.9317** | **0.9819** |


## Consistency of Generated 3D World

@ Cursor: At the end, create a new section named "addtionnal metrics" This one should be in a subsection named "quality"

| Method | clip-score (↑) | c-clip (↑) |
|:-------|:---:|:---:|
| LucidDreamer | <u>0.2988</u> | 0.6599 |
| LayerPano3D | 0.2639 | 0.5787 |
| WonderJourney | 0.2570 | 0.6149 |
| SceneScape | 0.2802 | <u>0.7866</u> |
| **SphericalDreamer (ours)** | **0.3325** | **0.8433** |



## Rendering Quality of a Single 3D World
VERSION COURTE:

@ Cursor: At the end, in the newly created section named "addtionnal metrics" This one should be in a subsection named "consitency"

| Method | BRISQUE (↓) | CLIP-IQA (↑) | Q-Align (↑) |
|:-------|:---:|:---:|:---:|
| LucidDreamer | 64.351 | <u>0.6237</u> | <u>1.8908</u> |
| LayerPano3D | 76.742 | 0.5077 | 1.7943 |
| WonderJourney | 61.684 | 0.5006 | 1.6017 |
| SceneScape | <u>55.919</u> | 0.3805 | 1.7231 |
| **SphericalDreamer (ours)** | **41.737** | **0.7014** | **2.3088** |



## More results on harmonic blending and why it is better than alternative: a study at the transition regions (i.e. blending boundaries)


@Cursor: this one should be in section E

| Method      | Depth Transition Score (↓) | Transition Region MAE (↓) |
|:------------|---------------------------:|--------------------------:|
| Interpolation |                    <u>0.00389</u> |                   <u>0.03067</u> |
| Depth inpainting (Infusion)    |                    0.09529 |                   0.09177 |
| Harmonic Blending (Ours)      |                    **0.00328** |                   **0.00079** |




## Ablation study

### Ablation: HBlend / LDI

@cursor: this one should in be in section B

| Setting | BRISQUE (↓) | Coverage (↑) | clip-score (↑) | c-clip (↑) | CLIP-IQA (↑) | Q-Align (↑) |
|:-------|:---:|:---:|:---:|:---:|:---:|:---:|
| Ours | **43.4709** | **0.9993** | **0.3418** | **0.8608** | **0.7582** | **2.366** |
| no LDI | 45.8937 | 0.9652 | 0.3371 | 0.8459 | 0.7358 | 2.1935 |
| no HB (naive instead) | 47.1084 | 0.9242 | 0.3253 | 0.8001 | 0.6503 | 1.9953 |
| no HB (inpainting instead) | <u>44.3742</u> | 0.9314 | 0.3272 | 0.8099 | 0.5976 | 2.078 |
| no HB (interpolation instead) | 45.4247 | <u>0.9835</u> | <u>0.3377</u> | <u>0.8496</u> | <u>0.7505</u> | <u>2.2595</u> |




### Ablation: World size N

@ cursor: this one should at the begining, with the video

| Setting | BRISQUE (↓) | Coverage (↑) | clip-score (↑) | c-clip (↑) | CLIP-IQA (↑) | Q-Align (↑) |
|:-------|:---:|:---:|:---:|:---:|:---:|:---:|
| N=3 | 43.4683 | 0.9993 | 0.3418 | 0.8608 | 0.7582 | 2.3662 |
| N=4 | 42.2766 | 0.9993 | 0.3418 | 0.8471 | 0.7387 | 2.3057 |
| N=5 | 41.548 | 0.9994 | 0.3403 | 0.8447 | 0.7747 | 2.3088 |
| N=6 | 42.1268 | 0.9995 | 0.34 | 0.8499 | 0.7777 | 2.312 |
| N=7 | 41.5514 | 0.9994 | 0.3424 | 0.8453 | 0.7913 | 2.349 |