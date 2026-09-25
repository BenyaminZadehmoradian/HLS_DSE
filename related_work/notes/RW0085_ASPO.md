# RW0085 — ASPO: Constraint-Aware Bayesian Optimization for FPGA-based Soft Processors

> **Relevance (2026-09-25 full-text review): SUPPORTING** — Constrained Bayesian optimisation for FPGA soft-processor parameters that puts evaluation cost into the acquisition (EI divided by a checkpoint-distance cost proxy) and reuses Vivado incremental-synthesis checkpoints: methodological precedent for cost-aware acquisition in S99 and history-dependent evaluation cost in S85/S86. Not CORE: soft-processor microarchitecture, single fidelity, no local-vs-joint evidence choice. Primary Studies: S99 S85 S86 S72. Prior-art boundary: METHOD FOUNDATIONAL.
> **Identity:** Authors: Haoran Wu, Ce Guo, Wayne Luk, Robert Mullins (Cambridge / Imperial College London). arXiv 2506.06817v1 (7 Jun 2025), blind-review preprint, no venue. The 74% saving is vs BOOM-Explorer (Table VI), not Boomerang as the abstract states.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Wu, Haoran; Guo, Ce; Luk, Wayne; Mullins, Robert
- Year / venue: 2025 / arXiv 2506.06817
- DOI: none recorded · URL: https://arxiv.org/abs/2506.06817

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: arxiv v1 (blind-review preprint)
- Canonical path: `related_work/papers/bo_mobo/RW0085_Wu2025_ASPO_arXiv.pdf` (local only, gitignored)
- SHA-256: `581779260504346b983bda44c0d89dd30c49c5f881f9948ce4976c9d33082cce`
- Source: https://arxiv.org/pdf/2506.06817

## Code provenance
NOT_REPORTED (web address removed for blind review)

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Soft-processor tuning has categorical parameters, Boolean inter-parameter constraints and slow synthesis-based evaluation; standard BO proposes invalid designs and wastes synthesis time.

## 2. Problem setting / 3. Search space / 4. Evaluation method
One-hot categorical encoding with a customised GP kernel (argmax mapping, as RCBO); constraints as smooth functions (linear, interval conditionals via min/max, divisibility via -sin^2); synthesis-checkpoint database with a weighted-Euclidean matcher (weights fitted to minimise incremental-synthesis time); orthogonal-array warm start; acquisition alpha(x,t) = EI(x) / (lambda(t) * c_hat(x)) with c_hat = min weighted distance to the checkpoint database and lambda(t) = lambda0*exp(-k t).

## 5. Benchmarks
RocketChip, BOOM, EL2 VeeR x 7 RISC-V workloads (coremark, dhrystone, rsort, qsort, multiply, spmv, mm) = 21 tasks.

## 6. Hardware
Zynq UltraScale+ XCZU3CG (EL2 VeeR), XCZU6CG (BOOM); RocketChip target NOT_REPORTED; synthesis only at 50 MHz; no on-board runs.

## 7. Toolchain
Vivado synthesis with incremental checkpoints (version NOT_REPORTED); Verilator; GP-based BO (library NOT_REPORTED).

## 8. Metrics
Evaluation time per configuration; Total Design Time (TDT, capped at 35 h); Invalid Design Rate; Estimated Execution Time (cycles / Fmax from synthesis slack).

## 9. Baselines
Direct evaluation; fixed default checkpoint; Hill Climbing, Vanilla BO, BOOM-Explorer, RCBO, default configuration.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: Table V mean evaluation time direct vs fixed-checkpoint vs ASPO: EL2 VeeR 11.4 / 10.4 / 9.1 min (20.2% saving); RocketChip 45.4 / 37.7 / 33.1 min (27.1%); BOOM 81.2 / 65.2 / 54.1 min (33.4%). Table VI: BOOM spmv TDT 9.12 h vs RCBO 27.96 h, BOOM-Explorer 35.00 h (cap), VBO 28.15 h. Table VII: best EET on 17 of 21 tasks; BOOM multiply 0.70 vs 1.07 ms default (-34.6%).

## 11. Limitations
AUTHOR-STATED: single objective; PPA multi-objective future work. REVIEWER: as written, Eq. 9's lambda(t) is identical for all candidates at iteration t, so the cooling does not change the argmax; the cost proxy is never validated against measured synthesis time; Table V uses 10 configurations with a pre-populated database (inflates savings); Fmax from synthesis-only slack (no P&R, no seed noise); single trajectories, no confidence intervals; RocketChip 'mm' row in Table VI duplicates BOOM 'mm' baseline values; abstract credits 74% to 'Boomerang' while experiments compare BOOM-Explorer; TDT cap truncates baselines.

## 12. What the paper does NOT evaluate
HLS pragma spaces; place-and-route; seed noise; multi-fidelity; measured-cost models; multi-objective fronts; joint evaluation; on-board execution; ablation of the cost term.

## 13. Relationship to our Studies (S99 S85 S86 S72)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | one soft processor per optimisation |
| measured interactions | NO | interdependence encoded as constraints only |
| staged evaluation | NO | single evaluation stage |
| adaptive evidence acquisition | YES | cost-aware EI divided by lambda(t)*c_hat(x) plus constraint-aware optimisation (cooling ineffective as written) |
| cost/fidelity modeling | PARTIAL | distance-proxy cost model, not validated; no fidelity levels |
| lifecycle/configuration cost | PARTIAL | checkpoint database growth/reuse as build-cost lifecycle |
| physical implementation in the loop | PARTIAL | Vivado synthesis in the loop, no P&R |
| multi-benchmark transfer | PARTIAL | 3 processors x 7 workloads optimised independently |
| decision/Pareto stability | NOT_REPORTED |  |
| energy/power | PARTIAL | power from synthesis reports, not optimised |
| CPU-FPGA interaction | NO |  |
| memory/data movement | PARTIAL | cache sizes as parameters; data movement not measured |

## 14. Possible overlap
METHOD FOUNDATIONAL

## 15. Possible research gap (not a novelty claim)
S99 should include cost-aware EI (EI / predicted cost) as a named baseline citing ASPO and Lee et al., but use measured or predicted cost rather than a parameter-distance proxy, and avoid ASPO's multiplicative cooling. Checkpoint reuse (20-33% per-evaluation savings) implies S85/S86 cost models should treat evaluation cost as history-dependent. Not prior art for the S97/S99 local-vs-joint claim.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED (web address removed for blind review).
