# RW0058 — HIPPO: A Hierarchy-Preserving and Noise-Tolerant Pre-HLS Power Modeling Framework for FPGA

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Lin, Zefan; Peng, Zedong; Gao, Mingzhe; Zhao, Jieru; Lin, Zhe
- Year / venue: 2025 / ICCAD
- DOI: 10.1109/ICCAD66269.2025.11240868 · URL: https://doi.org/10.1109/ICCAD66269.2025.11240868
- Metadata source: PDF first page (IEEE Xplore header with DOI, ICCAD 2025)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/energy_sustainability/RW0058_Lin2025_HIPPO_ICCAD.pdf`
- SHA-256: `7a22676cbf69916eb4950c0005855409f4694cee38165099d5c50c42e00038f9`
- Source: /home/benyamin/Desktop/Library/HIPPO A Hierarchy-Preserving and Noise-Tolerant Pre-HLS Power Modeling Framework for FPGA.pdf

## Code / dataset / artifact provenance
NOT_REPORTED (no code URL in paper)

## 1. Research question
FPGA power estimation for HLS designs requires a long EDA chain (HLS, implementation, measurement), and prior learned models still depend on HLS outputs, making power-aware DSE over many pragma configurations slow; on-board measurements are also noisy.

## 2. Problem setting
Pre-HLS prediction of dynamic and total on-board power of pragma-annotated C/C++ kernels on an AMD ZCU102 board, without invoking any EDA tool.

## 3. Search space
NOT_APPLICABLE (estimator; dataset pragmas: pipelining, unrolling, array partitioning, loop flattening)

## 4. Evaluation method
Prediction error against on-board power measurements (Power Advantage Tool) of implemented bitstreams; 80/10/10 split.

## 5. Benchmarks
PolyBench and MachSuite applications with pragma variants (7,090 inner-loop and 9,696 application-level design points, including randomly merged larger designs)

## 6. Hardware
AMD/Xilinx ZCU102 (on-board measurement)

## 7. Toolchain
Vitis HLS 2022.2, Vivado 2022.2 (label generation); Clang/LLVM; ProGraML; Zynq UltraScale+ Power Advantage Tool

## 8. Metrics
NMAE, NRMSE, R2 for dynamic and total power

## 9. Baselines
HL-Pow, PowerGear (post-HLS); GNN variants; full-coarsening ablation; no-operation-feature ablation

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: average errors of 8.89% (dynamic) and 6.31% (total) for nested loops and 9.86% (dynamic) and 3.41% (total) for single/inner loops; comparable to post-HLS HL-Pow/PowerGear with at most 0.45% discrepancy vs PowerGear.

## 11. Limitations
Single board/device; operation models require calibration on hardware; noise threshold fixed at 10 mW; not demonstrated inside an actual DSE loop.

## 12. What the paper does NOT evaluate
Use for DSE/Pareto search; latency/resource prediction; multi-kernel system power or host interaction; transfer to other devices.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S19 S20 S21 S59 S61 S72 S78 S81
- Partial (dimension = PARTIAL): S02 S10 S11 S32 S34 S36 S37 S56 S73 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Estimator |
| measured interactions | PARTIAL | Hierarchical composition of inner-loop power into nested-loop prediction |
| staged evaluation | PARTIAL | Hierarchical (operation->inner loop->nested loop) modeling, not a staged DSE |
| adaptive evidence acquisition | NO | No acquisition loop |
| cost/fidelity modeling | YES | Pre-HLS model positioned as a cheap substitute for full EDA flow + measurement; measurement noise modeled |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Labels from placed-and-routed bitstreams measured on board |
| multi-benchmark transfer | PARTIAL | Many PolyBench/MachSuite apps; random split |
| decision/Pareto stability | NO | Not studied |
| energy/power | YES | Dynamic and total power are the prediction targets |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | PARTIAL | Memory nodes/partitioning and memory access switching modeled for power |

## 14. Possible overlap
PARTIAL OVERLAP on: cost/fidelity modeling; physical implementation in the loop; energy/power

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no code URL in paper)

## Open questions / reviewer notes
Affiliations: Sun Yat-sen University and Shanghai Jiao Tong University.
