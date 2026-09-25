# RW0038 — RapidStream 2.0: Automated Parallel Implementation of Latency–Insensitive FPGA Designs Through Partial Reconfiguration

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Guo, Licheng; Maidee, Pongstorn; Zhou, Yun; Lavin, Chris; Hung, Eddie; Li, Wuxi; Lau, Jason; Qiao, Weikang; Chi, Yuze; Song, Linghao; Xiao, Yuanlong; Kaviani, Alireza; Zhang, Zhiru; Cong, Jason
- Year / venue: 2023 / ACM TRETS
- DOI: 10.1145/3593025 · URL: https://doi.org/10.1145/3593025
- Metadata source: PDF first page (ACM reference: ACM Trans. Reconfig. Technol. Syst. 16(4), Article 59, Sep 2023)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/physical/RW0038_Guo2023_RapidStream2_TRETS.pdf`
- SHA-256: `84621e5b380a0700bc525719721e5373832f155ad68715efb50f46209c03f955`
- Source: /home/benyamin/Desktop/Library/RapidStream 2.0: Automated Parallel Implementation of Latency–Insensitive FPGA Designs Through Partial Reconfiguration.pdf

## Code / dataset / artifact provenance
Code referenced ('please refer to our code'); explicit URL NOT_REPORTED in extracted text

## 1. Research question
FPGA compilation (HLS to bitstream) takes many hours with poor CPU parallelism (Vivado ~2.1 cores on average), and split compilation struggles with timing closure on inter-partition nets.

## 2. Problem setting
Parallel, physically integrated compilation of latency-insensitive HLS dataflow designs on AMD UltraScale+ FPGAs (U250, U280), including Vitis shells for host communication.

## 3. Search space
NOT_APPLICABLE (compilation flow; fixed or floorplanned island partition)

## 4. Evaluation method
Full place-and-route and bitstream generation; compile time, CPU/memory profiling and post-route frequency compared with Vivado.

## 5. Benchmarks
RapidStream 1.0: six dataflow designs (AutoSA MM, CNN, LU, MTTKRP; SODA 2-D/3-D stencils) on U250; RapidStream 2.0: two SODA stencil designs (gaussian-int, gaussian-float) on U280 with 4-HBM-channel shell

## 6. Hardware
AMD/Xilinx Alveo U250 and U280

## 7. Toolchain
Vivado 2021.1; RapidWright; RWRoute (customized); AMD DFX; TAPA/AutoBridge front-end

## 8. Metrics
End-to-end compile time and per-step breakdown, active CPU cores, peak memory, post-route frequency

## 9. Baselines
Vanilla Vivado (original and pipelined RTL), Vivado with AutoBridge floorplan hints, RapidStream 1.0

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: RapidStream achieves a 5 to 7x reduction in compile time and up to 1.3x frequency increase vs the commercial toolchain (U250, 1.0) and 5 to 7x compile time reduction with 1.3x frequency (U280, 2.0); e.g., 7.5x and 5.1x faster than Vivado on the two 2.0 benchmarks at 300 MHz.

## 11. Limitations
Requires latency-insensitive (FIFO/AXI) module boundaries; RapidStream 2.0 prototype uses a fixed 6-island partition and a 4-HBM-channel shell with only two benchmarks; RWRoute lacks accurate hold model; abstract-shell generation overhead (~15 min).

## 12. What the paper does NOT evaluate
HLS pragma/microarchitecture DSE; power; runtime reconfiguration use cases; generality across devices beyond U250/U280.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S07 S15 S21 S32 S34 S59 S61 S65 S72 S78 S81 S85 S86 S88 S94
- Partial (dimension = PARTIAL): S02 S10 S11 S36 S37 S56 S73 S83 S84 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Entire multi-module dataflow design implemented with coordinated islands |
| measured interactions | PARTIAL | Inter-island timing isolation via anchor registers; clocking effects studied |
| staged evaluation | YES | Multi-phase flow: partition/floorplan, parallel island implementation, stitching/partial routing |
| adaptive evidence acquisition | NO | No adaptive search |
| cost/fidelity modeling | YES | Compile-time cost is the primary optimized quantity and is profiled |
| lifecycle/configuration cost | YES | Uses partial reconfiguration (DFX) and pre-built shells; partial bitstreams per island |
| physical implementation in the loop | YES | Full place-and-route and bitstreams |
| multi-benchmark transfer | PARTIAL | Several designs; two devices |
| decision/Pareto stability | NOT_APPLICABLE | No search |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | PARTIAL | Integrates Vitis shell with PCIe/DMA for host communication; not evaluated |
| memory/data movement | PARTIAL | HBM subsystem in shell |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; staged evaluation; cost/fidelity modeling; lifecycle/configuration cost; physical implementation in the loop

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code referenced ('please refer to our code'); explicit URL NOT_REPORTED in extracted text

## Open questions / reviewer notes
Journal extension of RapidStream (FPGA'22).
