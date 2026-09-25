# RW0046 — Power Consumption Model for Partial and Dynamic Reconfiguration

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Bonamy, Robin; Chillet, Daniel; Bilavarn, Sebastien; Sentieys, Olivier
- Year / venue: 2012 / ReConFig
- DOI: 10.1109/ReConFig.2012.6416772 · URL: https://doi.org/10.1109/ReConFig.2012.6416772
- Metadata source: PDF (title/authors, IEEE 2012 ISBN 978-1-4673-2921-7) + web search (ReConFig 2012, Cancun; DOI from search result, HAL hal-00741611)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/energy_sustainability/RW0046_Bonamy2012_Bonamy12DPR_ReConFig.pdf`
- SHA-256: `e29c6b640f4d97a3c18071a0995f908113b6b782dc40550c60a04ceb61ef3810`
- Source: /home/benyamin/Desktop/pragma_mach/reference/papers/bonamy2012_dpr_power_model.pdf

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Lack of accurate power/energy models of FPGA dynamic partial reconfiguration (DPR) to decide between static hardware, DPR hardware, or software tasks.

## 2. Problem setting
Measurement-based characterization and modeling of DPR power on a Xilinx Virtex-5 using ICAP.

## 3. Search space
NOT_APPLICABLE

## 4. Evaluation method
On-board current measurement (high-precision amplifier + oscilloscope) on ML550

## 5. Benchmarks
Reconfiguration between hardware tasks in one partially reconfigurable region (4 configuration cases)

## 6. Hardware
Xilinx ML550 board, Virtex-5 XC5VLX50T, MicroBlaze + xps_hw_icap

## 7. Toolchain
Xilinx ISE 12.1

## 8. Metrics
Power profile, reconfiguration energy (mJ), model energy error and power error std. dev.

## 9. Baselines
Measured power

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: fine-grained model estimates DPR energy with <6% error (1.8% average); coarse/medium models give ~8-9% average error but coarse model up to 77% error when idle power differs; bitstream writing adds ~45 mW (>10% of FPGA power).

## 11. Limitations
Single old device/board and CompactFlash-based slow controller; small set of configurations.

## 12. What the paper does NOT evaluate
HLS design space; modern devices/high-throughput ICAP/PCAP; system-level DSE.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S19 S20 S21 S59 S61 S72 S78 S81 S85 S86 S94
- Partial (dimension = PARTIAL): S73 S83 S84

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE |  |
| measured interactions | NOT_APPLICABLE |  |
| staged evaluation | NOT_APPLICABLE |  |
| adaptive evidence acquisition | NOT_APPLICABLE |  |
| cost/fidelity modeling | YES | Three model granularities with accuracy/complexity trade-off. |
| lifecycle/configuration cost | YES | Reconfiguration energy/time is the subject. |
| physical implementation in the loop | YES | Real bitstreams on hardware. |
| multi-benchmark transfer | NOT_APPLICABLE |  |
| decision/Pareto stability | NOT_APPLICABLE |  |
| energy/power | YES | Measured. |
| CPU-FPGA interaction | PARTIAL | MicroBlaze-driven reconfiguration. |
| memory/data movement | PARTIAL | Bitstream transfer from CompactFlash to ICAP analyzed. |

## 14. Possible overlap
PARTIAL OVERLAP on: cost/fidelity modeling; lifecycle/configuration cost; physical implementation in the loop; energy/power

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Title on PDF: 'Power Consumption Model for Partial and Dynamic Reconfiguration'; IEEE/ResearchGate list it as 'Power Consumption Model for Partial Dynamic Reconfiguration'. DOI taken from web search, not printed in PDF. Distinct from the later journal paper 'Power consumption models for the use of dynamic and partial reconfiguration' (Microprocessors and Microsystems, 2014).
