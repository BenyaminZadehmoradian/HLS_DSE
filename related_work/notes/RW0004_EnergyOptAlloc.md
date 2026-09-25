# RW0004 — Fast Energy-Optimal Multi-Kernel DNN-like Application Allocation on Multi-FPGA Platforms

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Energy-optimal joint multi-kernel allocation; foundation for packing and energy trade-offs. Primary Studies: S95 S19. Prior-art boundary: RELEVANT BUT DIFFERENT.
> **Identity:** Title on PDF "Multi-Kernel DNN-like Application Allocation"; Crossref "Multikernel DNN-Like".

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Shan, Junnan; Lazarescu, Mihai T.; Cortadella, Jordi; Lavagno, Luciano; Casu, Mario R.
- Year / venue: 2022 / IEEE TCAD
- DOI: 10.1109/TCAD.2021.3076958 · URL: https://doi.org/10.1109/TCAD.2021.3076958
- Metadata source: PDF first page (UPCommons accepted manuscript) + Crossref (vol. 41, no. 4, pp. 1186-1190, Apr. 2022)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (accepted)
- Canonical path: `related_work/papers/concurrent_multikernel/RW0004_Shan2022_EnergyOptAlloc_TCAD_accepted.pdf`
- SHA-256: `e52ff84e7a15b13b028efa3fa935bdadc265b0be0a3af80d57d8168509d9ebb8`
- Source: https://upcommons.upc.edu/bitstreams/b3350461-2a18-4055-95c8-b9c2249d7168/download

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Finding minimum-power allocations of multi-kernel pipelined DNN-like applications on multi-FPGA platforms for a given throughput (II) constraint, fast enough to reprogram FPGAs at runtime as workloads change.

## 2. Problem setting
Linear pipeline of kernels with CU replication and per-FPGA frequency scaling on AWS F1 (8 FPGAs, PCIe host), minimizing total power subject to II <= II_max.

## 3. Search space
CUs per kernel per FPGA (n_k,f), per-FPGA clock frequency, number of active FPGAs; per-CU implementations pre-characterized.

## 4. Evaluation method
Kernel execution time measured on AWS F1; power estimated from datasheets and Xilinx power analysis tools (no power measurement on F1); solver comparison via model.

## 5. Benchmarks
AlexNet (ALEX-16, ALEX-32), VGG-16, Transformer (TRANSFORMER-16, 1 encoder/1 decoder, 4 heads)

## 6. Hardware
AWS F1 (8x Xilinx UltraScale+); optimizer on Intel Core i7-6900K

## 7. Toolchain
Xilinx SDAccel; MINLP solver from prior work; Xilinx power analysis tools

## 8. Metrics
Minimum power vs II, number of FPGAs used, optimization time

## 9. Baselines
MINLP method from prior work [Shan et al., TCAS-II 2020]

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: both heuristics obtain results comparable to MINLP when it finds the optimum and better results when MINLP cannot within bounded time; H2 is 'thousands of times faster than the exact algorithm' (run times ~5 s).

## 11. Limitations
Reconfiguration energy ignored (assumes infrequent reconfiguration, e.g., hourly); power estimated not measured; linear pipelines; all data via host (no FPGA-to-FPGA); H1 can miss best solution by ~12% on VGG-16; MINLP had to be stopped early (24-30 h) on large problems.

## 12. What the paper does NOT evaluate
Reconfiguration time/energy cost, on-board power measurement, intra-kernel HLS design choices, post-route interaction effects between co-located CUs.

## 13. Relationship to our Studies
- Direct (dimension = YES): S07 S15 S19 S20 S65 S73
- Partial (dimension = PARTIAL): S02 S04 S06 S21 S36 S37 S56 S59 S61 S72 S78 S81 S83 S84 S85 S86 S94

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | All kernels' CU counts, placements, and FPGA frequencies optimized jointly. |
| measured interactions | PARTIAL | Model couples kernels via shared FPGA resources, frequency and data replication; no measured non-additive interactions. |
| staged evaluation | NO | Single model-based evaluation; heuristics reduce search space. |
| adaptive evidence acquisition | NO | Not applicable. |
| cost/fidelity modeling | PARTIAL | Optimizer runtime compared across methods; fidelity not modeled. |
| lifecycle/configuration cost | PARTIAL | Runtime FPGA reprogramming to track workloads is the motivation, but reconfiguration energy/time explicitly ignored. |
| physical implementation in the loop | PARTIAL | Kernels profiled on AWS F1 from SDAccel builds; allocations evaluated via model. |
| multi-benchmark transfer | NO | Not studied. |
| decision/Pareto stability | NO | Not evaluated. |
| energy/power | YES | Objective is total power (static+dynamic), estimated. |
| CPU-FPGA interaction | PARTIAL | Host-FPGA PCIe transfer times included in II model. |
| memory/data movement | YES | DDR bandwidth, PCIe transfer time and input data replication modeled. |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; energy/power; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; staged evaluation; decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Published title uses 'Multikernel DNN-Like' (Crossref); PDF title is 'Multi-Kernel DNN-like'. Short (5-page) TCAD paper. Builds on Shan et al. TCAS-II 2020 ('Power-optimal mapping of CNN applications to cloud-based multi-FPGA platforms') and DAC 2019.
