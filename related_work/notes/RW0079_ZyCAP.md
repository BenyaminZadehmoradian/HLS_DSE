# RW0079 — ZyCAP: Efficient Partial Reconfiguration Management on the Xilinx Zynq

> **Relevance (2026-09-25 full-text review): SUPPORTING** — Measured partial-reconfiguration throughputs (PCAP, AXI HWICAP with/without DMA, custom ICAP-DMA controller) and bitstream sizes on ZedBoard (Zynq-7020 class): the configuration-cost evidence S85/S86 need, on the platform S100 targets. Not a DSE paper; no joint evaluation or evidence selection. Primary Studies: S85 S86 S100. Prior-art boundary: METHOD FOUNDATIONAL.
> **Identity:** File is the Warwick WRAP repository copy (wrap.warwick.ac.uk/86739); version of record IEEE ESL 6(3):41-44, 2014. Paper names ZedBoard, not the part; xc7z020 inferred.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Vipin, Kizheppatt; Fahmy, Suhaib A.
- Year / venue: 2014 / IEEE Embedded Systems Letters 6(3):41-44
- DOI: 10.1109/LES.2014.2314390 · URL: https://doi.org/10.1109/LES.2014.2314390

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: accepted (Warwick WRAP repository copy)
- Canonical path: `related_work/papers/lifecycle_dfx/RW0079_Vipin2014_ZyCAP_ESL_accepted.pdf` (local only, gitignored)
- SHA-256: `2fe34e14a04decc4a549503e815bc30639ca763d682f401c0cf28daae6481cad`
- Source: https://wrap.warwick.ac.uk/86739/7/WRAP_esl2013.pdf

## Code provenance
https://github.com/archntu/zycap

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Zynq partial-reconfiguration management either blocks the ARM processor (PCAP, AXI HWICAP) or gives low throughput; can a PL-side controller + driver reach near-peak ICAP throughput and overlap reconfiguration with software?

## 2. Problem setting / 3. Search space / 4. Evaluation method
ZyCAP: soft DMA + ICAP manager + ICAP primitive, configured over AXI-Lite (GP), streaming bitstreams from DRAM over AXI4 bursts (HP), interrupt on completion; standalone driver with prefetch and an LRU DRAM bitstream cache. Compared with PCAP (XDcfg), AXI HWICAP and AXI HWICAP + PS DMA. Case study: image pipeline reconfiguring one PRR twice per iteration.

## 5. Benchmarks
Reconfiguration throughput microbenchmark (Table I); edge-detection pipeline, frame sizes 32 to 4096 pixels (Fig. 5).

## 6. Hardware
ZedBoard (XC7Z020 inferred from board and the 4,045,564-byte full bitstream); PRR 2300 CLBs, 60 DSPs, 50 BRAMs; PL at 100 MHz; ICAP 32-bit at 100 MHz (400 MB/s theoretical).

## 7. Toolchain
Xilinx EDK 14.6 and PlanAhead 14.6 (ISE era); standalone OS; hardware timer.

## 8. Metrics
Reconfiguration throughput (MB/s); PL resources; application throughput; timing-model parameters (Table II).

## 9. Baselines
PCAP (XDcfg), AXI HWICAP without DMA, AXI HWICAP with PS DMA.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: Table I: PCAP 128 MB/s (0 PL resources); AXI HWICAP 19 MB/s; AXI HWICAP + DMA 67 MB/s; ZyCAP 382 MB/s (806 FF, 620 LUT; 95.5% of 400 MB/s peak), i.e. 20x/5.7x/2.98x faster. Partial bitstream 1,018,080 B vs full Zynq bitstream 4,045,564 B; DRAM-to-PRR DMA 382 MB/s; processor-DRAM 128 MB/s; peripheral access latency 140 ns; DMA setup 1.12 us. Table II: Tconfig = 0.970/T s (T in MB/s). Reviewer-derived: partial reconfiguration ~2.5 ms (ZyCAP), ~7.6 ms (PCAP), ~14.5 ms (DMA-HWICAP), ~51 ms (HWICAP); full 4.05 MB over PCAP ~32 ms (not measured in the paper). Fig. 5 at 512x512: 11.35x/3.28x/2.96x application throughput over HWICAP/DMA-HWICAP/PCAP.

## 11. Limitations
AUTHOR-STATED: standalone OS only; gap to peak from DMA setup, DRAM latency and interrupt sync. REVIEWER: single point measurements without variance; SD-card-to-DRAM load not quantified; full-bitstream time not measured; 2013-era ISE tools (Vivado/Linux FPGA Manager path may differ); one PRR size; no energy; PR-DMA vs accelerator-DMA contention not measured.

## 12. What the paper does NOT evaluate
Full-bitstream reconfiguration time; loading from storage; Linux overhead; multiple PRRs/concurrent accelerators; reconfiguration energy; memory interference; HLS accelerators; DSE.

## 13. Relationship to our Studies (S85 S86 S100)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | one PRR, accelerators swapped sequentially |
| measured interactions | NO | PR/data DMA contention not measured |
| staged evaluation | NO |  |
| adaptive evidence acquisition | NO |  |
| cost/fidelity modeling | PARTIAL | analytical timing model (Table II), no fidelity modelling |
| lifecycle/configuration cost | YES | reconfiguration throughput, bitstream sizes, caching/prefetch, blocking vs overlapped (Tables I-II, Fig. 5) |
| physical implementation in the loop | YES | measured on ZedBoard with a PR floorplan |
| multi-benchmark transfer | NO |  |
| decision/Pareto stability | NOT_REPORTED | no repeated-measurement variance |
| energy/power | NO | discussed analytically only |
| CPU-FPGA interaction | YES | PS-PL interfaces, processor blocking vs overlap, 140 ns access latency |
| memory/data movement | PARTIAL | DRAM-to-PL throughputs, bitstream caching; no contention study |

## 14. Possible overlap
METHOD FOUNDATIONAL

## 15. Possible research gap (not a novelty claim)
S85/S86 priors for ZedBoard/xc7z020: ~128 MB/s PCAP and up to 382 MB/s ICAP-DMA, i.e. ~2.5-8 ms per 1 MB partial and ~32 ms (derived) per full bitstream; must be re-measured under the project's Vivado/Linux stack. For S100 the shared DRAM/HP path is shown but no interference data is given. For S99, ms-scale configuration cost is negligible next to minutes-to-hours of synthesis: joint-evidence cost is dominated by building it.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/archntu/zycap.
