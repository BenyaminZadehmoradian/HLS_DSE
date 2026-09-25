# RW0031 — Holistic Optimization Framework for FPGA Accelerators

> **Relevance (2026-09-25 correction audit): CORE** — All tasks of a program optimized jointly in one NLP with global/per-SLR resources; joint-vs-local boundary. Primary Studies: S15 S65 S66. Prior-art boundary: PARTIAL OVERLAP.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Pouget, Stéphane; Lo, Michael; Pouchet, Louis-Noël; Cong, Jason
- Year / venue: 2025 / ACM TODAES
- DOI: 10.1145/3769307 · URL: https://doi.org/10.1145/3769307
- Metadata source: PDF first page (ACM reference: ACM Trans. Des. Autom. Electron. Syst. 31(1), Article 7, Nov 2025)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/core/RW0031_Pouget2025_Prometheus_TODAES.pdf`
- SHA-256: `2027336b4b0aa722526ee1226a6205285e7522b1cf8a8f6670a0ee0814f3903b`
- Source: /home/benyamin/Desktop/Library/Holistic Optimization Framework for FPGA Accelerators.pdf

## Code / dataset / artifact provenance
Code: https://github.com/UCLA-VAST/Prometheus

## 1. Research question
Existing HLS optimization frameworks treat loop transformation, pragma insertion, task concurrency, computation-communication overlap and SLR placement separately, producing incoherent designs and often failing bitstream generation on multi-SLR FPGAs.

## 2. Problem setting
Affine (PolyBench-style) multi-statement programs compiled to AMD Vitis HLS dataflow designs with off-chip memory on a multi-SLR Alveo U55C, minimizing latency under per-SLR resource constraints.

## 3. Search space
Task fusion, loop permutation, data-tile sizes with padding, unroll factors, pipelining, array partitioning, transfer/reuse levels and bit width, shared buffer vs FIFO dataflow between tasks, computation-communication overlap (double buffering), per-task SLR assignment.

## 4. Evaluation method
RTL (co-)simulation for all frameworks; on-board execution on Alveo U55C at 220 MHz target with 1 SLR (60% resources) and 3 SLRs for Prometheus.

## 5. Benchmarks
PolyBench/C 4.2.1 medium single-precision kernels (e.g., 2mm, 3mm, atax, bicg, mvt, gemm, syrk, trmm) plus n-madd matrix-addition chains

## 6. Hardware
AMD Alveo U55C

## 7. Toolchain
Vitis HLS 2023.2 (Vitis flow); AMPL; Gurobi 11.0.0

## 8. Metrics
Throughput (GF/s), execution time, resource utilization (DSP/BRAM/LUT/FF), achieved frequency, NLP solve time

## 9. Baselines
AutoDSE, Sisyphus, ScaleHLS, Stream-HLS, Allo

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: on board, Prometheus achieves a 77.16x performance improvement over AutoDSE and 2.59x over Sisyphus (with higher resource use, e.g., 2.38x/3.88x more DSPs); 3mm NLP solves in 21.37 s where Sisyphus timed out after 4 h.

## 11. Limitations
Limited to affine programs; congestion-driven regeneration performed manually; RTL simulation vs on-board gap; baselines needed manual modification (off-chip transfers) and some comparisons limited by availability (Allo artifacts).

## 12. What the paper does NOT evaluate
Power/energy; automated physical feedback loop; non-affine or data-dependent workloads; host-side overhead beyond generated OpenCL host; transfer to other devices.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S07 S15 S21 S59 S61 S65 S72 S73 S78 S81
- Partial (dimension = PARTIAL): S02 S05 S10 S11 S20 S23 S32 S33 S34 S36 S37 S56 S71 S83 S84 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | All tasks/statements of a program optimized jointly in one NLP including per-SLR placement |
| measured interactions | PARTIAL | Models interactions (shared buffers vs FIFOs, overlap, resource contention) analytically; not separately measured |
| staged evaluation | PARTIAL | NLP solution -> RTL simulation -> bitstream, with regeneration on failure |
| adaptive evidence acquisition | PARTIAL | Constraint tightening after failed bitstream uses implementation feedback (manual) |
| cost/fidelity modeling | YES | Analytical latency/resource cost model in NLP |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Bitstreams generated and run on board, including 3-SLR designs |
| multi-benchmark transfer | PARTIAL | Multiple PolyBench kernels; no transfer learning |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | PARTIAL | Generates OpenCL host code; host overhead not analyzed |
| memory/data movement | YES | Off-chip transfers, tiling, reuse, bit width, double buffering modeled |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; cost/fidelity modeling; physical implementation in the loop; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/UCLA-VAST/Prometheus

## Open questions / reviewer notes
Framework is named Prometheus; key chosen as 'Prometheus'.
