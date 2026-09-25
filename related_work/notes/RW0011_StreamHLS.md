# RW0011 — Stream-HLS: Towards Automatic Dataflow Acceleration

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Basalama, Suhail; Cong, Jason
- Year / venue: 2025 / FPGA
- DOI: 10.1145/3706628.3708878 · URL: https://doi.org/10.1145/3706628.3708878
- Metadata source: PDF first page (ACM reference format, FPGA '25)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/concurrent_multikernel/RW0011_Basalama2025_StreamHLS_FPGA.pdf`
- SHA-256: `83570565411d5f63c5e08bb883c9eacde9d3cb0402f3381bf23a8d1d700f888b`
- Source: /home/benyamin/Desktop/Library/Stream-HLS: Towards Automatic Dataflow Acceleration.pdf

## Code / dataset / artifact provenance
Code: https://github.com/UCLA-VAST/Stream-HLS ; artifact DOI 10.5281/zenodo.14585909

## 1. Research question
HLS automation frameworks mostly insert pragmas without loop scheduling, target single kernels, lack global DSE, and miss graph-level pipelining (streaming) for multi-kernel applications.

## 2. Problem setting
Automatic conversion of sequential multi-kernel C/C++ or PyTorch programs into globally optimized FPGA dataflow architectures under a DSP budget.

## 3. Search space
Per-node loop permutations (for node/graph-level pipelining), shared buffer vs FIFO inter-task channels, per-node unroll/tiling (parallelization) factors under a global DSP limit

## 4. Evaluation method
Cycle-accurate RTL simulation of Vitis HLS 2023.2 designs (HLS reports deemed inaccurate for dataflow); performance model validated against RTL simulation.

## 5. Benchmarks
7 PolyBench kernels (e.g., 3mm, atax, bicg, gesummv), transformer multi-head self-attention and FFN, residual block, depthwise separable conv block, two MLPs, synthetic 7mm balanced/imbalanced

## 6. Hardware
AMD Alveo U280 (target; DSP limits 220, 2560 = ~1 SLR, 9024)

## 7. Toolchain
Vitis HLS 2023.2; MLIR; AMPL + Gurobi

## 8. Metrics
RTL-simulated cycle counts, speedup, DSE runtime, DSP utilization

## 9. Baselines
Vitis HLS default, Allo and HeteroCL (manually optimized), HIDA, ScaleHLS, POM (automatic)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: Stream-HLS designs outperform prior automation frameworks and manually optimized abstraction-framework designs by up to 79.43x and 10.62x geometric means; combined MINLP (Opt5) achieves 27.67x-1300.42x speedups (geo-mean 314.89x) over the FIFO-only baseline; DSE runtime 176.41x faster than HIDA.

## 11. Limitations
Assumes inputs/outputs in fast partitioned on-chip memory (no DDR/HBM bandwidth modeling); Vitis may not achieve predicted II under node-level parallelization; FIFOs sized to write counts; no stencil support; no place-and-route evaluation.

## 12. What the paper does NOT evaluate
Post-route timing/Fmax and on-board execution; off-chip memory bandwidth; power; FIFO depth optimization (addressed later by FIFOAdvisor); physical multi-SLR placement.

## 13. Relationship to our Studies
- Direct (dimension = YES): S02 S04 S06 S07 S15 S21 S36 S37 S56 S65 S72
- Partial (dimension = PARTIAL): S10 S11 S32 S34 S73 S83 S84 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | All kernels (nodes) of a multi-kernel application scheduled jointly under a global DSP budget |
| measured interactions | YES | Graph-level pipelining interactions between producer/consumer nodes modeled and ablated (Opt2-Opt5) |
| staged evaluation | PARTIAL | Compares staged (two MINLPs) vs joint MINLP formulations |
| adaptive evidence acquisition | NO | Single model-driven solve |
| cost/fidelity modeling | YES | Analytical dataflow performance model validated vs RTL simulation |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | NO | RTL simulation only |
| multi-benchmark transfer | PARTIAL | Multiple application categories; no transfer |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | PARTIAL | Generates host code; host interaction not evaluated |
| memory/data movement | PARTIAL | On-chip FIFO vs shared buffer communication modeled; off-chip explicitly excluded |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; measured interactions; cost/fidelity modeling

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/UCLA-VAST/Stream-HLS ; artifact DOI 10.5281/zenodo.14585909

## Open questions / reviewer notes
none
