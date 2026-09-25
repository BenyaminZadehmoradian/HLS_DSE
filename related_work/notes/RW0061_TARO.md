# RW0061 — TARO: Automatic Optimization for Free-Running Kernels in FPGA High-Level Synthesis

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Choi, Young-Kyu; Chi, Yuze; Lau, Jason; Cong, Jason
- Year / venue: 2023 / IEEE TCAD
- DOI: 10.1109/TCAD.2022.3216544 · URL: https://doi.org/10.1109/TCAD.2022.3216544
- Metadata source: PDF first page (IEEE TCAD vol. 42 no. 7, July 2023; DOI printed)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/other/RW0061_Choi2023_TARO_TCAD.pdf`
- SHA-256: `3b87c2d419d17fa9a5f974deb7c6d407f7c86f999703a9f90b38fad028165b55`
- Source: /home/benyamin/Desktop/Library/TARO: Automatic Optimization for Free-Running Kernels in FPGA High-Level Synthesis.pdf

## Code / dataset / artifact provenance
Code: https://github.com/UCLA-VAST/tapa/tree/taro

## 1. Research question
Streaming HLS designs carry loop-control and global task-management logic that free-running kernels could eliminate, but it is unclear when the transformation is safe and manual application to legacy code is laborious.

## 2. Problem setting
Automatic source-to-source free-running optimization of TAPA task-parallel streaming (dataflow) designs on an AMD FPGA.

## 3. Search space
NOT_APPLICABLE (transformation, not a search)

## 4. Evaluation method
Post place-and-route resource utilization and frequency (TAPA + AutoBridge + Vitis 2020.2) on Alveo U250; cycle counts.

## 5. Benchmarks
PolySA-style systolic arrays: matrix-vector, matrix-matrix, Needleman-Wunsch, CNN; vector add

## 6. Hardware
AMD/Xilinx Alveo U250

## 7. Toolchain
Vitis 2020.2; TAPA; AutoBridge; Clang/LLVM 8

## 8. Metrics
LUT and FF reduction, clock frequency, cycle count

## 9. Baselines
Same designs with flushable loops but without free-running optimization

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: average 15.9% LUT and 45.4% FF reduction (abstract: 16%/45%) on streaming systolic-array designs with no change in clock frequency; transformation takes under 1 s.

## 11. Limitations
Only tasks without external memory access can be free-running; benefit shrinks with complex datatypes and many DRAM-access tasks (e.g., LUT saving 27% to 11-12%); one unconditional blocking access per input stream.

## 12. What the paper does NOT evaluate
Performance-oriented DSE; power; designs beyond systolic arrays and vector add; interaction with pragma choices.

## 13. Relationship to our Studies
- Direct (dimension = YES): S59 S61 S78 S81
- Partial (dimension = PARTIAL): S07 S10 S11 S15 S65 S73 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Applied across all tasks of a dataflow design; not a DSE |
| measured interactions | NO | Not studied |
| staged evaluation | NOT_APPLICABLE | No search |
| adaptive evidence acquisition | NOT_APPLICABLE | No search |
| cost/fidelity modeling | NO | Not modeled |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Post-PnR resources and frequency reported |
| multi-benchmark transfer | PARTIAL | Four systolic-array benchmarks |
| decision/Pareto stability | NOT_APPLICABLE | No search |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | PARTIAL | Distinguishes stream tasks from DRAM-access tasks |

## 14. Possible overlap
PARTIAL OVERLAP on: physical implementation in the loop

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: measured interactions; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/UCLA-VAST/tapa/tree/taro

## Open questions / reviewer notes
Short brief-format TCAD paper (5 pages).
