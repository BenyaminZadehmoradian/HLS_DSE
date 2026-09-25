# RW0033 — FIFOAdvisor: A DSE Framework for Automated FIFO Sizing of High-Level Synthesis Designs

> **Relevance (2026-09-25 correction audit): CORE** — All inter-kernel FIFO depths of a dataflow design sized jointly against whole-design latency; inter-kernel interaction boundary. Primary Studies: S15 S36 S65. Prior-art boundary: PARTIAL OVERLAP.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Abi-Karam, Stefan; Sarkar, Rishov; Basalama, Suhail; Cong, Jason; Hao, Callie
- Year / venue: 2026 / ASP-DAC
- DOI: 10.1109/ASP-DAC66049.2026.11420742 · URL: https://doi.org/10.1109/ASP-DAC66049.2026.11420742
- Metadata source: PDF first page (IEEE Xplore header with DOI, ASP-DAC 2026)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/core/RW0033_AbiKaram2026_FIFOAdvisor_ASPDAC.pdf`
- SHA-256: `8f57ad7f0cf58bdc300336cf47cbaf3068c365a7bea6924466b7a5b8ac4fbe0f`
- Source: /home/benyamin/Desktop/Library/FIFOAdvisor: A DSE Framework for Automated FIFO Sizing of High-Level Synthesis Designs.pdf

## Code / dataset / artifact provenance
Code and results: https://github.com/sharc-lab/fifo-advisor

## 1. Research question
Sizing FIFO channels in HLS dataflow designs trades latency (stalls/deadlock) against on-chip memory; static analyses cannot handle data-dependent control flow and co-simulation-based search is too slow.

## 2. Problem setting
Deadlock-free, dual-objective (latency vs BRAM) FIFO depth selection for Vitis HLS dataflow designs with multiple interacting tasks, including data-dependent control flow.

## 3. Search space
Per-FIFO (or per-FIFO-group) depths between 2 and an upper bound, pruned to BRAM-capacity breakpoints

## 4. Evaluation method
LightningSim cycle counts (validated against Vitis C/RTL co-simulation, within 1 cycle for all but one design, 2.3% for Autoencoder) and analytical BRAM model validated against HLS synthesis.

## 5. Benchmarks
21-22 Stream-HLS dataflow kernels (linear algebra, DNN layers, e.g., k15mmtree, k15mmtseq, Autoencoder); FlowGNN PNA accelerator case study

## 6. Hardware
AMD/Xilinx Alveo U280 (synthesis target)

## 7. Toolchain
Vitis HLS 2023.2; LightningSim 0.2.6

## 8. Metrics
Latency (cycles) relative to baselines, FIFO BRAM usage, Pareto frontiers, search runtime vs estimated co-simulation runtime

## 9. Baselines
Baseline-Max (FIFOs sized to write counts, Stream-HLS default), Baseline-Min (all depth 2), co-simulation-based search (runtime estimate), INR-Arch-style greedy

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: vs Baseline-Max, grouped optimizers find configurations with zero FIFO BRAMs and virtually no slowdown (1.0026x / 0.9994x latency); greedy saves 85.6% BRAM; vs Baseline-Min, grouped SA gives 0.52x latency with ~3.0 BRAMs and un-deadlocks designs; search is 10^5-10^7x faster than co-simulation-based search.

## 11. Limitations
Optimizes for a single testbench input set; FIFOs mapped only to BRAM (no URAM), flip-flop overhead ignored; BRAM model targets UltraScale+.

## 12. What the paper does NOT evaluate
Post-route timing or Fmax impact of FIFO sizes; power; joint optimization with task-level pragmas (only integration with Stream-HLS); robustness across input stimuli; on-board measurement.

## 13. Relationship to our Studies
- Direct (dimension = YES): S02 S04 S06 S07 S15 S21 S36 S37 S56 S65 S72 S73
- Partial (dimension = PARTIAL): S05 S10 S11 S20 S23 S33 S43 S45 S71 S90 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | All FIFOs of a multi-task dataflow design are sized jointly with whole-design latency |
| measured interactions | YES | Inter-task FIFO effects (stalls, deadlocks) captured via simulation |
| staged evaluation | NO | Single evaluator (LightningSim) per candidate |
| adaptive evidence acquisition | PARTIAL | Simulated annealing/greedy use evaluation feedback; no explicit acquisition function |
| cost/fidelity modeling | YES | Cheap simulator vs co-simulation runtime quantified |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | NO | No place-and-route |
| multi-benchmark transfer | PARTIAL | Evaluated across 21 Stream-HLS kernels plus FlowGNN; no transfer |
| decision/Pareto stability | PARTIAL | Full Pareto frontiers reported; selection via alpha score; no stability analysis |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Host not modeled |
| memory/data movement | YES | FIFO buffering/BRAM memory usage is the optimized quantity |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; measured interactions; cost/fidelity modeling; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: staged evaluation; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code and results: https://github.com/sharc-lab/fifo-advisor

## Open questions / reviewer notes
Paper text mentions both 21 and 22 Stream-HLS kernels.
