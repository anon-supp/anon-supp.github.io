
We thank the reviewer for recognizing the **real gap** addressed by our work, the **coherent pipeline**, and **visually appealing results**.

All referenced tables, figures, and animated results are available at: https://anon-supp.github.io/

## On the novelty of our approach

Our **core contribution** is in the structured integration of techniques enabling **360° immersive and navigable text-to-3D world generation**, a capability not achieved by prior work, which inherently trade off immersivity for navigability, or vice versa. To our knowledge, our method is the **first** to jointly achieve both.

Key novel ideas include: (1) using **spherical building blocks** from panoramas, designed for omnidirectional coverage while remaining composable; (2) a **panorama-fusion pipeline** connecting adjacent spheres via midpoint rendering, inpainting, and 3D lifting for consistent expansion. The novelty lies in **how these components are unified** using **novel ideas** into a scalable generative pipeline.

## On the importance of Harmonic Blending

While harmonic blending builds on classical formulations, our contribution is in **adapting it to fuse newly generated depth with existing geometry** in an iterative text-to-3D pipeline, ensuring geometric continuity during expansion.

To support our design choice, we provide **new experiments for this rebuttal**: (1) an ablation replacing harmonic blending with three alternatives within our pipeline, and (2) an in-depth analysis on the **task of depth completion**.

### Ablation within our pipeline

We replace Harmonic Blending (HB) with naïve blending, bilinear interpolation, and InFusion [2] (diffusion-based depth inpainting).

**Qualitatively** (Section B, Figure 2), HB outperforms all alternatives, fully completing all missing regions.

**Quantitatively**, we compute C-CLIP (semantic consistency), CLIP-Score (text alignment), BRISQUE, CLIP-IQA, and Q-Align (rendering quality). HB outperforms all alternatives on every metric (Section B, Table 2).

### In-depth analysis

We mask portions of reference depth maps and reconstruct them with each method.

**Qualitatively** (Section E, Figure 5), HB provides the smoothest transitions without artifacts.

**Quantitatively** (Section E, Table 4), we report: **Depth Transition Score** (avg. absolute depth difference across the known/reconstructed boundary; lower = smoother) and **Depth Estimation Error** (MAE vs. ground-truth in a narrow band near the boundary). Our method achieves the best scores on both metrics.

## World consistency


We thank the reviewer for raising this important point.

In preliminary experiments, we explored cross-view conditioning strategies and observed **progressive semantic drift**, consistent with prior iterative completion methods [1]. As the scene expands, conditioning becomes increasingly biased toward recent views, leading to a loss of consistency with earlier content.

To address this, we adopt a **shared implicit memory strategy** by using the input prompt as a global conditioning signal across all panorama generations. We observe that modern text-to-image models maintain **strong semantic consistency across independently generated views** when the prompt is sufficiently detailed, effectively acting as a shared scene prior.

A key advantage of this design is that it avoids error accumulation over long trajectories, ensuring that distant regions remain as semantically consistent as nearby ones.

Combined with our geometric alignment (via fusion and blending), this approach preserves consistency without requiring explicit global optimization

We further support this with **new quantitative evaluations** using CLIP-Score and C-CLIP, which measure alignment with the prompt and cross-view consistency, respectively. Our method achieves the best performance under combined rotation and translation, indicating strong global consistency (Section G, Table 5).

We will clarify this design choice in the final version of the paper.

## Bigger worlds

We now provide **new experiments** with larger worlds.

**Qualitatively** (Section A, Figure 1), SphericalDreamer produces long-range environments.

**Quantitatively** (Section A, Table 1), metrics (BRISQUE, Coverage, CLIP-Score, C-CLIP, CLIP-IQA, Q-Align) remain stable as N increases from 3 to 7, confirming maintained quality and consistency.

---

We sincerely hope that our response resolves the concerns raised. If the reviewer has other technical points to discuss that may currently prevent them from reconsidering the score, we would be more than happy to discuss further.

## References

[1] Chung, J. et al. (2025). LucidDreamer: Domain-Free Generation of 3D Gaussian Splatting Scenes. IEEE TVCG, 31(12), 10640–10651.

[2] Liu, Z. et al. (2024). InFusion: Inpainting 3D Gaussians via Learning Depth Completion from Diffusion Prior. arXiv:2404.11613.
