
We thank the reviewer for their review and remarks.  We especially appreciate that the reviewer found our work to be **intuitive and clear**, **well structured and easy to follow**, with **experiments showing the effectiveness of our method**.

We address the reviewer's concerns below.

Please note that we provide additional animated results at the following anonymous link: https://anon-supp.github.io/ . All additional results will be integrated in the final version of our paper.

## (w.1 + q1) Evaluation of geometry, cross-view consistency and quality


We thank the reviewers for highlighting the need for a more comprehensive evaluation of geometry, cross-view consistency and quality. In response, we introduce additional quantitative and qualitative analyses that explicitly assess these aspects. In particular, we evaluate geometric fidelity both directly through depth predictions and indirectly via perceptual quality metrics, and we measure cross-view consistency using dedicated vision–language metrics.


### (q1) Cross-view consistency

To support our claim on world consistency, we provide new **quantitative** evaluations in which we compute CLIP-Score and C-CLIP metrics between various views of our generated worlds. Those metrics are specifically designed to measure view consistency w.r.t text (CLIP-Score) and other views (C-CLIP). Our method presents the best results when both rotation and translation are considered, highlighting the semantic consistency of our generated worlds over large distances.


| Method | CLIP-score (↑) | C-CLIP (↑) |
|:-------|:---:|:---:|
| LucidDreamer | *0.2988* | 0.6599 |
| LayerPano3D | 0.2639 | 0.5787 |
| WonderJourney | 0.2570 | 0.6149 |
| SceneScape | 0.2802 | *0.7866* |
| **SphericalDreamer (ours)** | **0.3325** | **0.8433** |


As such, our method indeed remains consistent across translation. We also confirm this **qualitatively** by generating bigger worlds ([anon link](https://anon-supp.github.io/), Section A).

### (w1) Geometry: 

To evaluate the geometry of our generated worlds, we adopt two complementary approaches. First, we directly assess geometry by evaluating the predicted depth. Second, we evaluate geometry more implicitly using perceptual quality metrics (CLIP-IQA and Q-Align), which capture overall visual realism.

#### (w1.a) Evaluation of geometry via predicted depth 

We evaluate the geometry of our generated 3D worlds by comparing the predicted depth maps in SphericalDreamer with other 360$^\circ$ depth estimation models. 

**Qualitatively,** ([anon link](https://anon-supp.github.io/), section D), we observe that the depth maps computed in SphericalDreamer are the most accurate and present the least artifacts compared to other approaches.

**Quantitatively,** we report comparisons against these baselines on the Replica2K dataset using standard depth evaluation metrics, including Absolute Relative Error (AbsRel), Root Mean Squared Error (RMSE), and Scale-Invariant RMSE (SI-RMSE). We also include accuracy metrics (δ thresholds), which measure the proportion of pixels whose predicted depth falls within increasing error margins (1.25, 1.25², and 1.25³), corresponding to approximately 25%, 56%, and 95% relative error. **In brief,** our approach **consistently outperforms all baselines** across every evaluated metric.

| Model | AbsRel (↓) | RMSE (↓) | SI-RMSE (↓) | δ<1.25 (↑) | δ<1.25² (↑) | δ<1.25³ (↑) |
|:------|:----------:|:--------:|:----------:|:----------:|:-----------:|:-----------:|
| BiFuseV2 [1] | 1.0077 | 1.8958 | 1.0858 | 0.1736 | 0.3368 | 0.4906 |
| EGFormer [2] | 0.8048 | 1.6097 | 0.8338 | 0.2107 | 0.3952 | 0.5744 |
| HoHoNet [3]  | 1.1524 | 2.0839 | 1.1094 | 0.1711 | 0.3301 | 0.4723 |
| UniFuse [4] | 1.0445 | 1.9659 | 1.1372 | 0.1738 | 0.3250 | 0.4706 |
| **SphericalDreamer (via 360monodepth)** | **0.1605** | **0.6008** | **0.2039** | **0.7363** | **0.9317** | **0.9819** |


#### (w1.b) Evaluation of geometry via image quality metrics

In addition to depth-based evaluation, we assess geometry indirectly using perceptual image quality metrics (CLIP-IQA and Q-Align). These metrics operate in the 2D domain but reflect underlying geometric consistency, as geometric artifacts typically degrade visual quality.

The new evaluation is conducted against other 3D world generation baselines. Our method presents the best results when both translation and rotation are considered, which validates the quality of the underlying geometry. 


| Method | CLIP-IQA (↑) | | | | Q-Align (↑) | | | |
|:-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| | trans | rot | rot+trans | mean | trans | rot | rot+trans | mean |
| LucidDreamer | 0.6521 | **0.8437** | *0.6237* | *0.7065* | 2.0275 | **2.4182** | *1.8908* | *2.1120* |
| LayerPano3D | 0.4295 | 0.7740 | 0.5077 | 0.5704 | 1.7682 | *2.3579* | 1.7943 | 1.9730 |
| WonderJourney | **0.8975** | 0.5378 | 0.5006 | 0.6453 | 2.0634 | 1.5572 | 1.6017 | 1.7410 |
| SceneScape | 0.7930 | 0.3874 | 0.3805 | 0.5203 | *2.2070* | 1.7355 | 1.7231 | 1.8890 |
| **SphericalDreamer (ours)** | *0.8623* | *0.7973* | **0.7014** | **0.7870** | **2.5083** | 2.2813 | **2.3088** | **2.3660** |

## (w.2 + q.2) Ablation studies and analysis


### Ablation study of LDI (qualitative + quantitative)

We provide an ablation study where we ablate our LDI and compare it with the full SphericalDreamer pipeline. 

**Qualitatively,** ([anon link](https://anon-supp.github.io/), Section B) ablating LDI leads to visible occlusion artifacts, with unfilled regions appearing in the generated environment due to missing background content.

**Quantitatively,** as seen in the table below, the quality, coverage and cross-view consistency metrics all drop when ablating LDI, demonstrating its significance. 

| Setting | BRISQUE (↓) | Coverage (↑) | CLIP-score (↑) | C-CLIP (↑) | CLIP-IQA (↑) | Q-Align (↑) |
|:-------|:---:|:---:|:---:|:---:|:---:|:---:|
| no LDI | 45.8937 | 0.9652 | 0.3371 | 0.8459 | 0.7358 | 2.1935 |
| Ours | **43.4709** | **0.9993** | **0.3418** | **0.8608** | **0.7582** | **2.366** |


### Comparison of SphericalDreamer's LDI with prior approaches  

We provide **new comparisons** in Section C ([anon link](https://anon-supp.github.io/)) where we compare the LDI construction of SphericalDreamer with other layered representations, including those used in LayerPano3D and 3D Photography.

As shown in the figure, SphericalDreamer produces more realistic background panoramas and without artifacts, owing to more accurate foreground segmentation and occlusion-aware mask estimation.

## (q.3) Bigger world sizes

We provide additional experiments where we generate worlds of varying size.

**Qualitatively** ([anon link](https://anon-supp.github.io/), Section A), as visualized, SphericalDreamer can produce environments of various sizes, from short to long-range. 

**Quantitatively,** we further confirm this using our adopted metrics (BRISQUE, Coverage) and several new metrics (CLIP-score, C-CLIP, CLIP-IQA, and Q-Align), demonstrating that our generated worlds maintain similar levels of quality, global semantic consistency and prompt alignment as N increases.

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

[1] Wang, F.-E., Yeh, Y.-H., Tsai, Y.-H., Chiu, W.-C., & Sun, M. (2023). BiFuse++: Self-Supervised and Efficient Bi-Projection Fusion for 360° Depth Estimation. IEEE Transactions on Pattern Analysis and Machine Intelligence, 45(5), 5448–5460. doi:10.1109/TPAMI.2022.3203516

[2] Yun, I., Shin, C., Lee, H., Lee, H.-J., & Rhee, C. E. (2023, October). EGformer: Equirectangular Geometry-biased Transformer for 360 Depth Estimation. 2023 IEEE/CVF International Conference on Computer Vision (ICCV), 6078–6089. doi:10.1109/ICCV51070.2023.00561

[3] Sun, C., Sun, M., & Chen, H.-T. (2021, June). HoHoNet: 360 Indoor Holistic Understanding With Latent Horizontal Features. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2573–2582.

[4] Su, D., Zhang, Y., Li, H., Li, J., & Liu, Y. (2025, October). UniFuse: A Unified All-in-One Framework for Multi-Modal Medical Image Fusion Under Diverse Degradations and Misalignments. Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 14238–14247.