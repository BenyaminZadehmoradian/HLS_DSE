# RW0048 — HL-Pow: A Learning-Based Power Modeling Framework for High-Level Synthesis

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Learned power model driving a latency-power Pareto search over HLS directives. Primary Studies: S19. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** Key renamed from placeholder ENERGY1.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Lin, Zhe; Zhao, Jieru; Sinha, Sharad; Zhang, Wei
- Year / venue: 2020 / ASP-DAC
- DOI: 10.1109/ASP-DAC47756.2020.9045442 · URL: https://doi.org/10.1109/ASP-DAC47756.2020.9045442
- Metadata source: PDF first page (arXiv) + arXiv abs page (DOI, 'published as a conference paper in ASP-DAC 2020')

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/energy_sustainability/RW0048_Lin2020_HLPow_ASPDAC_arxiv.pdf`
- SHA-256: `c6b1774761ca9996b46cf261d7a34f29aa534845991a0194d32e04e4d61caa61`
- Source: https://arxiv.org/pdf/2009.00871

## Code / dataset / artifact provenance
NOT_REPORTED (no code link in paper)

## 1. Research question
Power of HLS designs is unknown until slow RTL implementation and measurement, hindering power-aware directive exploration.

## 2. Problem setting
Pre-RTL power prediction from HLS results and latency-power Pareto DSE over HLS directives for FPGA kernels.

## 3. Search space
HLS directives per application (loop unrolling, pipelining, array partitioning per Table II)

## 4. Evaluation method
Ground truth from on-board power measurement on ZCU102 (Power Advantage Tool) after Vivado implementation; DSE evaluated by ADRS vs exact Pareto set calibrated with measured power.

## 5. Benchmarks
22 PolyBench applications (test on 7 unseen: atax, bicg, fdtd-2d, gemm, gramschmidt, jacobi-2d, mvt); up to 11,326 design points

## 6. Hardware
Xilinx UltraScale+ ZCU102

## 7. Toolchain
Vivado HLS / Vivado Design Suite 2018.2; scikit-learn, XGBoost, Keras

## 8. Metrics
Power prediction MAE (% and mW); ADRS; fraction of design points sampled

## 9. Baselines
Compared ML model families against each other; DSE compared vs exact Pareto set (no external DSE baseline reported)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: power model 'only 4.67% (24.02 mW) away from onboard power measurement'; DSE reaches a close Pareto approximation (average ADRS 2.35% / 1.84%) 'while only requiring running HLS flow for 20%' (resp. 40%) of design points.

## 11. Limitations
Model trained per device/tool version (transfer to other FPGAs not shown); single-kernel designs; power model needs RTL implementation data for training; energy (power x latency) not optimized directly.

## 12. What the paper does NOT evaluate
Energy per task, multi-kernel/system interactions, CPU-FPGA transfer power, cross-device transfer, carbon/lifecycle.

## 13. Relationship to our Studies
- Direct (dimension = YES): S05 S10 S11 S19 S20 S23 S32 S33 S34 S59 S61 S78 S81 S88 S90
- Partial (dimension = PARTIAL): S04 S06 S21 S72 S73

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Per-application designs. |
| measured interactions | NO | Not addressed. |
| staged evaluation | YES | HLS runs + learned power model replace RTL implementation/measurement for most points. |
| adaptive evidence acquisition | YES | SDR-guided sampling selects which design points to run through HLS. |
| cost/fidelity modeling | PARTIAL | Fraction of HLS runs (20%/40%) used as a budget; no explicit cost model. |
| lifecycle/configuration cost | NO | Not addressed. |
| physical implementation in the loop | YES | Training/ground-truth power from implemented designs measured on board. |
| multi-benchmark transfer | YES | Power model trained on 15 apps and tested on 7 unseen PolyBench apps. |
| decision/Pareto stability | NO | Not studied. |
| energy/power | YES | Power is the modeled objective with latency-power Pareto DSE. |
| CPU-FPGA interaction | NO | Not addressed. |
| memory/data movement | PARTIAL | Features include BRAM usage and switching activity; array partitioning in directive space. |

## 14. Possible overlap
PARTIAL OVERLAP on: staged evaluation; adaptive evidence acquisition; physical implementation in the loop; multi-benchmark transfer; energy/power

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; measured interactions; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no code link in paper)

## Open questions / reviewer notes
ENERGY slot justification: directly combines power prediction with HLS directive DSE (latency-power Pareto) validated by on-board measurement; predecessor of PowerGear (already held) by the same group, so it adds the DSE-with-power-in-the-loop angle rather than duplicating it. Not on the excluded list.
