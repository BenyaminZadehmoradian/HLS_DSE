# RW0006 — Correlated Multi-objective Multi-fidelity Optimization for HLS Directives Design

> **Relevance (2026-09-25 correction audit): CORE** — Jointly selects HLS directive configuration and fidelity with a cost-penalized acquisition (full-text review); boundary of the evidence-selection question. Primary Studies: S04 S05 S07 S21 S23. Prior-art boundary: PRIOR ART.
> **Identity:** DATE 2021 DOI used; TODAES 2022 extension (10.1145/3503540) with the same title is a different paper.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Sun, Qi; Chen, Tinghuan; Liu, Siting; Miao, Jin; Chen, Jianli; Yu, Hao; Yu, Bei
- Year / venue: 2021 / DATE
- DOI: 10.23919/DATE51398.2021.9474241 · URL: https://doi.org/10.23919/DATE51398.2021.9474241
- Metadata source: PDF first page (author copy) + OpenAlex/IEEE Xplore (pp. 46-51)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (accepted)
- Canonical path: `related_work/papers/core/RW0006_Sun2021_CMMFO_DATE_accepted.pdf`
- SHA-256: `6de6884b3a23a7cd142e5a41ad52087e9ad96295d555b098f0320bd46068bb45`
- Source: https://www.cse.cuhk.edu.hk/~byu/papers/C114-DATE2021-MultiFidelity.pdf

## Code / dataset / artifact provenance
NOT_REPORTED (no code/data link in paper; benchmarks public: MachSuite https://breagen.github.io/MachSuite/, iSmartDNN https://github.com/onioncc/iSmartDNN)

## 1. Research question
Finding Pareto-optimal HLS directive configurations for power, delay and LUT area when evaluations come from three flow stages (HLS, logic synthesis, implementation) with different accuracy and cost, and objectives are correlated.

## 2. Problem setting
Single-kernel, multi-objective HLS directive DSE on Xilinx FPGA with three fidelities (post-HLS, post-synth, post-impl reports).

## 3. Search space
HLS directives: loop unrolling, loop pipelining with II, array partitioning (plus inline), defined per benchmark in YAML; pruned by tree-based array/loop compatibility (e.g., SORT_RADIX from >3.8e12 to ~20000 configs).

## 4. Evaluation method
Real Xilinx tool runs up to the selected fidelity (Vivado HLS, logic synthesis, implementation); final quality measured by ADRS against real Pareto set from post-implementation data; illegal (failed placement/routing) designs penalized.

## 5. Benchmarks
MachSuite GEMM, SORT_RADIX, SPMV_ELLPACK, SPMV_CRS, STENCIL3D; iSmart2 (DNN object detection)

## 6. Hardware
Xilinx Virtex-7 VC707

## 7. Toolchain
Xilinx Vivado HLS 2018.2 (and Vivado synthesis/implementation; version for later stages not separately stated)

## 8. Metrics
Normalized ADRS, standard deviation of ADRS over 10 runs, normalized overall running time; objectives: power, delay (latency x clock period), LUT utilization

## 9. Baselines
FPL18 (Lo & Chow linear multi-fidelity BO), ANN, Boosting tree (BT/XGBoost), DAC19 (Liu, Lau, Schafer predictive-model DSE)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: average normalized ADRS 0.39 vs 0.51 (FPL18), 1.00 (ANN), 0.96 (BT), 1.05 (DAC19), with lowest ADRS std-dev (0.16) and lowest average normalized running time (0.54); 'can approximate the Pareto-frontier of the directive design space in a shorter time with much better performance and good stability'.

## 11. Limitations
Only six benchmarks on one device and one tool version; small budgets (8 initial samples, 40 iterations); per-benchmark models (no transfer); GP scalability to larger spaces not studied; tree pruning heuristic tailored to unroll/partition compatibility; PDF text layer partially garbled in pages 3-4 (content read where legible).

## 12. What the paper does NOT evaluate
Multi-kernel/system-level joint evaluation, CPU-FPGA interaction, on-board measurement, cross-benchmark transfer, reconfiguration/lifecycle cost, stability of chosen decision beyond ADRS std-dev.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S05 S06 S19 S20 S21 S23 S32 S33 S34 S59 S61 S72 S78 S81 S88
- Partial (dimension = PARTIAL): S02 S36 S37 S43 S45 S56 S71 S73 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Each benchmark optimized independently as a single design. |
| measured interactions | PARTIAL | Models correlations among objectives and prunes incompatible loop-unroll/array-partition combinations; no cross-kernel interaction. |
| staged evaluation | YES | Three fidelities (HLS, Synth, Impl); each candidate run only up to chosen fidelity h. |
| adaptive evidence acquisition | YES | Per iteration selects (configuration, fidelity) pair maximizing penalized EIPV. |
| cost/fidelity modeling | YES | Non-linear multi-fidelity GP plus acquisition penalty proportional to T_impl/T_i stage runtime. |
| lifecycle/configuration cost | NO | Not considered. |
| physical implementation in the loop | YES | Implementation-stage (place-and-route) reports are the highest fidelity in the loop; illegal P&R designs penalized. |
| multi-benchmark transfer | NO | Models built per benchmark. |
| decision/Pareto stability | PARTIAL | Reports std-dev of ADRS over 10 repeated runs. |
| energy/power | YES | Power is one of three objectives (tool-reported). |
| CPU-FPGA interaction | NO | Not considered. |
| memory/data movement | PARTIAL | Array partitioning directives only; no data-movement modeling. |

## 14. Possible overlap
PARTIAL OVERLAP on: staged evaluation; adaptive evidence acquisition; cost/fidelity modeling; physical implementation in the loop; energy/power

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no code/data link in paper; benchmarks public: MachSuite https://breagen.github.io/MachSuite/, iSmartDNN https://github.com/onioncc/iSmartDNN)

## Open questions / reviewer notes
Hint title matches. DOI 10.1145/3503540 (ACM TODAES 2022, same title) is a journal extension by the same group; some indexes (e.g., Semantic Scholar) conflate it with the DATE paper. Downloaded PDF is the author copy from Bei Yu's CUHK page (camera-ready formatting, no DOI stamp); marked 'accepted'.
