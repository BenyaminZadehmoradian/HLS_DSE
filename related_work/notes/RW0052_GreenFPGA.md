# RW0052 — GreenFPGA: Evaluating FPGAs as Environmentally Sustainable Computing Solutions

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Choppali Sudarshan, Chetan; Arora, Aman; Chhabria, Vidya A.
- Year / venue: 2024 / DAC
- DOI: 10.1145/3649329.3657343 · URL: https://doi.org/10.1145/3649329.3657343
- Metadata source: PDF first page (ACM reference format DAC '24; arXiv:2311.12396v2 stamp)

## PDF provenance
- Status: `LOCAL_EXISTING` (arxiv)
- Canonical path: `related_work/papers/energy_sustainability/RW0052_ChoppaliSudarshan2024_GreenFPGA_DAC_arxiv.pdf`
- SHA-256: `4eecc1572a26a62a9af8ec87674b2537ad96b56092d15ab6bcb53ab14092274a`
- Source: /home/benyamin/Desktop/Sustainable_Design_Explorer/Papers/GreenFPGA_Evaluating_FPGAs_as_Environmentally_Sustainable_Computing_Solutions_2024.pdf

## Code / dataset / artifact provenance
Open source: https://github.com/ASU-VDA-Lab/GreenFPGA

## 1. Research question
When is an FPGA, thanks to reconfigurability across applications, a lower-carbon acceleration platform than iso-performance ASICs over the full lifecycle?

## 2. Problem setting
Lifecycle carbon footprint (design, manufacturing, packaging, reconfiguration, application development, operation, disposal/recycling) modeling of FPGAs vs ASICs.

## 3. Search space
Scenario parameters: number of applications, application lifetime, volume, domain (DNN, Crypto, ImgProc)

## 4. Evaluation method
Analytical model with industry/government report data and iso-performance FPGA/ASIC area/power from literature; no measurements.

## 5. Benchmarks
Three domains at iso-performance (DNN, Crypto, ImgProc) from prior study [12]

## 6. Hardware
Modeled FPGA testcases based on Intel Agilex 7 and Stratix 10 (TDP, area, node) vs ASICs

## 7. Toolchain
GreenFPGA (Python tool); versions NOT_REPORTED

## 8. Metrics
Total carbon footprint (CFP) and its embodied/operational components

## 9. Baselines
Iso-performance ASICs

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: FPGAs have lower CFP than ASICs for application lifetimes below ~1.6 years, when reused across more than ~5 applications, or for volumes under ~2 million (domain dependent); for ImgProc, ASICs always greener.

## 11. Limitations
Relies on public reports and literature iso-performance ratios; no measurement validation; coarse application-development and configuration models.

## 12. What the paper does NOT evaluate
Per-design HLS configuration choices; measured reconfiguration energy; DSE; partial reconfiguration.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20 S85 S86 S94
- Partial (dimension = PARTIAL): S43 S45 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE |  |
| measured interactions | NOT_APPLICABLE |  |
| staged evaluation | NOT_APPLICABLE |  |
| adaptive evidence acquisition | NOT_APPLICABLE |  |
| cost/fidelity modeling | NO |  |
| lifecycle/configuration cost | YES | Full lifecycle CFP including reconfiguration/app-development/configuration time. |
| physical implementation in the loop | NO | Back-end synthesis/P&R time only as a carbon cost term. |
| multi-benchmark transfer | NOT_APPLICABLE |  |
| decision/Pareto stability | PARTIAL | Crossover points FPGA vs ASIC across lifetime/volume/app count. |
| energy/power | YES | Operational energy from TDP and duty cycle. |
| CPU-FPGA interaction | NO |  |
| memory/data movement | NO |  |

## 14. Possible overlap
PARTIAL OVERLAP on: lifecycle/configuration cost; energy/power

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Open source: https://github.com/ASU-VDA-Lab/GreenFPGA

## Open questions / reviewer notes
Local file is arXiv 2311.12396v2 (9 Jul 2024) carrying the DAC '24 reference block.
