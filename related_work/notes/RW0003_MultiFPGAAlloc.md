# RW0003 — Exact and Heuristic Allocation of Multi-kernel Applications to Multi-FPGA Platforms

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Joint allocation of kernel compute units under shared resources/bandwidth; foundation for resource packing, not directive DSE. Primary Studies: S95 S15. Prior-art boundary: RELEVANT BUT DIFFERENT.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Shan, Junnan; Casu, Mario R.; Cortadella, Jordi; Lavagno, Luciano; Lazarescu, Mihai T.
- Year / venue: 2019 / DAC
- DOI: 10.1145/3316781.3317821 · URL: https://doi.org/10.1145/3316781.3317821
- Metadata source: PDF first page (UPCommons copy) + Crossref

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (accepted)
- Canonical path: `related_work/papers/concurrent_multikernel/RW0003_Shan2019_MultiFPGAAlloc_DAC_accepted.pdf`
- SHA-256: `07bce8536ccb0793cd0ebc2c39ec9e6a934150cdb35fa246acaf63231f6e522e`
- Source: https://upcommons.upc.edu/bitstreams/3c0caaa4-c9bf-414e-bd41-bb46034b5c74/download

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Choosing the number of compute units (CUs) per kernel and allocating them across multiple FPGAs to minimize the pipeline initiation interval of multi-kernel applications under per-FPGA resource and DRAM bandwidth constraints.

## 2. Problem setting
Linear task-level pipeline of OpenCL-like kernels (CNN layers) communicating via off-chip DRAM, deployed on an AWS F1 instance with up to 8 FPGAs.

## 3. Search space
Integer CU counts per kernel per FPGA (n_k,f); per-CU implementations are pre-characterized, not searched.

## 4. Evaluation method
Kernel CU versions profiled on AWS F1 (execution time, resources, bandwidth); allocation quality evaluated with the analytic model (II vs resource constraint) comparing solvers; solver CPU time measured.

## 5. Benchmarks
AlexNet (16-bit fixed, 32-bit float), VGG16 (16-bit fixed) conv/pool/norm layers

## 6. Hardware
AWS F1 (8x Xilinx UltraScale+ FPGAs); optimizer on Intel Core i7-2600

## 7. Toolchain
Xilinx SDAccel; GPkit; Couenne MINLP solver

## 8. Metrics
Initiation interval, FPGA resource utilization (DSP/BRAM), spreading, optimizer CPU time

## 9. Baselines
MINLP (II only), MINLP+G (II + spreading) via Couenne

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: GP+A obtains results comparable to the MINLP solver but is 2-3 orders of magnitude faster (0.78 s to 4.4 s vs ~1 min to several hours).

## 11. Limitations
Only linear pipelines; all communication via off-chip DRAM (no on-chip/FPGA-to-FPGA links); power not considered; kernel execution time assumed to scale linearly with CUs and independent of placement; VGG kernels not fully optimized; FC layers not implemented; end-to-end on-board runs of the allocated designs are not the main reported result.

## 12. What the paper does NOT evaluate
Intra-kernel HLS pragma search, measured interactions between co-located CUs (routing congestion, frequency degradation), reconfiguration cost, energy, host-CPU time (explicitly ignored).

## 13. Relationship to our Studies
- Direct (dimension = YES): S07 S15 S65 S73
- Partial (dimension = PARTIAL): S02 S04 S06 S21 S32 S34 S36 S37 S43 S45 S56 S59 S61 S72 S78 S81 S83 S84 S88 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | All kernels' CU counts and placements are optimized jointly under shared per-FPGA constraints. |
| measured interactions | PARTIAL | Shared resource/bandwidth constraints capture additive interactions; no measured non-additive effects. |
| staged evaluation | PARTIAL | Two-step solve (GP relaxation then discrete allocation), not multi-fidelity evaluation. |
| adaptive evidence acquisition | NO | Kernel profiles collected up front. |
| cost/fidelity modeling | PARTIAL | Optimizer runtime compared (MINLP vs GP+A); evaluation fidelity not modeled. |
| lifecycle/configuration cost | NO | Not considered. |
| physical implementation in the loop | PARTIAL | Kernel CUs characterized from on-board AWS F1 runs; allocations themselves evaluated via model. |
| multi-benchmark transfer | NO | Not studied. |
| decision/Pareto stability | PARTIAL | Sensitivity of II to heuristic parameter T analysed; no stability analysis of decisions. |
| energy/power | NO | Explicitly not considered (power constraints left out). |
| CPU-FPGA interaction | PARTIAL | Host CPU orchestrates; CPU time explicitly ignored in model. |
| memory/data movement | YES | Per-FPGA DRAM bandwidth constraint in the model. |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
PDF is the institutional (UPCommons) author copy; no ACM copyright block visible, assumed accepted version. Follow-up journal version: Shan et al., 'CNN-on-AWS: Efficient Allocation of Multikernel Applications on Multi-FPGA Platforms', IEEE TCAD 2020/2021.
