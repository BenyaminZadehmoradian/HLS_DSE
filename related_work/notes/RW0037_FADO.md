# RW0037 — FADO: Floorplan-Aware Directive Optimization for High-Level Synthesis Designs on Multi-Die FPGAs

> **Relevance (2026-09-25 correction audit): CORE** — Directives of multiple kernels co-optimized under shared per-die resources with floorplan interaction; joint multi-kernel boundary. Primary Studies: S15 S65 S78. Prior-art boundary: PARTIAL OVERLAP.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Du, Linfeng; Liang, Tingyuan; Sinha, Sharad; Xie, Zhiyao; Zhang, Wei
- Year / venue: 2023 / FPGA
- DOI: 10.1145/3543622.3573188 · URL: https://doi.org/10.1145/3543622.3573188
- Metadata source: arXiv v3 PDF (author version with FPGA'23 reference) + arXiv abs page

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/core/RW0037_Du2023_FADO_FPGA_arxiv.pdf`
- SHA-256: `4e63512b5bd841b194d0ffbac8aab37b3397ea74ec0783cfade65e9e06bff353`
- Source: https://arxiv.org/pdf/2212.11582

## Code / dataset / artifact provenance
Code: https://github.com/RipperJ/FADO (stated fully open-sourced in paper)

## 1. Research question
HLS directive DSE for single-die FPGAs ignores per-die resource constraints and die-crossing delays on multi-die FPGAs, while global floorplanning per DSE step is too slow.

## 2. Problem setting
Co-optimization of HLS directives and SLR-level floorplan for large designs mixing dataflow and non-dataflow kernels on multi-die (SSI) FPGAs.

## 3. Search space
Directives (PIPELINE, UNROLL, ARRAY_PARTITION, BIND_STORAGE and parameters) x function-to-slot floorplan assignment; directive space millions-billions, floorplan 4^hundreds

## 4. Evaluation method
Function-level HLS QoR library (Vitis HLS) during DSE; final designs implemented with Vitis on Alveo U250 to measure Fmax; overall execution time = latency x clock period; optimality checked via MILP floorplanning on sampled points

## 5. Benchmarks
Six composite designs: CNN*2+2MM*1, MM*1+COV*2, MTTKRP*2+HEAT*2, MM*2+2MM*2, CNN*3+COV*2, MTTKRP*2+COV*2 (dataflow CNN/MM/MTTKRP from PolySA/AutoSA; 2MM/COV/HEAT from PolyBench)

## 6. Hardware
Xilinx Alveo U250 (floorplanning restricted to lower half, 4 slots on SLR0/SLR1; 65% per-slot resource limit)

## 7. Toolchain
Xilinx Vitis HLS 2020.2; Vitis implementation; AutoBridge min-cut floorplanner for initial floorplan

## 8. Metrics
DSE runtime, latency (cycles), Fmax, overall execution time, max resource utilization per slot

## 9. Baselines
Initial FP -> Iterative DO (one-off AutoBridge MILP floorplan); Iterative (DO + AutoBridge FP) global MILP floorplanning each iteration

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 693X-4925X shorter DSE runtime than DSE with global floorplanning, and 1.16X-8.78X improvement in overall workflow execution time after implementation on Alveo U250; 33.12% smaller latency on average vs iterative DO+AutoBridge FP, average Fmax 290.96 MHz.

## 11. Limitations
Greedy bottleneck-driven, latency-oriented search (not full Pareto); evaluated on 6 synthesized composite benchmarks and restricted to half of U250; relies on per-function QoR library (template reuse); implementation non-determinism affects Fmax.

## 12. What the paper does NOT evaluate
Power/energy, CPU-host interaction, on-board runtime measurement beyond implementation Fmax, cross-benchmark transfer, uncertainty/stability of decisions.

## 13. Relationship to our Studies
- Direct (dimension = YES): S02 S07 S15 S36 S37 S56 S65
- Partial (dimension = PARTIAL): S04 S06 S21 S32 S34 S43 S45 S59 S61 S72 S73 S78 S81 S88 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Multiple dataflow and non-dataflow kernels in one design co-optimized under shared per-die resource constraints. |
| measured interactions | YES | Cross-kernel resource contention per slot, die-crossing timing, and latency bottleneck across functions explicitly modeled. |
| staged evaluation | PARTIAL | Pre-processing HLS QoR library, fast model-based co-search, then implementation of final design. |
| adaptive evidence acquisition | NO | Deterministic greedy search; no adaptive acquisition of new tool evidence. |
| cost/fidelity modeling | PARTIAL | Uses cheap QoR-library lookups and incremental legalization to avoid expensive HLS/MILP calls; runtime compared, no fidelity model. |
| lifecycle/configuration cost | NO | Not considered. |
| physical implementation in the loop | PARTIAL | SLR-level floorplanning and wire pipelining inside the loop; full P&R only for final evaluation. |
| multi-benchmark transfer | NO | Not studied. |
| decision/Pareto stability | PARTIAL | Notes Fmax variance under implementation non-determinism; optimality analysis via MILP legality checks. |
| energy/power | NO | Not reported. |
| CPU-FPGA interaction | NO | Not considered. |
| memory/data movement | PARTIAL | ARRAY_PARTITION/BIND_STORAGE, BRAM/URAM usage and RAM-connected kernels grouped in same slot. |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; measured interactions

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/RipperJ/FADO (stated fully open-sourced in paper)

## Open questions / reviewer notes
Hint mentioned FPGA/TCAD: the conference version is FPGA'23 (recorded here). Journal extension: 'FADO: Floorplan-Aware Directive Optimization Based on Synthesis and Analytical Models for High-Level Synthesis Designs on Multi-Die FPGAs', ACM TRETS 2024, DOI 10.1145/3653458 (author copy https://zhiyaoxie.com/files/TRETS24_FADO.pdf, 'FADO 2.0'), not reviewed here.
