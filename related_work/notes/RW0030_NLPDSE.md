# RW0030 — Automatic Hardware Pragma Insertion in High-Level Synthesis: A Non-Linear Programming Approach

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Pouget, Stéphane; Pouchet, Louis-Noël; Cong, Jason
- Year / venue: 2025 / ACM TODAES
- DOI: 10.1145/3711847 · URL: https://doi.org/10.1145/3711847
- Metadata source: PDF first page (ACM reference: ACM Trans. Des. Autom. Electron. Syst. 30(2), Article 26, Feb 2025)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/hls_dse/RW0030_Pouget2025_NLPDSE_TODAES.pdf`
- SHA-256: `34b85a725f66942c067fc4aec706193321ea3de05fa4a35e4f76700a195c895d`
- Source: /home/benyamin/Desktop/Library/Automatic Hardware Pragma Insertion in High-Level Synthesis: A Non-Linear Programming Approach.pdf

## Code / dataset / artifact provenance
NOT_REPORTED (no code URL in the paper)

## 1. Research question
Pragma DSE for HLS is either very time-consuming (hundreds of HLS runs) or operates on restricted spaces because the QoR landscape of pragma configurations is irregular.

## 2. Problem setting
Affine loop-based C kernels optimized via AMD/Xilinx Merlin pragmas and Vitis HLS on an Alveo U200, minimizing latency under resource limits.

## 3. Search space
Merlin pragmas: parallel (fine/coarse-grained unroll factors), pipeline (flatten/off), tile factors, data caching; plus DSE over maximum array-partitioning factor and parallelism type.

## 4. Evaluation method
Merlin + Vitis HLS 2021.1 synthesis reports (HLS latency estimates) for NLP-selected designs.

## 5. Benchmarks
PolyBench/C 4.2.1 (medium and large; 47 kernel/size cases) plus a CNN layer; HARP comparison on small/medium double-precision PolyBench

## 6. Hardware
AMD/Xilinx Alveo U200 @250 MHz (target of synthesis)

## 7. Toolchain
AMD/Xilinx Merlin; Vitis 2021.1; AMPL; BARON 21.1.13; PolyOpt-HLS (modified)

## 8. Metrics
Throughput (GFLOP/s), DSE time, number of designs explored/timeouts, NLP solve time, lower-bound tightness vs HLS latency

## 9. Baselines
AutoDSE, HARP, ScaleHLS

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: vs AutoDSE, DSE time is 5.69x faster on average (3.70x geo-mean) and throughput 17.24x higher on average (2.38x geo-mean), with 46/47 cases matching (+/-2%) or beating AutoDSE; vs HARP throughput 1.45x average (1.21x geo-mean); vs ScaleHLS 11.63x average (2.89x geo-mean) including memory transfers.

## 11. Limitations
Restricted to affine programs; lower bound relies on pragmas being applied as intended (about half of designs had at least one pragma not applied) and on optimistic memory-transfer modeling; excludes double-buffering pragma and code transformations; NLP can time out (12 kernels had a 30-min timeout).

## 12. What the paper does NOT evaluate
Post-route timing/frequency or on-board runs; power; multi-kernel/system-level interactions; host-FPGA transfer costs beyond on-chip caching; generalization to non-affine code.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S21 S32 S34 S72 S73 S88
- Partial (dimension = PARTIAL): S02 S05 S10 S11 S20 S23 S33 S36 S37 S56 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | One kernel at a time |
| measured interactions | PARTIAL | Model captures pragma interactions (partitioning vs unroll, resource sharing) within a kernel |
| staged evaluation | YES | NLP lower bound used to rank/prune before HLS synthesis |
| adaptive evidence acquisition | PARTIAL | Iterative DSE stops when lower bound exceeds best synthesized latency |
| cost/fidelity modeling | YES | Analytical lower-bound model versus expensive HLS runs; bound tightness evaluated |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | NO | HLS reports only |
| multi-benchmark transfer | PARTIAL | Many PolyBench kernels and sizes; no learned transfer |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | YES | Off-chip to on-chip transfer, tiling/caching and burst width modeled |

## 14. Possible overlap
PARTIAL OVERLAP on: staged evaluation; cost/fidelity modeling; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no code URL in the paper)

## Open questions / reviewer notes
Local filename matches title exactly; 44-page journal version.
