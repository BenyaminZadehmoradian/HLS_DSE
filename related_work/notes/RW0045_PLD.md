# RW0045 — PLD: Fast FPGA Compilation to Make Reconfigurable Acceleration Compatible with Modern Incremental Refinement Software Development

> **Relevance (2026-09-25 correction audit): SUPPORTING** — DFX-based fast compilation trading compile cost against QoR: build/configuration cost source. Primary Studies: S85 S94. Prior-art boundary: RELEVANT BUT DIFFERENT.
> **Identity:** Key renamed from placeholder DFX2.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Xiao, Yuanlong; Micallef, Eric; Butt, Andrew; Hofmann, Matthew; Alston, Marc; Goldsmith, Matthew; Merczynski-Hait, Andrew; DeHon, André
- Year / venue: 2022 / ASPLOS
- DOI: 10.1145/3503222.3507740 · URL: https://doi.org/10.1145/3503222.3507740
- Metadata source: PDF first page (published, CC BY-NC-ND) + Crossref (pp. 933-945)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (published)
- Canonical path: `related_work/papers/lifecycle_dfx/RW0045_Xiao2022_PLD_ASPLOS.pdf`
- SHA-256: `17a42a757d216ee774c90c86068ab73d7dbe7baa5068b9274bbb3efb6f1a108f`
- Source: https://ic.ese.upenn.edu/pdf/pld_asplos2022.pdf

## Code / dataset / artifact provenance
Open source: https://github.com/icgrp/pld2022

## 1. Research question
FPGA compile times of hours inhibit incremental edit-compile-debug refinement; the paper introduces separate compilation and linking of HLS operators using DFX partial-reconfiguration pages to offer compile-time/performance trade-off levels.

## 2. Problem setting
Streaming dataflow HLS applications decomposed into operators, compiled to soft processors (-O0), separately to DFX pages linked by an on-chip network (-O1), or monolithically (-O3), on an Alveo U50.

## 3. Search space
NOT_APPLICABLE (compilation option / operator-to-page mapping choices, not an automated DSE)

## 4. Evaluation method
Measured compile times (HLS, synthesis, place & route, bitstream) and on-board runtime performance on Alveo U50.

## 5. Benchmarks
Rosetta benchmark suite (3D Rendering, Digit Recognition, Spam Filter, Optical Flow, BNN, Face Detection)

## 6. Hardware
Xilinx Alveo U50 (Virtex UltraScale+ XCU50)

## 7. Toolchain
Xilinx Vitis 2021.1 (Vivado, Vitis HLS), abstract shell DFX flow

## 8. Metrics
Compile time (per stage and total), application runtime/throughput, clock frequency, resource utilization

## 9. Baselines
Monolithic Vitis flow; PLD -O3 decomposed monolithic; all-softcore -O0

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: separate compilation (-O1) reduces compile times from 1-2 hours to 10-20 minutes (4.2-7.3x speedup) and -O0 to under 4 seconds; -O1 designs run 1.5-10x slower than monolithic, while -O3 decomposed designs match monolithic performance.

## 11. Limitations
-O1 performance limited by linking-network bandwidth and overlay overhead; requires streaming-dataflow operator decomposition (hls::stream interfaces); increased BRAM use for FIFOs; page sizes fixed.

## 12. What the paper does NOT evaluate
Automated DSE over HLS pragmas using the compile-time/QoR trade-off; energy; runtime reconfiguration time as a system cost beyond loading pages.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S21 S32 S34 S59 S61 S72 S78 S81 S85 S86 S88 S94
- Partial (dimension = PARTIAL): S02 S07 S15 S36 S37 S56 S65 S73 S83 S84

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Operators compiled locally/separately then linked; whole-application performance measured. |
| measured interactions | PARTIAL | Compares decomposed vs monolithic performance (network bottlenecks, SLR crossings). |
| staged evaluation | YES | -O0 / -O1 / -O3 levels provide progressively slower but higher-quality compile paths. |
| adaptive evidence acquisition | NO | Not a DSE method. |
| cost/fidelity modeling | YES | Compile time vs performance trade-off quantified per level. |
| lifecycle/configuration cost | YES | Compile/turnaround cost is the core subject; partial bitstream loading used. |
| physical implementation in the loop | YES | Full place & route and bitstream per page; on-board execution. |
| multi-benchmark transfer | NO | Not studied. |
| decision/Pareto stability | NO | Not studied. |
| energy/power | NO | Not reported. |
| CPU-FPGA interaction | PARTIAL | Host driver orchestrates bitstream loading; soft processors as -O0 target. |
| memory/data movement | PARTIAL | Linking network bandwidth and FIFO/BRAM use discussed. |

## 14. Possible overlap
PARTIAL OVERLAP on: staged evaluation; cost/fidelity modeling; lifecycle/configuration cost; physical implementation in the loop

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Open source: https://github.com/icgrp/pld2022

## Open questions / reviewer notes
Chosen as DFX2: uses DFX partial reconfiguration regions directly in an HLS flow and quantifies compile/turnaround cost vs QoR — relevant to evaluation-cost/lifecycle aspects of HLS-DSE. Related follow-up: HiPR (FPL 2022) high-level partial reconfiguration for fast incremental compile.
