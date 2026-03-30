
We thank the reviewer for their review and remarks.  We especially appreciate that the reviewer found our work to be targeting a **real gap** in the current literature, with a an **easy to follow system**, **coherent pipeline**, and **visually appealing results**.

We address the reviewer's concerns below.

Please note that we provide additional animated results at the following anonymous link: https://anon-supp.github.io/ . All additional results will be integrated in the final version of our paper.

## On the novelty of our approach

The **core of our contribution** lies in the structured integration of well-known techniques to enable a capability not achieved by prior work: **360$^\circ$ immersive and navigable text-to-3D world generation**. As outlined in the paper, prior approaches inherently trade off between these two properties. To the best of our knowledge, our method is the **first** to jointly achieve both immersivity and navigability.

To realize this, we introduce several key ideas that go beyond a direct combination of existing components. First, we propose using **spherical building blocks** derived from panoramas, explicitly designed to support omnidirectional coverage while remaining composable for large-scale scene construction. Second, we introduce a novel **panorama-fusion pipeline** that connects adjacent spheres through midpoint rendering, inpainting, and 3D lifting, enabling consistent expansion of the environment. 

While our approach leverages off-the-shelf modules, the novelty lies in **how these components are integrated into a unified generative pipeline**, using **novel ideas** that enables scalable, immersive, and navigable world generation.



## On the importance of Harmonic Blending

While harmonic blending itself builds on classical formulations,, our contribution is in **adapting it as a mechanism to fuse newly generated depth with existing geometry in an iterative text-to-3D pipeline**, where it is critical for maintaining geometric continuity during expansion.

To support our design choice of Harmonic Blending, we **provide new experiments**. 

First, we conduct an ablation study in which harmonic blending is replaced by three simpler alternatives, highlighting its importance **within our pipeline**. Second, we provide a more in-depth analysis by comparing harmonic blending with these alternatives on the specific **task of depth completion**. This offers a clearer and more direct understanding of why harmonic blending is more effective.

### Ablating Harmonic Blending in our pipeline

We validate the use of Harmonic Blending in our pipeline by performing an ablation study where we replace it by three simpler alternatives: naïve blending, depth inpaiting via bilinear interpolation, and depth inpainting via InFusion [2], a diffusion based depth-inpainting model.

**Qualitatively,** ([anon link](https://anon-supp.github.io/), Section B), we observe that harmonic blending outperforms its alternatives: it successfully completes all missing regions in the world, whereas the alternatives often leave incomplete or inconsistent areas.

**Quantitatively,** we compute various scores to validate our results:
- C-CLIP to measure the semantic consistency across the world,
- CLIP-Score to measure text alignment,
- BRISQUE, CLIP-IQA, and Q-Align to measure rendering quality.

**In brief,** using Harmonic Blending (HB) produce 3D worlds that outperform those produced with its alternatives on all of the metrics.


| Setting | BRISQUE (↓) | Coverage (↑) | clip-score (↑) | c-clip (↑) | CLIP-IQA (↑) | Q-Align (↑) |
|:-------|:---:|:---:|:---:|:---:|:---:|:---:|
| no HB (naive instead) | 47.1084 | 0.9242 | 0.3253 | 0.8001 | 0.6503 | 1.9953 |
| no HB (inpainting instead) | *44.3742* | 0.9314 | 0.3272 | 0.8099 | 0.5976 | 2.078 |
| no HB (interpolation instead) | 45.4247 | *0.9835* | *0.3377* | *0.8496* | *0.7505* | *2.2595* |
| Ours | **43.4709** | **0.9993** | **0.3418** | **0.8608** | **0.7582** | **2.366** |



### In-depth analysis

We conduct an in-depth analysis to further compare harmonic blending with the three alternatives listed above for the task of depth completion. In these experiments, we first mask out a portion of the reference depth map and then predict the missing regions using each method, enabling a direct comparison of their performance. 

**Qualitatively** ([anon link](https://anon-supp.github.io/), Section E), we can see that harmonic blending provides the smoothest transition between known depth regions and estimated regions, without causing any artifacts.

**Quantitatively,** we compute two metrics to confirm our findings:
- The **Depth Transition Score** is defined as the average absolute difference in depth values across pixels on either side of the boundary between known and reconstructed regions, where lower values indicate smoother transitions. Our approach presents the best transition score, indicating that it enables the smoothest transition between known and unknown depth.
- The **Depth Estimation Error** measures the difference between predicted and ground-truth depth values within a narrow band along the blending boundary, inside the missing regions. This band captures transition areas where geometric inconsistencies are most likely to occur. Our method achieves the lowest MAE, indicating closer agreement with the ground truth and more coherent geometry in these regions.


| Method      | Depth Transition Score (↓) | Transition Region MAE (↓) |
|:------------|---------------------------:|--------------------------:|
| Interpolation |                    *0.00389* |                   *0.03067* |
| Depth inpainting (Infusion [2])    |                    0.09529 |                   0.09177 |
| Harmonic Blending (Ours)      |                    **0.00328** |                   **0.00079** |


## World consistency

We thank the reviewer for raising this important point regarding global consistency.

In fact, when designing our method, we explored cross-view conditioning strategies and observed **progressive semantic drift accumulation**, consistent with prior iterative completion methods [1]. This mainly happens because as the scene expands, conditioning becomes increasingly biased toward recently generated views, leading to a gradual loss of semantic consistency with earlier content.

To mitigate this issue, we decided to adopt a **shared implicit memory strategy**, which relates to what the reviewer is proposing (although not elaborated upon in the paper). 
In fact, we have observed that modern text-to-image models maintain **strong semantic consistency** across independently generated views when the prompt is **sufficiently detailed**, effectively serving as a shared scene prior. This allows us to use **the prompt itself** as a global conditioning signal across all panorama generations, effectively acting as a **shared world memory**.

A key advantage of this design is that it prevents error accumulation over long trajectories. As a result, distant regions of the generated world remain as semantically close with the initial regions as nearby ones (unlike [1]).

Combined with our geometric and semantic alignment (via fusion and blending), this approach preserves consistency without requiring explicit global optimization, as observed in our initial qualitative visualizations of generated worlds.

To further support our claim on world consistency, we provide additional quantitative evaluations in which we compute CLIP-Score and C-CLIP metrics using various views of our generated worlds. Those metrics are specifically designed to measure semantic consitency w.r.t text (CLIP-Score) and other views (C-CLIP). Compared to baselines, our method presents the best results when both rotation and translation are considered, highlighting that our generated worlds are globally semantically consistent over large distances.

We will clarify this design choice and include this discussion in the final paper.

| Method | CLIP-score (↑) | C-CLIP (↑) |
|:-------|:---:|:---:|
| LucidDreamer | *0.2988* | 0.6599 |
| LayerPano3D | 0.2639 | 0.5787 |
| WonderJourney | 0.2570 | 0.6149 |
| SceneScape | 0.2802 | *0.7866* |
| **SphericalDreamer (ours)** | **0.3325** | **0.8433** |

## Bigger worlds

We provide additional experiments where we generate bigger worlds. 

**Qualitatively** ([anon link](https://anon-supp.github.io/), Section A), the videos show that SphericalDreamer can produce long-range environment. 

**Quantitatively,** we further confirm this using our previously adopted metrics (BRISQUE, Coverage) and new metrics (CLIP-score, C-CLIP, CLIP-IQA, and Q-Align), demonstrating that our generated worlds maintain similar levels of quality, global semantic consistency and prompt alignment as N increases.


| Setting | BRISQUE (↓) | Coverage (↑) | CLIP-score (↑) | C-CLIP (↑) | CLIP-IQA (↑) | Q-Align (↑) |
|:-------|:---:|:---:|:---:|:---:|:---:|:---:|
| N=3 | 43.4683 | 0.9993 | 0.3418 | 0.8608 | 0.7582 | 2.3662 |
| N=4 | 42.2766 | 0.9993 | 0.3418 | 0.8471 | 0.7387 | 2.3057 |
| N=5 | 41.548 | 0.9994 | 0.3403 | 0.8447 | 0.7747 | 2.3088 |
| N=6 | 42.1268 | 0.9995 | 0.34 | 0.8499 | 0.7777 | 2.312 |
| N=7 | 41.5514 | 0.9994 | 0.3424 | 0.8453 | 0.7913 | 2.349 |

---

We sincerely hope that our response resolves the concerns raised. If the reviewer has other technical points to discuss that may currently prevent them from reconsidering the score, we would be more than happy to discuss further.

## References

[1] Chung, J., Lee, S., Nam, H., Lee, J., & Lee, K. M. (2025). LucidDreamer: Domain-Free Generation of 3D Gaussian Splatting Scenes. IEEE Transactions on Visualization and Computer Graphics, 31(12), 10640–10651. doi:10.1109/TVCG.2025.3611489

[2] Liu, Z., Ouyang, H., Wang, Q., Cheng, K. L., Xiao, J., Zhu, K., … Cao, Y. (2024). InFusion: Inpainting 3D Gaussians via Learning Depth Completion from Diffusion Prior. arXiv Preprint arXiv:2404. 11613.