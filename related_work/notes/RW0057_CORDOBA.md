# RW0057 — CORDOBA: Carbon-Efficient Optimization Framework for Computing Systems

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Carbon-aware design optimization with explicit Pareto/decision analysis; methodology for carbon objectives. Primary Studies: S20 S92 S43. Prior-art boundary: METHOD FOUNDATIONAL.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Elgamal, Mariam; Carmean, Doug; Ansari, Elnaz; Zed, Okay; Peri, Ramesh; Manne, Srilatha; Gupta, Udit; Wei, Gu-Yeon; Brooks, David; Hills, Gage; Wu, Carole-Jean
- Year / venue: 2025 / HPCA
- DOI: 10.1109/HPCA61900.2025.00098 · URL: https://doi.org/10.1109/HPCA61900.2025.00098
- Metadata source: PDF first page (IEEE HPCA 2025 header and DOI)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/energy_sustainability/RW0057_Elgamal2025_CORDOBA_HPCA.pdf`
- SHA-256: `4e44ebf0b94e552796820552c2115564a00f8bf6c3043b6dc747d7f9740cb69f`
- Source: /home/benyamin/Desktop/Sustainable_Design_Explorer/Papers/CORDOBA_Carbon-Efficient_Optimization_Framework_for_Computing_Systems_2025.pdf

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
How to optimize total (embodied + operational) carbon efficiency of computing systems in large design spaces while trading off power, performance, area, and handling carbon-data uncertainty.

## 2. Problem setting
Carbon optimization (as distinct from carbon accounting) for specialized hardware and real systems, using the total Carbon Delay Product (tCDP).

## 3. Search space
Accelerator configurations (number of MACs x activation SRAM size; 121 configurations), operational lifetime and carbon intensity; system case studies (CPU core count 8 vs 4; 3D logic-memory stacking vs 2D).

## 4. Evaluation method
Architecture simulation (accelerator simulator validated against FPGA board implementation with 2.98% performance error) + ACT-based carbon model; real-device profiling on Meta Quest 2 (Snapdragon XR2) for CPU case study; 7 nm P&R energy values for 3D case.

## 5. Benchmarks
15 AI/XR kernels (ResNet-18/50/152, GoogleNet, MobileNet-V2, eye tracking, depth estimation, denoising, super-resolution, etc.) grouped into 5 tasks

## 6. Hardware
Simulated ML accelerators; Meta Quest 2 (Qualcomm Snapdragon XR2, 7 nm) for real-system profiling

## 7. Toolchain
Custom accelerator simulator (PyTorch model input), ACT carbon model (updated), Android Debug Bridge + Simpleperf; versions NOT_REPORTED

## 8. Metrics
tCDP, total carbon (embodied + operational), CCI, EDP, delay, energy, area

## 9. Baselines
EDP-optimal and tC-optimal designs; conventional (2D) systems; 8-core provisioning

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: tCDP identifies distinct carbon-efficient optimal designs, eliminating up to 98% of the design space as sub-optimal for any operational lifetime despite carbon-parameter uncertainty; 8->4 cores improves tCDP by 1.25x; 3D logic-memory stacking improves tCDP up to 6.9x.

## 11. Limitations
Carbon estimates bounded by carbon-data uncertainty and simulator fidelity; power P(t) assumed fixed/known in uncertainty analysis; exhaustive sweep of a small (121-point) space taking hours.

## 12. What the paper does NOT evaluate
HLS pragma spaces; FPGA reconfiguration cost; multi-fidelity/adaptive search; post-route evaluation of explored designs; multi-kernel joint implementation on FPGA.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20 S43 S45 S85 S86 S92 S94
- Partial (dimension = PARTIAL): S04 S06 S07 S15 S21 S59 S61 S65 S72 S73 S78 S81

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Tasks composed of multiple kernels evaluated on one accelerator configuration; no joint multi-accelerator implementation. |
| measured interactions | NOT_REPORTED |  |
| staged evaluation | NO | Exhaustive sweep. |
| adaptive evidence acquisition | NO |  |
| cost/fidelity modeling | PARTIAL | Carbon-data uncertainty explicitly modeled; evaluation cost not modeled. |
| lifecycle/configuration cost | YES | Embodied vs operational carbon over hardware lifetime is central. |
| physical implementation in the loop | PARTIAL | 3D case uses energy values from prior 7 nm P&R; main DSE is simulation. |
| multi-benchmark transfer | NO |  |
| decision/Pareto stability | YES | Optimal design robustness across lifetime and carbon-intensity uncertainty analysed. |
| energy/power | YES | Energy/operational carbon from simulator. |
| CPU-FPGA interaction | NO |  |
| memory/data movement | PARTIAL | Activation SRAM size and 3D memory stacking explored. |

## 14. Possible overlap
PARTIAL OVERLAP on: lifecycle/configuration cost; decision/Pareto stability; energy/power

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; staged evaluation

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
none
