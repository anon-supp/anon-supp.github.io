
We thank the reviewer for recognizing the **solid theoretical foundation**, the method's **superiority in maintaining immersivity and navigability**, and the **highly original and effective solution** to multi-panorama fusion.

All referenced tables, figures, and animated results are available at: https://anon-supp.github.io/

## Extended evaluation

In this rebuttal, we strengthen the evaluation with (i) **new metrics** capturing visual quality, consistency, and geometric accuracy, (ii) **new ablations**, and (iii) **new detailed analysis** of core submodules (LDI and Harmonic Blending).

### Quality evaluation

We now adopt CLIP-IQA and Q-Align alongside BRISQUE. SphericalDreamer achieves the best quality on all three metrics under combined rotation and translation (Section G, Table 6).

### Text-alignment and semantic consistency

We now evaluate text alignment via CLIP-Score and global semantic consistency via C-CLIP. Our method achieves the best results under both rotation and translation, confirming prompt alignment and high global semantic consistency across the generated worlds (Section G, Table 5).

### Geometry evaluation

We evaluate geometry via two complementary approaches.

#### a. Evaluation via predicted depth

We now compare depth maps from SphericalDreamer with other 360° depth estimation models.

**Qualitatively** (Section D, Figure 4), our depth maps are the most accurate with the fewest artifacts.

**Quantitatively** (Section D, Table 3), we evaluate on Replica2K using AbsRel, RMSE, SI-RMSE, and accuracy thresholds (δ<1.25, δ<1.25², δ<1.25³). Our approach **consistently outperforms all baselines** across every metric.

#### b. Evaluation via image quality metrics

The image quality metrics (CLIP-IQA, Q-Align) presented above also reflect geometric consistency, as geometric artifacts degrade visual quality. Our best-in-class results further support the quality of the underlying geometry.

### Ablation study

We now ablate two key components: Harmonic Blending (HB) and LDI. We remove LDI, and replace HB with naïve blending, bilinear interpolation, and InFusion [5] (diffusion-based depth inpainting).

**Qualitatively** (Section B, Figure 2), replacing HB causes geometry artifacts in transition regions; removing LDI introduces disocclusion artifacts with unfilled regions. The full model produces complete, coherent environments.

**Quantitatively** (Section B, Table 2), we evaluate C-CLIP, CLIP-Score, BRISQUE, CLIP-IQA, Q-Align, and Coverage. Both ablations cause consistent drops across all metrics. HB improves completeness and visual quality; LDI is critical for handling occlusions and maintaining consistency.

### Further evaluation of HB and LDI

#### LDI comparison with prior approaches

We now provide **new comparisons** of our LDI with LayerPano3D and 3D Photography in Section C, Figure 3. SphericalDreamer produces more realistic background panoramas without artifacts, owing to accurate foreground segmentation and occlusion-aware mask estimation.

#### Harmonic blending vs. simpler alternatives

We now mask regions of reference depth maps and reconstruct them with each method.

**Qualitatively** (Section E, Figure 5), HB produces the smoothest transitions without artifacts.

**Quantitatively** (Section E, Table 4), HB achieves the best **Depth Transition Score** (boundary discontinuity; lower = smoother) and **Depth Estimation Error** (MAE vs. ground-truth near boundary), confirming seamless alignment in overlapping areas.

We will include this analysis in the final paper.

## Dealing with highly non-linear camera trajectories

Harmonic blending is formulated generally and is not restricted to linear trajectories (cf. Figure 8). We focus on linear trajectories in experiments for simplicity and comparability with prior work.

---

We sincerely hope that our response resolves the concerns raised. If the reviewer has other technical points to discuss that may currently prevent them from reconsidering the score, we would be more than happy to discuss further.

## References

[1] Wang, F.-E., et al. (2023). BiFuse++. IEEE TPAMI, 45(5), 5448–5460.
[2] Yun, I., et al. (2023). EGformer. ICCV, 6078–6089.
[3] Sun, C., Sun, M., & Chen, H.-T. (2021). HoHoNet. CVPR, 2573–2582.
[4] Su, D., et al. (2025). UniFuse. ICCV, 14238–14247.
[5] Liu, Z., et al. (2024). InFusion. arXiv:2404.11613.
