# RW0047 — Accurate Measurement of Power Consumption Overhead During FPGA Dynamic Partial Reconfiguration

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Nafkha, Amor; Louet, Yves
- Year / venue: 2016 / ISWCS
- DOI: NOT_REPORTED · URL: https://ieeexplore.ieee.org/document/7600972/
- Metadata source: PDF (arXiv:1701.08849v1 stamp) + web search (13th ISWCS 2016, Poznan; IEEE Xplore 7600972)

## PDF provenance
- Status: `LOCAL_EXISTING` (arxiv)
- Canonical path: `related_work/papers/energy_sustainability/RW0047_Nafkha2016_Nafkha17DPR_ISWCS_arxiv.pdf`
- SHA-256: `9dfeed771286b53c1d675d641fec93feecfd13935601f3e7a0b7a5baf6eec0d0`
- Source: /home/benyamin/Desktop/pragma_mach/reference/papers/nafkha2017_dpr_power_measurement.pdf

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Quantify time and power overhead of FPGA DPR with adequate temporal resolution.

## 2. Problem setting
DPR of a variable digital filter (APT-VDF) reconfigurable region on Virtex-5 for SDR use.

## 3. Search space
NOT_APPLICABLE

## 4. Evaluation method
On-board measurement; post-place-and-route resource figures; XPower estimates for static/dynamic power

## 5. Benchmarks
APT-VDF filter (highpass/bandstop configurations), order-21 prototype

## 6. Hardware
Xilinx ML550, Virtex-5 XC5VLX50T

## 7. Toolchain
Xilinx ISE/XPS/PlanAhead 14.7, ModelSim, XPower Analyzer

## 8. Metrics
Reconfiguration time, bitstream size, core power overhead

## 9. Baselines
Full JTAG and partial JTAG reconfiguration

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: partial reconfiguration of a 94.5 KB bitstream via ICAP32 DMA takes ~324 us (vs 208.9 ms partial JTAG, 3.80 s full JTAG); DPR power overhead does not exceed ~160 mW.

## 11. Limitations
Single design/device; oscilloscope-based short measurement; no energy model.

## 12. What the paper does NOT evaluate
HLS DSE, modern devices, multi-accelerator systems.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20 S59 S61 S78 S81 S85 S86 S94
- Partial (dimension = PARTIAL): S73 S83 S84

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE |  |
| measured interactions | NOT_APPLICABLE |  |
| staged evaluation | NOT_APPLICABLE |  |
| adaptive evidence acquisition | NOT_APPLICABLE |  |
| cost/fidelity modeling | NO |  |
| lifecycle/configuration cost | YES | Reconfiguration time/power overhead measured. |
| physical implementation in the loop | YES | Real partial bitstreams on hardware. |
| multi-benchmark transfer | NOT_APPLICABLE |  |
| decision/Pareto stability | NOT_APPLICABLE |  |
| energy/power | YES | Measured. |
| CPU-FPGA interaction | PARTIAL | MicroBlaze setup + DMA to ICAP. |
| memory/data movement | PARTIAL | Bitstream transfer path from dual-port RAM to ICAP. |

## 14. Possible overlap
PARTIAL OVERLAP on: lifecycle/configuration cost; physical implementation in the loop; energy/power

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Local file is arXiv 1701.08849v1 (Jan 2017); conference version ISWCS 2016 (Sept 2016). IEEE DOI not confirmed (Xplore document 7600972); doi left empty. Local filename says 2017 (arXiv date).
