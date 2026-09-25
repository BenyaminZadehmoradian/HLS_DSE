# RW0040 — RapidStream IR: Infrastructure for FPGA High-Level Physical Synthesis

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Lau, Jason; Xiao, Yuanlong; Xie, Yutong; Chi, Yuze; Song, Linghao; Xiang, Shaojie; Lo, Michael; Zhang, Zhiru; Cong, Jason; Guo, Licheng
- Year / venue: 2024 / ICCAD
- DOI: 10.1145/3676536.3676649 · URL: https://doi.org/10.1145/3676536.3676649
- Metadata source: PDF first page (ACM reference format, ICCAD '24)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/physical/RW0040_Lau2024_RapidStreamIR_ICCAD.pdf`
- SHA-256: `af17ea282c55cb76ee37ee66b5ccdfc1617075be284efd85bc11c22dd351d6f1`
- Source: /home/benyamin/Desktop/Library/RapidStream IR: Infrastructure for FPGA High-Level Physical Synthesis.pdf

## Code / dataset / artifact provenance
Free for academic researchers at https://rapidstream-da.com

## 1. Research question
Existing high-level physical synthesis (HLPS) tools (e.g., AutoBridge) only pipeline top-level dataflow functions, cannot integrate RTL and vendor IP, are tied to specific devices, and lack an extensible infrastructure for new physical optimizations.

## 2. Problem setting
Frequency optimization of large mixed-source (HLS, RTL, IP) FPGA designs on multi-die AMD UltraScale+ and Versal devices via partitioning, floorplanning and pipelining at arbitrary hierarchy levels.

## 3. Search space
Module partitioning/grouping, coarse-grained floorplan (module-to-slot assignment under per-slot resource limits), pipeline insertion; case study sweeps max slot utilization to trade wirelength vs local congestion

## 4. Evaluation method
Vivado 2023.2 place-and-route frequency on multiple devices; synthesis wall time for parallel synthesis plugin; format-ingestion tests.

## 5. Benchmarks
AutoSA CNN systolic arrays, LLaMA2 LLM accelerator (HLS+IP+RTL), Minimap2 genome accelerator, KNN accelerator; ingestion tests on 29 Dynamatic examples, a Catapult HLS sparse accelerator, 12 CHStone Intel HLS benchmarks

## 6. Hardware
AMD Alveo U250, U280, Versal VHK158, VP1552 and other devices (six FPGAs in LLaMA2 porting)

## 7. Toolchain
Vivado 2023.2; COIN-OR ILP solver (400 s limit); Dynamatic 2.0, Catapult HLS 2021.1, Intel FPGA HLS 19.4.0 for input RTL

## 8. Metrics
Post-route frequency, resource utilization change, synthesis wall time, lines of code for plugins

## 9. Baselines
Vivado default flow, AutoBridge, manual optimization (Chen et al. LLaMA2)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: improves frequency of mixed-source designs by 7% to 62% (30%-62% when porting LLaMA2 across devices, average 244 MHz), comparable to manual optimization on U280 (243 vs 245 MHz), 306 MHz after refactoring; parallel synthesis plugin gives 2.49x average synthesis wall-time speedup; some unroutable designs reach ~300 MHz.

## 11. Limitations
Floorplan exploration is a parameter sweep rather than automated DSE; relies on vendor tools for implementation; some designs need refactoring into smaller pipelinable parts; infrastructure distributed via company site.

## 12. What the paper does NOT evaluate
HLS pragma DSE; power; throughput effects beyond frequency; automated metric-guided parameter tuning (addressed by later HLPS DSE work).

## 13. Relationship to our Studies
- Direct (dimension = YES): S07 S15 S59 S61 S65 S78 S81
- Partial (dimension = PARTIAL): S02 S04 S06 S10 S11 S21 S32 S34 S36 S37 S56 S72 S73 S83 S84 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Entire hierarchical design partitioned and floorplanned jointly |
| measured interactions | PARTIAL | Trade-off between local congestion and global wirelength measured in floorplan sweep |
| staged evaluation | PARTIAL | Pass pipeline: communication analysis, partitioning, floorplanning, interconnect synthesis |
| adaptive evidence acquisition | NO | No adaptive feedback loop |
| cost/fidelity modeling | PARTIAL | ILP cost on crossings/resources |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Post-route frequencies reported |
| multi-benchmark transfer | PARTIAL | Ported across six devices and multiple input formats |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | PARTIAL | Ingests Vitis XO kernels for platform integration |
| memory/data movement | PARTIAL | Handles memory/IP interfaces as interconnect protocols |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; physical implementation in the loop

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Free for academic researchers at https://rapidstream-da.com

## Open questions / reviewer notes
Co-first authors Lau and Xiao; authors affiliated with RapidStream Design Automation, UCLA, Cornell.
