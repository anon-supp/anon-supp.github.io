
We thank the reviewer for finding our work **intuitive and clear**, **well structured**, with **experiments showing the effectiveness of our method**.

All referenced tables, figures, and animated results are available at: https://anon-supp.github.io/

## (w.1 + q1) Evaluation of geometry, cross-view consistency, and quality

In this rebuttal, we introduce **new** quantitative and qualitative analyses assessing geometric fidelity, cross-view consistency, and perceptual quality.

### (q1) Cross-view consistency

We now compute CLIP-Score and C-CLIP between various views of generated worlds. These metrics measure view consistency w.r.t. text (CLIP-Score) and other views (C-CLIP). Our method achieves the best results under both rotation and translation, confirming semantic consistency over large distances (Section G, Table 5).

We also confirm this **qualitatively** by generating larger worlds (Section A, Figure 1).

### (w1) Geometry

We evaluate geometry via two complementary approaches: direct depth assessment and indirect perceptual quality metrics.

#### (w1.a) Evaluation via predicted depth

We now compare depth maps from SphericalDreamer with other 360° depth estimation models.

**Qualitatively** (Section D, Figure 4), our depth maps are the most accurate with the fewest artifacts.

**Quantitatively** (Section D, Table 3), we evaluate on Replica2K using AbsRel, RMSE, SI-RMSE, and accuracy thresholds (δ<1.25, δ<1.25², δ<1.25³). Our approach **consistently outperforms all baselines** across every metric.

#### (w1.b) Evaluation via image quality metrics

We assess geometry indirectly using CLIP-IQA and Q-Align, which reflect geometric consistency since artifacts degrade visual quality. Our method achieves the best results under combined rotation and translation, validating underlying geometry quality (Section G, Table 6).

## (w.2 + q.2) Ablation studies and analysis

### Ablation of LDI

We now ablate LDI and compare with the full pipeline.

**Qualitatively** (Section B, Figure 2), removing LDI causes visible occlusion artifacts with unfilled background regions.

**Quantitatively** (Section B, Table 2), quality, coverage, and cross-view consistency metrics all drop without LDI.

### Comparison of SphericalDreamer's LDI with prior approaches

We now provide **new comparisons** of our LDI construction with LayerPano3D and 3D Photography in Section C, Figure 3. SphericalDreamer produces more realistic background panoramas without artifacts, owing to more accurate foreground segmentation and occlusion-aware mask estimation.

## (q.3) Bigger world sizes

We now provide **new experiments** with worlds of varying size (N=3 to N=7).

**Qualitatively** (Section A, Figure 1), SphericalDreamer produces short to long-range environments.

**Quantitatively** (Section A, Table 1), BRISQUE, Coverage, CLIP-Score, C-CLIP, CLIP-IQA, and Q-Align remain stable as N increases, confirming maintained quality and consistency.

---

We sincerely hope that our response resolves the concerns raised. If the reviewer has other technical points to discuss that may currently prevent them from reconsidering the score, we would be more than happy to discuss further.

## References

[1] Wang, F.-E., et al. (2023). BiFuse++. IEEE TPAMI, 45(5), 5448–5460.

[2] Yun, I., et al. (2023). EGformer. ICCV, 6078–6089.

[3] Sun, C., Sun, M., & Chen, H.-T. (2021). HoHoNet. CVPR, 2573–2582.

[4] Su, D., et al. (2025). UniFuse. ICCV, 14238–14247.
