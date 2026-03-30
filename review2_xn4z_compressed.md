
We thank the reviewer for finding our work **particularly impressive**, with **strong performance** and an idea that is **both novel and promising**.

All referenced tables, figures, and animated results are available at: https://anon-supp.github.io/

## (w.1) On the reliance on monocular depth estimators

Inaccuracies in monocular depth estimation degrade geometric quality. However, this limitation is **not specific to SphericalDreamer**: all compared baselines equally rely on depth estimation. This is a **broader limitation of the current paradigm**, not of our method. We will include additional discussion in the final paper.

## (w.2) More diverse scenes

As noted in our limitations, SphericalDreamer is better suited to outdoor/natural environments due to its reliance on spherical imagery, which is less effective for structured planar geometry (urban/indoor scenes). In the camera-ready, we will explicitly scope our claims to outdoor and natural settings in the abstract, introduction, and experiments, preventing misinterpretation of the method as universally applicable.

## (w.3) Alignment of adjacent spheres

The **only potential source of geometric misalignment** is at the panorama fusion stage. World assembly is a direct aggregation of already-aligned blocks and introduces no additional distortion. **Harmonic blending** ensures smooth geometric transitions at fusion boundaries.

We validate this through **two new evaluations for this rebuttal**:

### Ablation within our pipeline

We replace Harmonic Blending (HB) with naïve blending, bilinear interpolation, and InFusion [1] (diffusion-based depth inpainting).

**Qualitatively** (Section B, Figure 2), HB outperforms all alternatives, fully completing all missing regions.

**Quantitatively** (Section B, Table 2), we compute C-CLIP, CLIP-Score, BRISQUE, CLIP-IQA, and Q-Align. HB outperforms all alternatives on every metric.

### In-depth analysis

We mask portions of reference depth maps and reconstruct them with each method.

**Qualitatively** (Section E, Figure 5), HB provides the smoothest transitions without artifacts.

**Quantitatively** (Section E, Table 4), we report **Depth Transition Score** (boundary discontinuity; lower = smoother) and **Depth Estimation Error** (MAE vs. ground-truth near boundary). HB achieves the best scores on both, confirming that panorama fusion **does not exhibit alignment issues** at overlapping regions.

We will include this discussion in the final paper.

## (q.1) Varying the number of building blocks

We now provide **new experiments** with worlds of varying size (N=3 to N=7).

**Qualitatively** (Section A, Figure 1), SphericalDreamer produces short to long-range environments.

**Quantitatively** (Section A, Table 1), BRISQUE, Coverage, CLIP-Score, C-CLIP, CLIP-IQA, and Q-Align remain stable as N increases, confirming maintained quality and consistency. No intrinsic limit on N was observed; the main constraint is **computational cost**.

## (q.2) Runtime performance

We now report total runtime and per-component breakdown for N=2, N=3, and N=4 on a single NVIDIA A100 GPU (Section H, Table 7).

Generating a 3D world with N=3 panoramas and rendering a video trajectory takes ~50 minutes. Generation time scales approximately linearly with N.

---

We sincerely hope that our response resolves the concerns raised. If the reviewer has other technical points to discuss that may currently prevent them from reconsidering the score, we would be more than happy to discuss further.

## References

[1] Liu, Z., Ouyang, H., Wang, Q., Cheng, K. L., Xiao, J., Zhu, K., … Cao, Y. (2024). InFusion: Inpainting 3D Gaussians via Learning Depth Completion from Diffusion Prior. arXiv:2404.11613.
