# RW0024 — Balor: HLS Source Code Evaluator Based on Custom Graphs and Hierarchical GNNs

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Murphy, Emmet; Josipović, Lana
- Year / venue: 2024 / ICCAD
- DOI: 10.1145/3676536.3676788 · URL: https://doi.org/10.1145/3676536.3676788
- Metadata source: PDF first page (ACM reference format, ICCAD '24)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/hls_dse/RW0024_Murphy2024_Balor_ICCAD.pdf`
- SHA-256: `0101982c5232336648945d0eb5d95d42eac1757df1805a0312c7cc4cae645539`
- Source: /home/benyamin/Desktop/Library/Balor HLS Source Code EvaluatorBased on Custom Graphs and Hierarchical GNNs.pdf

## Code / dataset / artifact provenance
Code: https://github.com/emmet-murphy/balor ; dataset DB4HLS (public)

## 1. Research question
GNN-based HLS QoR estimators suffer from over-squashing/over-smoothing, software-oriented graph representations, and redundant computation, which increase error and inference cost for DSE.

## 2. Problem setting
Predicting post-HLS resource and timing QoR of directive-annotated C kernels directly from source code for use as a DSE evaluator.

## 3. Search space
NOT_APPLICABLE (estimator; dataset directives: loop unroll/parallelization, array partitioning, function inlining)

## 4. Evaluation method
Prediction error on held-out post-HLS results from DB4HLS (Vivado HLS 2018.2); no DSE run.

## 5. Benchmarks
25 MachSuite kernels from DB4HLS (36,296 design points)

## 6. Hardware
NOT_REPORTED (dataset target device not stated in paper); training on NVIDIA GTX 1080 GPUs

## 7. Toolchain
Vivado HLS 2018.2 (dataset); ROSE compiler; TransformerConv GNN

## 8. Metrics
Resource percentage estimation error, timing percentage estimation error, node count, number of weights, multiplications per inference, inference time

## 9. Baselines
GNN-DSE-like baseline re-implementation ('Information Has Location'); architecture ablations A-D

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: reduces resource estimation error by 41%, timing estimation error by 41%, and computational cost by 82% relative to a GNN-DSE-style baseline; graphs have 0.34x the node count on average.

## 11. Limitations
Estimates only post-HLS (not post-implementation) QoR; pipelining is not an explored directive in the dataset; single HLS tool version; no comparison to 'Information Is Implicit' approach; transfer to new kernels/conditions left as future work.

## 12. What the paper does NOT evaluate
Actual DSE outcome quality; post-route QoR; power; multi-kernel interactions; transfer learning to unseen kernels or devices.

## 13. Relationship to our Studies
- Direct (dimension = YES): none
- Partial (dimension = PARTIAL): S02 S04 S06 S10 S11 S21 S36 S37 S56 S71 S72 S73 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Estimator only |
| measured interactions | PARTIAL | Directive effects propagated to affected nodes; interactions learned, not measured |
| staged evaluation | NO | Not a staged flow |
| adaptive evidence acquisition | NO | No acquisition loop |
| cost/fidelity modeling | PARTIAL | Explicitly measures estimator inference cost; motivates as cheap alternative to HLS |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | NO | Post-HLS labels only |
| multi-benchmark transfer | PARTIAL | Single model across 25 MachSuite kernels; random split, no unseen-kernel test |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not estimated |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | PARTIAL | Array partition directives and local vs parameter arrays encoded |

## 14. Possible overlap
POTENTIAL OVERLAP (partial evidence) on: measured interactions; cost/fidelity modeling; multi-benchmark transfer; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; staged evaluation; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/emmet-murphy/balor ; dataset DB4HLS (public)

## Open questions / reviewer notes
Affiliations not captured by text extraction; authors per ACM reference line.
