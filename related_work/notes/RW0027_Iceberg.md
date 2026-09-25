# RW0027 — Iceberg: Enhancing HLS Modeling with Synthetic Data

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Ding, Zijian; Nguyen, Tung; Li, Weikai; Grover, Aditya; Sun, Yizhou; Cong, Jason
- Year / venue: 2025 / ICLAD
- DOI: 10.1109/ICLAD65226.2025.00032 · URL: https://doi.org/10.1109/ICLAD65226.2025.00032
- Metadata source: PDF first page (IEEE Xplore header with DOI, 2025 IEEE International Conference on LLM-Aided Design)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/hls_dse/RW0027_Ding2025_Iceberg_ICLAD.pdf`
- SHA-256: `ae8c9505e90524abfecb69e0ddc3815cd4911a156ce636abe3faf29b0686d18c`
- Source: /home/benyamin/Desktop/Library/Iceberg: Enhancing HLS Modeling with Synthetic Data.pdf

## Code / dataset / artifact provenance
Code: https://github.com/UCLA-VAST/iceberg ; synthetic programs released

## 1. Research question
Deep-learning HLS QoR predictors generalize poorly to new kernels because public datasets lack diversity in programs and in labeled design configurations, and labels are expensive to obtain.

## 2. Problem setting
Few-shot adaptation of HLS performance (latency) surrogates to unseen programs for Merlin-pragma DSE.

## 3. Search space
Merlin pragmas per loop: PIPELINE (off/cg/fg), PARALLEL factor, TILE factor (used for offline DSE evaluation)

## 4. Evaluation method
Prediction MSE on held-out programs using Vitis HLS 2023.2 labels; offline best@K optimization on sampled designs with actual HLS labels.

## 5. Benchmarks
HLSyn (10 test programs), six real-world apps from Rosetta and attention-layer kernels (e.g., att-3mm, 2D convolution), Iceberg synthetic dataset

## 6. Hardware
NOT_REPORTED

## 7. Toolchain
Vitis HLS 2023.2; Merlin; AutoDSE (label collection); HARP encoder

## 8. Metrics
Test MSE (geometric mean), best@1 offline optimization

## 9. Baselines
HARP, Hierarchical-MoE (H-MoE); GP-based synthetic functions (ablation)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: improves geometric-mean modeling accuracy by 86.4% when adapting to six real-world applications with few-shot examples, and achieves 2.47x and 1.12x better offline DSE performance on two test datasets; pretraining on Iceberg raises HARP accuracy by 80% and H-MoE by 10%.

## 11. Limitations
Only latency modeled (resource/validity delegated to H-MoE); modeling gains do not always translate to optimization gains on real-world apps; weak-label quality degrades on diverse Iceberg programs; offline evaluation only.

## 12. What the paper does NOT evaluate
Online DSE; resource/timing/power prediction; post-route QoR; multi-kernel interactions; device transfer.

## 13. Relationship to our Studies
- Direct (dimension = YES): S10 S11 S90
- Partial (dimension = PARTIAL): S04 S06 S21 S71 S72

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Per-program designs |
| measured interactions | NO | Not studied |
| staged evaluation | NO | Offline top-K selection only |
| adaptive evidence acquisition | NO | No acquisition loop (online evaluation left to future work) |
| cost/fidelity modeling | PARTIAL | Combines expensive actual HLS labels with cheap weak labels from surrogate ensembles |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | NO | HLS labels only |
| multi-benchmark transfer | YES | Few-shot adaptation to unseen HLSyn and real-world programs |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not modeled |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | NO | Not modeled |

## 14. Possible overlap
PARTIAL OVERLAP on: multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; measured interactions; adaptive evidence acquisition; staged evaluation; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/UCLA-VAST/iceberg ; synthetic programs released

## Open questions / reviewer notes
Abstract numbers (2.47x, 1.12x offline DSE) not re-derived from tables in extracted text.
