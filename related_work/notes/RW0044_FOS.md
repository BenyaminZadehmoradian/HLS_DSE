# RW0044 — FOS: A Modular FPGA Operating System for Dynamic Workloads

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Vaishnav, Anuj; Pham, Khoa Dang; Powell, Joseph; Koch, Dirk
- Year / venue: 2020 / ACM TRETS
- DOI: 10.1145/3405794 · URL: https://doi.org/10.1145/3405794
- Metadata source: arXiv PDF (2001.09990v1) + Crossref (TRETS 13(4), 2020, pp. 1-28)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/lifecycle_dfx/RW0044_Vaishnav2020_FOS_TRETS_arxiv.pdf`
- SHA-256: `ba7485013bf6f1bbe99538c806b03e07a112546d0b9c0532d585baedd1e38188`
- Source: https://arxiv.org/pdf/2001.09990

## Code / dataset / artifact provenance
Open source: https://github.com/khoapham/fos (also github.com/FPGA-Research-Manchester/fos)

## 1. Research question
FPGA systems lack modularity and multi-tenancy support; component dependencies force whole-stack recompilation, and static accelerator allocation under-utilizes resources for dynamic workloads.

## 2. Problem setting
Linux-based FPGA OS on Zynq UltraScale+ MPSoC boards with relocatable partial reconfiguration regions shared among tenants.

## 3. Search space
Runtime choice of accelerator implementation variants (e.g., HLS-pragma alternatives) and number of PR slots per request (resource-elastic scheduling); not an offline DSE.

## 4. Evaluation method
On-board measurements on Ultra-96, UltraZed and ZCU102: compile times, re-initialisation latencies, memory throughput, application execution latencies.

## 5. Benchmarks
Spector benchmark suite (OpenCL/HLS), AES, Normal Estimation, Black-Scholes, Mandelbrot, Sobel

## 6. Hardware
Xilinx ZCU102, UltraZed, Ultra-96 (Zynq UltraScale+ MPSoC)

## 7. Toolchain
Vivado / Vivado HLS 2018.2(.1), PetaLinux, BitMan, GoAhead-style PR flow

## 8. Metrics
Compilation (P&R + bitstream) time, component update latency, memory bandwidth, execution latency/speedup

## 9. Baselines
Standard Xilinx PR flow; standard (non-modular) development flow; static single-accelerator execution

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 'FOS can speed up the compilation time by up to 2.34x and avoid standard recompilation requirements to reduce the update latencies by over 100x'; accelerator swap latency 3.81 ms (Ultra-96) / 6.77 ms (ZCU102); DCT achieved 3.55x for 2x resources by switching to a larger implementation.

## 11. Limitations
Requires homogeneous PR regions and fixed interfaces; memory bandwidth contention (row-buffer pollution) limits scaling; rapid multi-tenant requests induce reconfiguration latencies; evaluated on embedded MPSoC boards only.

## 12. What the paper does NOT evaluate
Offline HLS DSE that accounts for PR slot granularity or reconfiguration cost; energy; post-route interaction between co-located accelerators beyond memory bandwidth.

## 13. Relationship to our Studies
- Direct (dimension = YES): S02 S36 S37 S56 S59 S61 S73 S78 S81 S83 S84 S85 S86 S94
- Partial (dimension = PARTIAL): S04 S06 S07 S15 S21 S65 S72

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | Multiple accelerators co-executed and measured together at runtime; not DSE candidate co-evaluation. |
| measured interactions | YES | Measured co-execution effects, e.g., memory-bank contention in Mandelbrot x Sobel scenarios. |
| staged evaluation | NO | Not a DSE method. |
| adaptive evidence acquisition | NO | Not applicable. |
| cost/fidelity modeling | PARTIAL | Compile and reconfiguration latencies quantified; not used in an optimization model. |
| lifecycle/configuration cost | YES | Compile time, component update/re-initialisation latency and PR swap latency quantified (Table 5). |
| physical implementation in the loop | YES | Relocatable PR bitstreams built and run on boards. |
| multi-benchmark transfer | NO | Not studied. |
| decision/Pareto stability | NO | Not studied. |
| energy/power | NO | Not reported. |
| CPU-FPGA interaction | YES | Linux/ARM host runtime and drivers manage accelerators; offloading scenarios. |
| memory/data movement | YES | AXI port throughput characterized; memory contention observed. |

## 14. Possible overlap
PARTIAL OVERLAP on: measured interactions; lifecycle/configuration cost; physical implementation in the loop; CPU-FPGA interaction; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; staged evaluation; decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Open source: https://github.com/khoapham/fos (also github.com/FPGA-Research-Manchester/fos)

## Open questions / reviewer notes
Chosen as DFX3: well-cited DFX-based system that quantifies compile time and partial-reconfiguration/update latency and switches among HLS implementation variants at runtime — relevant to configuration-cost-aware accelerator decisions. Reviewed arXiv v1 (Jan 2020); published TRETS version may differ.
