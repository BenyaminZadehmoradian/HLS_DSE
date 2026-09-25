# RW0070 — Fovea: Physical-Implication-Aware Wafer-Scale DSE with Decision-Domain-Guided Cross-Fidelity Refinement

> **Relevance (2026-09-25 full-text review): SUPPORTING** — Hardware DSE (wafer-scale LLM-training systems), not HLS/FPGA, so not CORE, but the closest conceptual precedent for S99's principle that expensive evidence is bought only when it can change a decision: a measured cheap-to-reference disagreement bound defines a Decision Domain that provably contains the reference optimum when the bound is valid, validated against exhaustive reference results as S97/S04 would do. Primary Studies: S99 S98 S97 S04 S72. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** none (arXiv:2608.03285v1, 4 Aug 2026; Jinxi Li, Huizheng Wang, Jinyi Deng, Yang Hu, Shouyi Yin, Tsinghua).

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Li, Jinxi; Wang, Huizheng; Deng, Jinyi; Hu, Yang; Yin, Shouyi
- Year / venue: 2026 / arXiv 2608.03285
- DOI: none recorded · URL: https://arxiv.org/abs/2608.03285

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: arxiv v1
- Canonical path: `related_work/papers/multifidelity/RW0070_Li2026_Fovea_arXiv.pdf` (local only, gitignored)
- SHA-256: `30a7de2bcdf60e3bbf151abc7d5e1087539d66b1af07fd178fdcefb0d3d9b065`
- Source: https://arxiv.org/pdf/2608.03285

## Code provenance
NOT_REPORTED

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Workload-specific wafer-scale architecture selection where a cheap analytical evaluator shows ranking inversions against a ~4000x costlier reference, making a fixed top-k shortlist unreliable.

## 2. Problem setting / 3. Search space / 4. Evaluation method
Stage I: physical-implication-aware space formulation (reticle, tiling, area budget, D2D capability, die-edge placement) plus exact local reductions. Stage II: e(d) = |P_L(d)/P_R(d) - 1|, eps = max e(d); under a valid bound P_L/(1+eps) <= P_R <= P_L/(1-eps); cutoff R(eps) = ((1-eps)/(1+eps)) P_L(d*_L); Decision Domain C(eps) = {d : P_L(d) >= R(eps)}. Guarantee (Eq. 11): if eps bounds the disagreement over all of D, every reference optimum lies in C(eps) — deterministic but conditional; no probabilistic guarantee for the estimated eps. Practice: evaluate the full space analytically, reference-evaluate a uniform 10% sample, eps_hat = max over the sample, reference-evaluate C(eps_hat). One-shot, single scalar objective.

## 5. Benchmarks
10 reference-verifiable design spaces (179-5,655 candidates) x 7 LLM-training workloads = 70 pairs; construction sweep up to 46,782 candidates.

## 6. Hardware
Modelled wafer-scale chips (no silicon); single Intel i7-6850K server.

## 7. Toolchain
Chakra traces; ASTRA-sim analytical backend; ASTRA-sim + ns-3 reference; gem5 Garnet 3.0 cross-validation.

## 8. Metrics
Exact recovery of the exhaustive-reference optimum; normalized performance; Decision-Domain fraction; reference fraction; speedup; Spearman rho; inversion rate; top-k recall.

## 9. Baselines
Exhaustive reference/analytical, simulated annealing, Theseus (multi-fidelity MOBO), Polaris (multi-fidelity DSE) at 25% of exhaustive-reference runtime.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: Table V: exact optimum recovered in 1400/1400 runs (worst normalized 1.000) vs Polaris 84.86%, Theseus 25.50%, SA 24.14%, exhaustive analytical 7.14%. Table IV: Decision Domain averages 13.58% of D (max 50.37%); total reference fraction 20.42%. Fig. 9: 24.21% of exhaustive runtime (4.13x average, 7.80x max speedup). Analytical 2.49 s/design vs reference 2.78 h/design; Spearman 0.7752; inversion rate 20.96%; top-10% recall 64.94%; largest eps underestimate 1.47 pp.

## 11. Limitations
AUTHOR-STATED: homogeneous repeated-die scope; simulator reference; eps_hat may underestimate eps; containment conditional on a valid bound. REVIEWER: full space must be evaluated cheaply (<~5.6k); single scalar objective (ratio bound does not extend directly to Pareto fronts); worst-case max bound is conservative; 10% rate tuned on the same family of spaces; baselines not budget-matched; no code.

## 12. What the paper does NOT evaluate
Multi-objective; sequential acquisition; heterogeneous dies; silicon; energy; probabilistic guarantees; very large spaces.

## 13. Relationship to our Studies (S99 S98 S97 S04 S72)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | joint plan choice under shared constraints; no local-vs-joint component evaluation |
| measured interactions | PARTIAL | coupled physical implications modelled; disagreement is between evaluators |
| staged evaluation | YES | formulation, analytical screening, calibration, reference evaluation |
| adaptive evidence acquisition | PARTIAL | one-shot bound-based selection after calibration |
| cost/fidelity modeling | YES | ~4000x cost gap, disagreement bound, full runtime accounting |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | PARTIAL | modelled reticle/tiling/D2D/edge feasibility; no P&R |
| multi-benchmark transfer | PARTIAL | 70 pairs; leave-one-space-out calibration rate |
| decision/Pareto stability | YES | exact recovery over 20 calibration draws per pair |
| energy/power | NO |  |
| CPU-FPGA interaction | NOT_APPLICABLE |  |
| memory/data movement | PARTIAL | memory capacity/bandwidth as knobs |

## 14. Possible overlap
PARTIAL OVERLAP

## 15. Possible research gap (not a novelty claim)
S99 can adopt a Pareto analogue of Eq. 10: a kernel combination needs joint evaluation only if its optimistic joint vector (composed-local corrected by the S98 residual bound) is not dominated by the pessimistic vectors of the current front. S98 supplies eps; S97's exhaustive joint oracle checks containment. Because the guarantee needs a worst-case bound, S98 must report maximum residuals, not only means. S99's novelty must rest on multi-kernel composition and Pareto feasibility, since single-objective decision-domain pruning in hardware DSE is prior art.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED.
