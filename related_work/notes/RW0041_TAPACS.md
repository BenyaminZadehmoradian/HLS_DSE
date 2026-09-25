# RW0041 — TAPA-CS: Enabling Scalable Accelerator Design on Distributed HBM-FPGAs

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Prakriya, Neha; Chi, Yuze; Basalama, Suhail; Song, Linghao; Cong, Jason
- Year / venue: 2024 / ASPLOS
- DOI: 10.1145/3620666.3651347 · URL: https://doi.org/10.1145/3620666.3651347
- Metadata source: PDF first page (ACM reference format, ASPLOS '24)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/physical/RW0041_Prakriya2024_TAPACS_ASPLOS.pdf`
- SHA-256: `63eea3584b15f3501a0e3a4fe26000015159d65671c335b656f747547669e227`
- Source: /home/benyamin/Desktop/Library/TAPA-CS: Enabling Scalable Accelerator Design on Distributed HBM-FPGAs.pdf

## Code / dataset / artifact provenance
Stated as open-source; repository URL not found in extracted text (NOT_REPORTED)

## 1. Research question
Large dataflow accelerators exceed a single FPGA, and existing tools do not automatically partition designs across network-connected multi-die HBM FPGAs while maintaining high frequency and hiding inter-FPGA communication latency.

## 2. Problem setting
Automatic partitioning and compilation of C++ task-parallel dataflow designs across a cluster of Alveo U55C FPGAs connected by 100 Gbps Ethernet (ring), with intra-FPGA floorplanning.

## 3. Search space
Task-to-FPGA assignment (topology-aware), task-to-slot assignment within each FPGA, interconnect pipelining, HBM channel usage

## 4. Evaluation method
On-board execution of implemented multi-FPGA designs (runtime, throughput) and post-route frequency.

## 5. Benchmarks
Stencil (Dilate etc.), systolic-array CNNs, PageRank graph processing (e.g., cit-Patents), KNN; scaled 2-8 FPGAs

## 6. Hardware
Two nodes with four AMD/Xilinx Alveo U55C each (QSFP28 ring); AMD EPYC 7V13 host

## 7. Toolchain
Vitis 2022.1; Python MIP or Gurobi; AlveoLink

## 8. Metrics
Speedup/throughput vs single-FPGA Vitis baseline, Fmax, resource utilization, data transfer volumes

## 9. Baselines
Single-FPGA Vitis HLS designs; prior multi-FPGA approaches discussed qualitatively

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 2-, 3- and 4-FPGA designs are on average 2.1x, 3.2x and 4.4x faster than single-FPGA Vitis HLS baselines, with 11%-116% frequency improvement over Vitis HLS; an 8-FPGA stencil across two nodes is 1.45x slower than single FPGA due to host-mediated inter-node transfers.

## 11. Limitations
Scalability limited by communication-heavy or sequential workloads; inter-node communication through host MPI over 10 Gbps; AlveoLink limitations; relies on user-provided dataflow task decomposition.

## 12. What the paper does NOT evaluate
Intra-task HLS pragma DSE; power/energy; learned or multi-fidelity cost models; reconfiguration costs.

## 13. Relationship to our Studies
- Direct (dimension = YES): S02 S07 S15 S36 S37 S56 S59 S61 S65 S73 S78 S81
- Partial (dimension = PARTIAL): S04 S06 S10 S11 S21 S32 S34 S72 S83 S84 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | All tasks partitioned jointly across FPGAs and slots |
| measured interactions | YES | Inter-task communication cost across dies/FPGAs modeled and measured |
| staged evaluation | PARTIAL | Hierarchical (inter-FPGA then intra-FPGA) partitioning |
| adaptive evidence acquisition | NO | No feedback loop |
| cost/fidelity modeling | PARTIAL | ILP cost on communication/resources |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Full implementation and on-board runs |
| multi-benchmark transfer | PARTIAL | Several application types |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | PARTIAL | Host MPI used for inter-node transfers; host-device data movement discussed |
| memory/data movement | YES | HBM channel allocation and inter-FPGA data volumes analyzed |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; measured interactions; physical implementation in the loop; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Stated as open-source; repository URL not found in extracted text (NOT_REPORTED)

## Open questions / reviewer notes
none
