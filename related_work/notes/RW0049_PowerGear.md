# RW0049 — PowerGear: Early-Stage Power Estimation in FPGA HLS via Heterogeneous Edge-Centric GNNs

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Lin, Zhe; Yuan, Zike; Zhao, Jieru; Zhang, Wei; Wang, Hui; Tian, Yonghong
- Year / venue: 2022 / DATE
- DOI: 10.23919/DATE54114.2022.9774682 · URL: https://doi.org/10.23919/DATE54114.2022.9774682
- Metadata source: PDF first page ('Preprint of the paper to be published in DATE 2022') + IEEE Xplore landing page (doc 9774682) for DOI

## PDF provenance
- Status: `LOCAL_EXISTING` (preprint)
- Canonical path: `related_work/papers/energy_sustainability/RW0049_Lin2022_PowerGear_DATE_preprint.pdf`
- SHA-256: `742fb84149125e530eae97931e43d76540169709ad3f829b739071e041ca651a`
- Source: /home/benyamin/Desktop/Library/PowerGear Early-Stage Power Estimation in FPGA HLS via Heterogeneous Edge-Centric GNNs.pdf

## Code / dataset / artifact provenance
Code: https://github.com/zlinaf/PowerGear (found via web search; not stated in PDF)

## 1. Research question
Accurate FPGA power estimation normally requires implementation and gate-level simulation; prior HLS-level power models ignore interconnects and switching activity and do not predict dynamic power well.

## 2. Problem setting
Post-HLS (pre-RTL-implementation) estimation of total and dynamic on-board power for unseen HLS designs, and use of the model in latency-power DSE.

## 3. Search space
DSE case study over loop pipelining, loop unrolling and buffer partitioning configurations of each dataset

## 4. Evaluation method
Leave-one-application-out prediction error vs on-board power measurement (Power Advantage Tool) of implemented designs at 100 MHz; DSE quality via ADRS vs exact Pareto set.

## 5. Benchmarks
Nine PolyBench-derived applications with pragma variants plus synthetic datasets

## 6. Hardware
Xilinx UltraScale+ ZCU102 board

## 7. Toolchain
Vivado and Vivado HLS 2018.2

## 8. Metrics
Total and dynamic power estimation error, runtime speedup vs Vivado power estimator, ADRS

## 9. Baselines
Vivado power estimator (calibrated), HL-Pow, mainstream GNNs (e.g., GCN/GAT variants), HEC-GNN ablation variants

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: total and dynamic power errors of 3.60% and 8.81% on unseen designs vs on-board measurement, 4x faster than Vivado power estimator; PowerGear-assisted DSE yields 39.2-52% and 6.9-11.2% ADRS gains over Vivado- and HL-Pow-based DSE.

## 11. Limitations
Requires running HLS for each design (post-HLS inputs); single board at fixed 100 MHz; small application set; static power partially dependent on power gating.

## 12. What the paper does NOT evaluate
Pre-HLS use; timing/Fmax effects; multi-kernel/system-level power; other devices; host power.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S10 S11 S19 S20 S21 S59 S61 S72 S78 S81 S90
- Partial (dimension = PARTIAL): S05 S23 S32 S33 S34 S43 S45 S73 S88 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Single-application designs |
| measured interactions | NO | Not studied |
| staged evaluation | PARTIAL | HLS run then GNN power prediction replaces implementation+measurement |
| adaptive evidence acquisition | PARTIAL | DSE case study iteratively samples likely Pareto points |
| cost/fidelity modeling | YES | Cheap post-HLS model substitutes for implementation, simulation and measurement; runtime compared |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Labels from implemented bitstreams measured on board |
| multi-benchmark transfer | YES | Leave-one-application-out transfer |
| decision/Pareto stability | PARTIAL | ADRS against exact latency-power Pareto front |
| energy/power | YES | Total and dynamic power predicted and optimized |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | PARTIAL | Buffer nodes with memory utilization in graph |

## 14. Possible overlap
PARTIAL OVERLAP on: cost/fidelity modeling; physical implementation in the loop; multi-benchmark transfer; energy/power

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; measured interactions; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/zlinaf/PowerGear (found via web search; not stated in PDF)

## Open questions / reviewer notes
Local PDF is the author preprint of the DATE 2022 paper.
