# RW0039 — TAPA: A Scalable Task-parallel Dataflow Programming Framework for Modern FPGAs with Co-optimization of HLS and Physical Design

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Guo, Licheng; Chi, Yuze; Lau, Jason; Song, Linghao; Tian, Xingyu; Khatti, Moazin; Qiao, Weikang; Wang, Jie; Ustun, Ecenur; Fang, Zhenman; Zhang, Zhiru; Cong, Jason
- Year / venue: 2023 / ACM TRETS
- DOI: 10.1145/3609335 · URL: https://doi.org/10.1145/3609335
- Metadata source: PDF first page (ACM reference: ACM Trans. Reconfig. Technol. Syst. 16(4), Article 63, Dec 2023)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/physical/RW0039_Guo2023_TAPA_TRETS.pdf`
- SHA-256: `4c527f953fc0bdc8abf7d0e1c335eabe632f91165daf90241eb08469210037c6`
- Source: /home/benyamin/Desktop/Library/TAPA: A Scalable Task-parallel Dataflow Programming Framework for Modern FPGAs with Co-optimization of HLS and Physical Design.pdf

## Code / dataset / artifact provenance
Code: https://github.com/UCLA-VAST/tapa ; floorplanner: https://github.com/UCLA-VAST/AutoBridge ; design checkpoints in repository

## 1. Research question
Large task-parallel HLS designs on multi-die and HBM FPGAs fail timing closure or routing because HLS cannot foresee physical layout, and existing HLS APIs make complex inter-task communication hard to express.

## 2. Problem setting
Compiling C++ task-parallel dataflow programs (tasks communicating via streams) to high-frequency accelerators on multi-die AMD FPGAs (U250 with DDR, U280 with HBM).

## 3. Search space
Coarse-grained floorplan (task-to-slot assignment under per-slot resource ratios), inter-slot pipelining with latency balancing, HBM channel binding; sweep of utilization-ratio parameter to generate multiple floorplans

## 4. Evaluation method
Full Vivado implementation (placement and routing) at 300 MHz target; correctness via cycle-accurate simulation and on-board execution.

## 5. Benchmarks
43 designs from SODA stencils, Minimap2 genome sequencing, PolySA CNN, HBM PageRank graph processing, HBM bucket sort, AutoSA Gaussian elimination; plus SASA stencils, Sextans SpMM, Serpens SpMV HBM designs

## 6. Hardware
AMD/Xilinx Alveo U250 and U280

## 7. Toolchain
Vitis HLS, Vivado, Vitis 2021.2; Python MIP + Gurobi

## 8. Metrics
Post-route Fmax, routability, resource utilization, throughput/cycles, floorplanning compile time

## 9. Baselines
Default AMD Vitis/Vivado flow; ablations (pipelining only, floorplanning only, different slot grids)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: across 43 designs, average frequency improves from 147 MHz to 297 MHz (102%) with no loss of throughput and negligible resource change; 16 originally unroutable designs reach 274 MHz on average; floorplanning of a 493-module CNN takes ~20 s.

## 11. Limitations
Users must partition applications into suitably sized tasks (no task-level optimization); tasks larger than a slot unsupported; stream-only inter-task communication; effective up to ~75% resource usage; long compile time (RapidStream integration future work).

## 12. What the paper does NOT evaluate
HLS pragma/microarchitecture DSE within tasks; power; learned QoR prediction; runtime reconfiguration.

## 13. Relationship to our Studies
- Direct (dimension = YES): S07 S15 S59 S61 S65 S73 S78 S81
- Partial (dimension = PARTIAL): S02 S04 S06 S10 S11 S21 S32 S34 S36 S37 S56 S72 S83 S84 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | All tasks of the dataflow design floorplanned and pipelined jointly |
| measured interactions | PARTIAL | Inter-task wire crossings and latency balancing modeled; congestion observed post-route |
| staged evaluation | PARTIAL | HLS estimates drive floorplan, then full implementation |
| adaptive evidence acquisition | NO | No feedback loop (floorplan sweep in parallel) |
| cost/fidelity modeling | PARTIAL | ILP cost (crossings, resources); compile time reported |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | All results post place-and-route |
| multi-benchmark transfer | PARTIAL | Many topologies on two devices |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | PARTIAL | Integrates with Vitis host infrastructure; not evaluated |
| memory/data movement | YES | HBM/DDR channel binding and memory interface optimizations |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; physical implementation in the loop; memory/data movement

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/UCLA-VAST/tapa ; floorplanner: https://github.com/UCLA-VAST/AutoBridge ; design checkpoints in repository

## Open questions / reviewer notes
Journal extension of AutoBridge (FPGA'21) and TAPA (FCCM'21).
