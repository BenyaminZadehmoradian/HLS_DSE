# RW0080 — FADO: Floorplan-Aware Directive Optimization Based on Synthesis and Analytical Models for High-Level Synthesis Designs on Multi-Die FPGAs

> **Relevance (2026-09-25 full-text review): CORE** — Co-optimizes HLS directives of 175-350 functions from multiple co-resident dataflow and non-dataflow kernels under shared per-slot resource and die-crossing constraints on one FPGA and implements the final designs: boundary (a). Its evidence shows composed per-function QoR does not guarantee implementability or timing (slot caps tightened; placement/routing failures in Table 6), but it never quantifies the joint-vs-composed residual or reasons about which evidence to buy. Primary Studies: S97 S98 S81 S72. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** Full title 'FADO: Floorplan-Aware Directive Optimization Based on Synthesis and Analytical Models for High-Level Synthesis Designs on Multi-Die FPGAs', ACM TRETS 2024, DOI 10.1145/3653458. Authors: Linfeng Du, Tingyuan Liang, Xiaofeng Zhou, Jinming Ge, Shangkun Li, Sharad Sinha, Jieru Zhao, Zhiyao Xie, Wei Zhang.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Du, Linfeng; Liang, Tingyuan; Zhou, Xiaofeng; Ge, Jinming; Li, Shangkun; Sinha, Sharad; Zhao, Jieru; Xie, Zhiyao; Zhang, Wei
- Year / venue: 2024 / ACM TRETS
- DOI: 10.1145/3653458 · URL: https://doi.org/10.1145/3653458

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: accepted (author site)
- Canonical path: `related_work/papers/core/RW0080_Du2024_FADO2_TRETS_accepted.pdf` (local only, gitignored)
- SHA-256: `1b11908a72617845f923a0a62e183a64c93e0652430f59b63a46ade6efc63107`
- Source: https://zhiyaoxie.com/files/TRETS24_FADO.pdf

## Code provenance
https://github.com/RipperJ/FADO

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Co-optimize HLS directives and SLR-level floorplans for large designs on multi-die FPGAs to minimize execution time (cycles / Fmax) under per-slot resource, RAM-grouping and SLL constraints without repeated global ILP floorplanning.

## 2. Problem setting / 3. Search space / 4. Evaluation method
Multi-choice multi-dimensional bin-packing formulation. FADO 1.0: per-function QoR library from HLS reports of sampled configurations, latency-bottleneck-guided greedy search, incremental floorplanning (online worst-fit, offline best-fit-decreasing, look-ahead/look-back), incremental pipelining of die-crossing wires. FADO 2.0: calibrated COMBA-based analytical QoR model on LLVM IR, loop-tree-ordered directive search, BRAM/URAM/LUTRAM balancing. Final directives re-synthesized and implemented with AutoBridge floorplans. COMPOSITION OPERATOR: design latency = SUM over kernels along the longest path, dataflow kernel = MAX of sub-function latencies (Eq. 2); per-slot resource = SUM of per-function resources (Eq. 5); utilization = MAX normalized ratio.

## 5. Benchmarks
Six mixed benchmarks with 175-350 functions (CNN*2+2MM*1, MM*1+COV*2, MTTKRP*2+HEAT*2, MM*2+2MM*2, CNN*3+COV*2, MTTKRP*2+COV*2) from PolySA/AutoSA and PolyBench; ~1000 random configurations for model rank validation.

## 6. Hardware
AMD/Xilinx Alveo U250 lower half (4 slots).

## 7. Toolchain
Vitis HLS 2020.2, Vitis implementation, AutoBridge, COMBA-derived analytical model, LLVM passes.

## 8. Metrics
Max utilization ratio, DSE runtime, latency (kilo-cycles), post-implementation Fmax, execution time = cycles/Fmax, model speedup, Spearman/Kendall rank correlation.

## 9. Baselines
Directive-free and directive-rich originals (with/without AutoBridge), iterative synthesis-based and analytical directive optimization with ILP floorplanning, FADO 1.0 vs 2.0.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: FADO 1.0: 693x-4925x search speedup, 1.16x-8.78x better execution time than the best synthesis-based baseline, 33.12% lower latency, average Fmax 290.96 MHz. FADO 2.0: 2.66x better execution time than iterative analytical DO + AutoBridge, 1.40x over FADO 1.0 on average (excluding a 19.83x outlier), 9.18% higher Fmax (Table 6). Analytical model 231.84x/208.80x faster than Vitis HLS; latency rank Spearman 0.9137, Kendall 0.7732. Table 6 records implementation failures for several floorplan-unaware or ILP-floorplan configurations; Sec. 6.1: a 70% slot limit still caused placement/routing failures, tightened to 65% (FADO 1.0); FADO 2.0 used 80% because model LUTs are over-predicted.

## 11. Limitations
AUTHOR-STATED: FADO 1.0 sampling can prune effective configurations; 2-cycle latency errors can reverse search order; LUT over-prediction; FF dropped from constraints; Fmax varies with non-deterministic implementation; oversized design points break the offline stage. REVIEWER: additive/max composition with a heuristic slot cap standing in for congestion/timing; composed per-function predictions never compared quantitatively with whole-design post-route results; one implementation run per method, so ~9% Fmax differences are within unquantified noise; multi-die U250 differs from small single-die devices.

## 12. What the paper does NOT evaluate
Per-design residual between composed and whole-design QoR; repeated-seed variance; Pareto fronts; energy; host interaction and DDR contention; budgeted choice of when to implement; single-die devices.

## 13. Relationship to our Studies (S97 S98 S81 S72)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | directives for all kernels co-selected under shared per-slot constraints; whole design synthesized and implemented |
| measured interactions | PARTIAL | resource/die-crossing coupling modelled; failures and cap tightening show non-compositional effects; no residual measured |
| staged evaluation | PARTIAL | library/model-driven search, then one fixed final implementation |
| adaptive evidence acquisition | NO | greedy bottleneck-guided search |
| cost/fidelity modeling | PARTIAL | library vs analytical model trade-off (208-232x speed, rank 0.91) |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | YES | SLR floorplan in the loop; post-implementation Fmax on U250 |
| multi-benchmark transfer | PARTIAL | model calibrated once and reused |
| decision/Pareto stability | NO | Fmax non-determinism acknowledged, not quantified |
| energy/power | NO |  |
| CPU-FPGA interaction | NO |  |
| memory/data movement | PARTIAL | on-chip RAM binding balance; no DDR interference |

## 14. Possible overlap
PARTIAL OVERLAP

## 15. Possible research gap (not a novelty claim)
S98: clearest published evidence that summed per-function HLS QoR does not predict whole-design post-route feasibility/timing (70% -> 65% slot cap, placement exceptions), but the residual is never measured — S98 quantifies what FADO works around heuristically (U250, not xc7z020). S81: single-run ~9% Fmax comparisons motivate reporting implementation variance. S99: FADO buys joint evidence once at the end; a decision-driven local/joint policy is not prior art here.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/RipperJ/FADO.
