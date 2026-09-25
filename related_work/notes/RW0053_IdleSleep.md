# RW0053 — Idle is the New Sleep: Configuration-Aware Alternative to Powering Off FPGA-Based DL Accelerators During Inactivity

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Qian, Chao; Cichiwskyj, Christopher; Ling, Tianheng; Schiele, Gregor
- Year / venue: 2024 / ARCS (LNCS 14842)
- DOI: 10.1007/978-3-031-66146-4_11 · URL: https://doi.org/10.1007/978-3-031-66146-4_11
- Metadata source: PDF (arXiv:2407.12027v2 stamp) + web search (Springer chapter, ARCS 2024, LNCS 14842)

## PDF provenance
- Status: `LOCAL_EXISTING` (arxiv)
- Canonical path: `related_work/papers/energy_sustainability/RW0053_Qian2024_IdleSleep_ARCS_arxiv.pdf`
- SHA-256: `53963a987e44eec8db8561cd7f4e7653691d9a39cf8f4abfd0d7a43329036e29`
- Source: /home/benyamin/Desktop/pragma_mach/reference/papers/idle_is_the_new_sleep_2024.pdf

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
In duty-cycled IoT inference, FPGA configuration energy after power-off dominates; when is keeping the FPGA configured and idle better than On-Off?

## 2. Problem setting
MCU+FPGA (RP2040 + Spartan-7) embedded platform running a DL (LSTM) accelerator with periodic requests under an energy budget.

## 3. Search space
Configuration parameters: SPI bus width (3 options), SPI clock (11 frequencies), bitstream compression; strategies On-Off vs Idle-Waiting; idle power-saving methods

## 4. Evaluation method
On-board power measurement (PAC1934 sensors, 1024 Hz) + simulator validated against hardware (2.7% lifetime discrepancy)

## 5. Benchmarks
LSTM accelerator (hidden size 20) from authors' prior work

## 6. Hardware
Elastic-node-style board: RP2040 MCU + Spartan-7 XC7S15 (also XC7S25)

## 7. Toolchain
NOT_REPORTED (AMD/Xilinx 7-series configuration flow)

## 8. Metrics
Configuration time/power/energy, idle power, executable workload items, system lifetime

## 9. Baselines
Default configuration settings (Single SPI 3 MHz, uncompressed); On-Off strategy

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: tuned configuration cuts configuration energy 40.13x (to 11.85 mJ); Idle-Waiting with power-saving beats On-Off for request periods up to 499.06 ms and at 40 ms extends lifetime ~12.39x within a 4147 J budget.

## 11. Limitations
Idle power bound by flash component; voltage scaling only simulated; single accelerator; periodic requests only.

## 12. What the paper does NOT evaluate
HLS DSE of accelerator, partial reconfiguration, multi-accelerator systems.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20 S59 S61 S78 S81 S83 S84 S85 S86 S94
- Partial (dimension = PARTIAL): S02 S04 S06 S21 S36 S37 S43 S45 S56 S72 S73 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE |  |
| measured interactions | PARTIAL | Joint effect of bus width, clock and compression on configuration energy measured. |
| staged evaluation | NOT_APPLICABLE |  |
| adaptive evidence acquisition | NOT_APPLICABLE |  |
| cost/fidelity modeling | PARTIAL | Simulator vs hardware fidelity checked (2.7%). |
| lifecycle/configuration cost | YES | Configuration energy and on/off vs idle lifecycle central. |
| physical implementation in the loop | YES | Real bitstreams on hardware. |
| multi-benchmark transfer | NO |  |
| decision/Pareto stability | PARTIAL | Crossover request period between strategies derived. |
| energy/power | YES | Measured. |
| CPU-FPGA interaction | YES | MCU-FPGA SPI configuration and offloading. |
| memory/data movement | PARTIAL | Bitstream loading over SPI from flash. |

## 14. Possible overlap
PARTIAL OVERLAP on: lifecycle/configuration cost; physical implementation in the loop; energy/power; CPU-FPGA interaction

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Local file is arXiv 2407.12027v2 (21 Apr 2026), revised after ARCS 2024 publication.
