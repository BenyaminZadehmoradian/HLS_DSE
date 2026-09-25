# RW0035 — Pattern-Guided Design Space Exploration for FPGA Accelerator Design

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Zhang, Jialiang; Yan, Weiman; Zou, Yuelin
- Year / venue: 2026 / ICECCME (arXiv preprint)
- DOI: 10.48550/arXiv.2607.15068 · URL: https://arxiv.org/abs/2607.15068
- Metadata source: arXiv PDF first page (header: Proc. ICECCME 2026, 15-17 Oct 2026, Bali) + arXiv abs page

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/hls_dse/RW0035_Zhang2026_PatternDSE_ICECCME_arxiv.pdf`
- SHA-256: `bacd9ce5f87e9e98bcced49313ff282a76cd67f54605a1c37e1489a5ea1fac9a`
- Source: https://arxiv.org/pdf/2607.15068

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
HLS schedule decisions (pipelining, unrolling, tiling, reordering, buffering) create a combinatorial space; generic search wastes synthesis budget on structurally unproductive schedules.

## 2. Problem setting
Front-end pruning of schedule spaces for single numerical kernels written in Allo before Vitis HLS synthesis.

## 3. Search space
Allo schedule primitives: pipeline, unroll factors, loop reorder, array partition (tiling/buffering discussed but limited), bounded per pattern template

## 4. Evaluation method
Vitis HLS synthesis (latency, II, resources) of selected candidates; validity requires passing LLVM execution and codegen

## 5. Benchmarks
vecadd, axpy, dot, matvec, gemm, jacobi2d

## 6. Hardware
NOT_REPORTED (same target part and clock within an experiment, unspecified)

## 7. Toolchain
Allo; LLVM backend; Vitis HLS (version NOT_REPORTED)

## 8. Metrics
Number of HLS-evaluated candidates, search-space reduction, best valid HLS latency

## 9. Baselines
Exhaustive-lite (bounded generic template enumeration)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: reduces HLS-evaluated candidates from 140 to 29 (4.83x overall, up to 12.0x per kernel) while recovering the same best valid Vitis HLS latency as the exhaustive-lite baseline for all six kernels.

## 11. Limitations
Stated: manually defined, small pattern library; simple estimator; templates focus on loop scheduling and bounded unrolling; only exhaustive-lite baseline (no BO/GA/prior DSE tools). Also: tiny kernels, HLS-estimate evaluation only, pattern assigned manually per kernel.

## 12. What the paper does NOT evaluate
Resource/latency Pareto trade-offs, post-implementation or on-board results, power, multi-kernel systems, comparisons with established DSE tools.

## 13. Relationship to our Studies
- Direct (dimension = YES): S32 S34 S88
- Partial (dimension = PARTIAL): S02 S04 S06 S21 S36 S37 S56 S72 S73

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Single kernels only. |
| measured interactions | PARTIAL | Knob interactions discussed qualitatively; not measured. |
| staged evaluation | YES | LLVM execution check -> HLS C codegen check -> estimator ranking -> Vitis HLS on top-k. |
| adaptive evidence acquisition | NO | Static template instantiation and ranking; feedback calibration is future work. |
| cost/fidelity modeling | PARTIAL | Cheap estimator ranks before expensive synthesis; cost counted as number of HLS runs. |
| lifecycle/configuration cost | NO | Not considered. |
| physical implementation in the loop | NO | HLS synthesis only. |
| multi-benchmark transfer | NO | Pattern templates hand-assigned; no transfer study. |
| decision/Pareto stability | NO | Not studied. |
| energy/power | NO | Not reported. |
| CPU-FPGA interaction | NO | Not considered. |
| memory/data movement | PARTIAL | Array partitioning knobs; buffering/memory hierarchy listed as future work. |

## 14. Possible overlap
PARTIAL OVERLAP on: staged evaluation

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Identified by hint 'pattern-guided HLS DSE'; this is the only paper found titled/pitched as pattern-guided DSE and self-names 'PatternDSE'. Very recent (arXiv July 2026), 6-page conference paper; not peer-review status verified beyond the ICECCME 2026 header. Related but different: knowledge/code-similarity-based HLS DSE works (e.g., the knowledge-based approach of Ferretti et al. cited by CollectiveHLS) are not 'pattern-guided' in this sense.
