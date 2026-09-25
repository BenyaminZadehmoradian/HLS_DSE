# RW0081 — Correlated Multi-objective Multi-fidelity Optimization for HLS Directives Design

> **Relevance (2026-09-25 full-text review): CORE** — HLS DSE with adaptive evidence selection across fidelities (Vivado hls/syn/impl) under a budget with a multi-objective Pareto target: contribution boundary (b). No multi-kernel or joint co-resident evaluation, so prior art for stage selection but not for local-vs-joint composition. Primary Studies: S99 S98 S72 S04. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** TODAES 27(4) Art. 31, March 2022, doi 10.1145/3503540. Authors Qi Sun, Tinghuan Chen, Siting Liu, Jianli Chen, Hao Yu, Bei Yu (Jin Miao, on the DATE 2021 version RW0006, is not listed). Additions over DATE: deep-kernel DCGP, MES ablation, running-time ablation.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Sun, Qi; Chen, Tinghuan; Liu, Siting; Chen, Jianli; Yu, Hao; Yu, Bei
- Year / venue: 2022 / ACM TODAES 27(4) Art. 31 (March 2022)
- DOI: 10.1145/3503540 · URL: https://www.cse.cuhk.edu.hk/~byu/papers/J63-TODAES2022-MultiFidelity.pdf

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: accepted (author site)
- Canonical path: `related_work/papers/core/RW0081_Sun2022_CMMFOJ_TODAES_accepted.pdf` (local only, gitignored)
- SHA-256: `2cc0a2713ce89e19e2735973660bdb54beec47521fe9427f0a38c91df47f896a`
- Source: https://www.cse.cuhk.edu.hk/~byu/papers/J63-TODAES2022-MultiFidelity.pdf

## Code provenance
NOT_REPORTED

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Find the Pareto set of HLS directive configurations (power, delay, LUT) using cheaper but less accurate post-HLS and post-synthesis reports relative to post-implementation.

## 2. Problem setting / 3. Search space / 4. Evaluation method
Tree-based pruning of directive spaces; non-linear multi-fidelity GP f_{i+1}(x) = z(f_i(x), x) + f_e(x) (lower-stage outputs appended to next-stage inputs); correlated multi-objective GP (coregionalization, ARD Matern-5/2); DCGP deep-kernel variant (FC 1000-500-50-6). Acquisition (Eqs. 11-12, 15): EIPV_i penalized as PEIPV_i = (T_impl/T_i) EIPV_i; per-stage argmax, then (x*, h) = argmax over stages; the tool runs up to stage h, so one evaluation yields all three objectives at every stage <= h. Invalid designs set to 10x the current worst. Early stop after 5 steps without hypervolume improvement. Final Pareto set from impl-stage samples. No resource-fit constraint.

## 5. Benchmarks
MachSuite GEMM, SORT_RADIX, SPMV_ELLPACK, SPMV_CRS, STENCIL3D; iSmart2 DNN as a single design; each optimized alone.

## 6. Hardware
Xilinx Virtex-7 VC707.

## 7. Toolchain
Vivado 2018.2 (HLS, synthesis, implementation); BoTorch/GPyTorch for DCGP.

## 8. Metrics
ADRS against the exhaustively computed true Pareto set (normalized to ANN); ADRS std over 10 runs; overall running time (algorithm + tool hours).

## 9. Baselines
FPL18 (Lo & Chow), DAC19, ANN, boosting tree; MES acquisition ablation; CGP (DATE 2021 version).

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: Table 1 normalized ADRS (ANN = 1.00): DCGP 0.34, CGP 0.39, FPL18 0.51, BT 0.96, DAC19 1.05; best DCGP 0.11 on SPMV_ELLPACK; DCGP beats CGP by 12.8% average (up to 42.1%). Table 3: MES acquisition 0.45 vs 0.34. Table 2 average overall hours: DCGP 30.08, CGP 33.88, FPL18 47.21, ANN 63.12, BT 63.33, DAC19 440.64. 8 initial + at most 40 steps, 10 runs. Absolute ADRS NOT_REPORTED.

## 11. Limitations
AUTHOR-STATED: very large spaces handled by sampling (untested). REVIEWER: ADRS only normalized to ANN; ADRS distance function unspecified; FPGA time computed as average per-design time x runs, not measured; 10x-worst penalty distorts the GP; no device-fit constraint; each stage's EIPV measures improvement of that stage's own front, and T_impl/T_i favours cheap stages; 8 + 40 evaluations, 10 runs; no code.

## 12. What the paper does NOT evaluate
Multi-kernel/co-resident joint designs; inter-kernel interaction; resource-feasibility constraints; implementation seed variability; on-board or energy measurement; transfer.

## 13. Relationship to our Studies (S99 S98 S72 S04)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | each benchmark alone; iSmart2 monolithic |
| measured interactions | NO | correlation between objectives and stages, not kernels |
| staged evaluation | YES | hls/syn/impl stages, run up to a selected stage h |
| adaptive evidence acquisition | YES | per-stage cost-penalized EIPV, argmax over (x, stage) |
| cost/fidelity modeling | YES | rho_i = T_impl/T_i and non-linear multi-fidelity GP |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | YES | Vivado implementation reports at the impl stage on VC707 |
| multi-benchmark transfer | NO |  |
| decision/Pareto stability | PARTIAL | ADRS std over 10 runs; hypervolume-stagnation stop |
| energy/power | PARTIAL | tool-reported power objective |
| CPU-FPGA interaction | NO |  |
| memory/data movement | PARTIAL | array partitioning and BRAM usage |

## 14. Possible overlap
PARTIAL OVERLAP

## 15. Possible research gap (not a novelty claim)
Prior art for stage-selective HLS evidence acquisition: S99 must not claim hls/syn/impl selection as new; the new element must be local-vs-joint evidence across co-resident kernels. A naive local-source EIPV would measure improvement of the local front rather than the target front, which S99 must avoid. The nested-observation idea carries over (a joint post-route run also yields per-kernel hierarchical utilization). Its exhaustive-ground-truth ADRS protocol matches S04; reimplementation needed as an S72 baseline.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED.
