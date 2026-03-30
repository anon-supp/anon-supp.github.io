
We thank the reviewer for their review and remarks.  We especially appreciate that the reviewer found our work to be **particularly impressive**, with **strong performance**, and an idea that is **both novel and promising**.

We address the reviewer's concerns below.

Please note that we provide additional animated results at the following anonymous link: https://anon-supp.github.io/ . All additional results will be integrated in the final version of our paper.

## (w.1) On the reliance of monocular depth estimators

Our method, like all image-to-3D lifting approaches, fundamentally relies on monocular depth estimation to construct geometry. As a result, inaccuracies in depth prediction indeed lead to degraded geometric quality in the generated world.

However, we would like to emphasize that this limitation is **not specific to SphericalDreamer**, but is shared across all compared baselines, which are also reliant on depth estimation as a core component of their pipelines. In this sense, the sensitivity to depth errors is a **broader limitation of the current paradigm** rather than of our method in particular.

In the final paper, we will include additional discussion on this aspect.

## (w.2) More diverse scenes

We thank the reviewer for raising the point regarding generalization across diverse scene categories. As discussed in the limitations section, SphericalDreamer is inherently better suited to outdoor, natural environments, due to its reliance on spherical imagery, which makes it less effective at modeling structured planar geometry commonly found in urban and indoor scenes.

To address this concern, we will clarify the scope of our method in the camera-ready version. In particular, we will explicitly state in the abstract, introduction, and experimental sections that SphericalDreamer is designed for 3D world generation in outdoor and natural settings. This clarification will prevent potential misinterpretation of the method as being universally applicable to all scene types.

We believe this revision better aligns the claims of the paper with the demonstrated capabilities of the method, while clearly acknowledging its current limitations.

## (w.3) Alignment of adjacent spheres

We thank the reviewer for raising this important point regarding potential alignment errors.

We would like to clarify that, in our pipeline, **the only potential source of geometric misalignment arises at the panorama fusion stage**, where newly generated content is integrated between adjacent spheres. The world assembly itself is a direct aggregation of already aligned building and filling blocks, and does not introduce additional distortions.

To specifically address potential misalignment artifacts at fusion boundaries, we have proposed using **harmonic blending** to ensure smooth geometric transitions between existing and newly generated depth. 

In this rebuttal, we further validate this choice through additional evaluations of harmonic blending. First, we conduct an ablation study in which harmonic blending is replaced by three simpler alternatives, highlighting its importance **within our pipeline**. Second, we provide a more in-depth analysis by comparing harmonic blending with these alternatives on the specific **task of depth completion**. This offers a clearer and more direct understanding of why harmonic blending is more effective.

### Ablating Harmonic Blending in our pipeline

We validate the use of Harmonic Blending in our pipeline by performing an ablation study where we replace it by three simpler alternatives: naïve blending, depth inpaiting via bilinear interpolation, and depth inpainting via InFusion [1], a diffusion based depth-inpainting model.

**Qualitatively,** ([anon link](https://anon-supp.github.io/), Section B), we observe that harmonic blending outperforms its alternatives: it successfully completes all missing regions in the world, whereas the alternatives often leave incomplete or inconsistent areas.

**Quantitatively,** we compute various scores on generated scenes to validate our results:
- C-CLIP to measure the semantic consistency across the world,
- CLIP-Score to measure text alignment,
- BRISQUE, CLIP-IQA, and Q-Align to measure rendering quality.

**In brief,** using Harmonic Blending (HB) produce 3D worlds that outperform those produced with its alternatives on all of the metrics.

| Setting | BRISQUE (↓) | Coverage (↑) | CLIP-score (↑) | C-CLIP (↑) | CLIP-IQA (↑) | Q-Align (↑) |
|:-------|:---:|:---:|:---:|:---:|:---:|:---:|
| no HB (naive instead) | 47.1084 | 0.9242 | 0.3253 | 0.8001 | 0.6503 | 1.9953 |
| no HB (inpainting instead [1]) | *44.3742* | 0.9314 | 0.3272 | 0.8099 | 0.5976 | 2.078 |
| no HB (interpolation instead) | 45.4247 | *0.9835* | *0.3377* | *0.8496* | *0.7505* | *2.2595* |
| Ours | **43.4709** | **0.9993** | **0.3418** | **0.8608** | **0.7582** | **2.366** |

### In-depth analysis

We conduct an in-depth analysis to further compare harmonic blending with the three alternatives listed above for the task of depth completion. In these experiments, we first mask out a portion of the reference depth map and then predict the missing regions using each method, enabling a direct comparison of their performance. 

**Qualitatively** ([anon link](https://anon-supp.github.io/), Section E), we can see that harmonic blending provides the smoothest transition between known depth regions and estimated regions, without causing any artifacts.

**Quantitatively,** we compute two metrics to confirm our findings:
- The **Depth Transition Score** is defined as the average absolute difference in depth values across pixels on either side of the boundary between known and reconstructed regions, where lower values indicate smoother transitions. Our approach presents the best transition score, indicating that it enables the smoothest transition between known and unknown depth.
- The **Depth Estimation Error** measures the difference between predicted and ground-truth depth values within a narrow band along the blending boundary, inside the missing regions. This band captures transition areas where geometric inconsistencies are most likely to occur. Our method achieves the lowest MAE, indicating closer agreement with the ground truth and more coherent geometry in these regions.

These results further confirm that our panorama fusion **does not exhibit alignment issues at overlapping regions**, thanks to our adopted blending strategy. 

We will include this discussion in the final version of our paper.

| Method      | Depth Transition Score (↓) | Transition Region MAE (↓) |
|:------------|---------------------------:|--------------------------:|
| Interpolation |                    *0.00389* |                   *0.03067* |
| Depth inpainting (Infusion [1])    |                    0.09529 |                   0.09177 |
| Harmonic Blending (Ours)      |                    **0.00328** |                   **0.00079** |

## (q.1) Varying the number of building blocks 

We provide additional experiments where we generate worlds of varying size.

**Qualitatively** ([anon link](https://anon-supp.github.io/), Section A), as visualized, SphericalDreamer can produce environments of various sizes, from short to long-range. 

**Quantitatively,** we further confirm this using our adopted metrics (BRISQUE, Coverage) and several new metrics (CLIP-score, C-CLIP, CLIP-IQA, and Q-Align), demonstrating that our generated worlds maintain similar levels of quality, global semantic consistency and prompt alignment as N increases.

We do not observe an intrinsic limit on the number of panoramas $N$ beyond which consistency breaks down. In practice, the main limiting factor is **computational cost**, rather than a fundamental issue with the method itself. We discuss computational costs below.

| Setting | BRISQUE (↓) | Coverage (↑) | CLIP-score (↑) | C-CLIP (↑) | CLIP-IQA (↑) | Q-Align (↑) |
|:-------|:---:|:---:|:---:|:---:|:---:|:---:|
| N=3 | 43.4683 | 0.9993 | 0.3418 | 0.8608 | 0.7582 | 2.3662 |
| N=4 | 42.2766 | 0.9993 | 0.3418 | 0.8471 | 0.7387 | 2.3057 |
| N=5 | 41.548 | 0.9994 | 0.3403 | 0.8447 | 0.7747 | 2.3088 |
| N=6 | 42.1268 | 0.9995 | 0.34 | 0.8499 | 0.7777 | 2.312 |
| N=7 | 41.5514 | 0.9994 | 0.3424 | 0.8453 | 0.7913 | 2.349 |

## (q.2) Runtime performance

We report the total runtime of our method for $N=2$, $N=3$, and $N=4$, along with a breakdown of the runtime for each component of the pipeline, measured on a single NVIDIA A100 GPU.

In brief, generating a 3D world from text with $N=3$ panoramas using our method and then rendering a video trajectory from it requires about 50 minutes. Furthermore, the generation time increases approximately linearly with the number of panoramas $N$ to be fused.


Indented rows denote sub-stages of the parent step:

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

---

We sincerely hope that our response resolves the concerns raised. If the reviewer has other technical points to discuss that may currently prevent them from reconsidering the score, we would be more than happy to discuss further.

## References

[1] Liu, Z., Ouyang, H., Wang, Q., Cheng, K. L., Xiao, J., Zhu, K., … Cao, Y. (2024). InFusion: Inpainting 3D Gaussians via Learning Depth Completion from Diffusion Prior. arXiv Preprint arXiv:2404. 11613.