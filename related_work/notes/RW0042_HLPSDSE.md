# RW0042 — Automated Design Space Exploration in High-Level Physical Synthesis

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Metric-guided DSE over floorplan/implementation choices with post-route feedback: HLS-physical co-DSE foundation. Primary Studies: S78 S61. Prior-art boundary: RELEVANT BUT DIFFERENT.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Du, Linfeng; Liang, Jiawei; Lau, Jason; Chi, Yuze; Xie, Yutong; Su, Chunyou; Ahmad, Afzal; He, Zifan; Ke, Jake; Ge, Jinming; Cong, Jason; Zhang, Wei; Guo, Licheng
- Year / venue: 2025 / ICCAD
- DOI: 10.1109/ICCAD66269.2025.11240757 · URL: https://doi.org/10.1109/ICCAD66269.2025.11240757
- Metadata source: PDF first page (IEEE Xplore header with DOI)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/physical/RW0042_Du2025_HLPSDSE_ICCAD.pdf`
- SHA-256: `d0bcec56bd13f64aa64c659062391f70f17f6b39fc393a378ddc3532e79c220d`
- Source: /home/benyamin/Desktop/Library/Automated Design Space Exploration in High-Level Physical Synthesis.pdf

## Code / dataset / artifact provenance
NOT_REPORTED (no framework code URL in the paper; benchmark design repositories are cited)

## 1. Research question
High-Level Physical Synthesis (HLPS) QoR on multi-die FPGAs is unstable because many partitioning, floorplanning and pipelining parameters are chosen ad hoc; small parameter changes can change Fmax by 5x or cause routing failure.

## 2. Problem setting
Large HLS dataflow accelerators implemented on multi-die AMD UltraScale+ and Versal FPGAs via an AutoBridge-based HLPS flow; objective is maximum achievable frequency.

## 3. Search space
HLPS parameters: IP/memory-port binding, device grid (slot) dimensions and abstraction schedule, global and slot-wise max/min resource limits, inter-slot wire capacity per boundary, pipeline density scheme (intra-slot/double/mixed/single), SLL availability ratio per die-crossing bundle.

## 4. Evaluation method
Full Vitis/Vivado place-and-route of every explored solution (post-route Fmax), with up to 4 parallel implementation jobs per batch.

## 5. Benchmarks
Sextans (SpMM), Callipepla (CG solver), MM 10x13 systolic array, Serpens (SpMV), NTT, GPT-2 Medium accelerator

## 6. Hardware
AMD Alveo U55C, U280, U250, Versal VHK158 (implementation only; AMD EPYC 7742 server)

## 7. Toolchain
AMD Vitis/Vivado (version NOT_REPORTED); AutoBridge-based HLPS core; RapidWright

## 8. Metrics
Post-route Fmax (MHz), cumulative DSE time (hours), number of solutions and parallel batches, resource utilization per slot

## 9. Baselines
AMD Vitis (-O3, Explore strategy, frequency sweep), AutoBridge

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: average frequency of 311.06 MHz, 2.42x the Vitis/Vivado toolchain (128.48 MHz) and 1.67x AutoBridge (186.21 MHz).

## 11. Limitations
Heuristic sequential action order without optimality guarantee; single PnR iteration can exceed ten hours so DSE takes days (e.g., up to 325 h cumulative) with limited coverage; design-level HLS partitioning issues (e.g., NTT large module) cannot be fixed by HLPS parameters.

## 12. What the paper does NOT evaluate
HLS pragma/microarchitecture parameters (design is fixed); throughput/latency beyond Fmax; power/energy; learned or multi-fidelity prediction of PnR outcome (partial PnR is mentioned as future work); on-board runtime measurement.

## 13. Relationship to our Studies
- Direct (dimension = YES): S02 S05 S07 S15 S20 S23 S32 S33 S34 S36 S37 S56 S59 S61 S65 S78 S81 S88
- Partial (dimension = PARTIAL): S04 S06 S10 S11 S21 S72 S73 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Whole multi-module accelerator is floorplanned and implemented jointly |
| measured interactions | YES | Physical interactions between modules (congestion, crossings, SLL use) measured from post-route results |
| staged evaluation | YES | FSM of ordered actions; each stage builds on best result of the previous |
| adaptive evidence acquisition | YES | Metrics from prior implementations guide the next parameter choices |
| cost/fidelity modeling | PARTIAL | Wall-clock PnR cost reported and managed with parallel batches; no explicit cost/fidelity model |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Every candidate is placed and routed |
| multi-benchmark transfer | PARTIAL | Six designs on four devices; no learned transfer |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Host interaction not modeled |
| memory/data movement | PARTIAL | HBM/DDR/NoC memory-port binding to relieve congestion; no bandwidth modeling |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; measured interactions; staged evaluation; adaptive evidence acquisition; physical implementation in the loop

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no framework code URL in the paper; benchmark design repositories are cited)

## Open questions / reviewer notes
Authors from RapidStream Design Automation, HKUST, UCLA.
