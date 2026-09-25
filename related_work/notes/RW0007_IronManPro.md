# RW0007 — IronMan-Pro: Multiobjective Design Space Exploration in HLS via Reinforcement Learning and Graph Neural Network-Based Modeling

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_ABSTRACT_ONLY`.

## Bibliographic identity
- Authors: Wu, Nan; Xie, Yuan; Hao, Cong
- Year / venue: 2023 / IEEE TCAD
- DOI: 10.1109/TCAD.2022.3185540 · URL: https://doi.org/10.1109/TCAD.2022.3185540
- Metadata source: IEEE Xplore/ACM DL abstract + OpenAlex (vol. 42, no. 3, pp. 900-913) + dblp key journals/tcad/WuXH23 + Sharc Lab publications page

## PDF provenance
- Status: `METADATA_ONLY_PAYWALLED` (no PDF)
- Canonical path: `none`
- SHA-256: `none`
- Source: none

## Code / dataset / artifact provenance
Code: https://github.com/lydiawunan/IronMan (also linked as https://github.com/sharc-lab/IronMan)

## 1. Research question
HLS abstractions hide optimization opportunities, actual RTL quality is hard to predict, and HLS tools do not provide Pareto trade-offs among objectives/constraints.

## 2. Problem setting
Automated multi-objective HLS DSE producing either constraint-satisfying directive solutions or Pareto trade-offs among resource types, area and latency.

## 3. Search space
HLS directives / resource allocation strategies (per abstract: 'optimal resource allocation strategies' and 'optimized HLS directives'); exact directive set NOT_REPORTED in abstract

## 4. Evaluation method
GNN predictions trained against actual RTL/implementation-level results (resource utilization and critical-path timing) per abstract; exact tool flow NOT_REPORTED in abstract

## 5. Benchmarks
NOT_REPORTED (abstract only)

## 6. Hardware
NOT_REPORTED (abstract only)

## 7. Toolchain
NOT_REPORTED (abstract only)

## 8. Metrics
Prediction error for resource utilization and CP timing; resource utilization and CP timing of solutions; constraint-satisfaction rate; DSE speedup

## 9. Baselines
Meta-heuristic-based techniques (specifics NOT_REPORTED in abstract); HLS tool estimates for prediction

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: GPP reduces HLS-tool prediction error by 10.9x (resource) and 5.7x (CP timing); vs meta-heuristics improves resource utilization by 16.0%-29.5% and CP timing by 7.6%-16.5%; under user constraints finds satisfying solutions in over 96% of cases, more than twice meta-heuristics, with speedup up to 400x.

## 11. Limitations
Full text not reviewed; limitations cannot be assessed beyond abstract. Predictor-driven DSE depends on GNN accuracy/generalization.

## 12. What the paper does NOT evaluate
From abstract: no mention of power/energy, multi-kernel joint evaluation, CPU-FPGA interaction, fidelity-cost modeling, or on-board measurement.

## 13. Relationship to our Studies
- Direct (dimension = YES): none
- Partial (dimension = PARTIAL): S04 S06 S21 S59 S61 S71 S72 S78 S81

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract only. |
| measured interactions | NOT_REPORTED | Abstract only. |
| staged evaluation | NOT_REPORTED | Abstract only. |
| adaptive evidence acquisition | NOT_REPORTED | RL explores design space, but no evidence-acquisition policy described in abstract. |
| cost/fidelity modeling | PARTIAL | GNN predictor substitutes for HLS-tool estimates of post-RTL resource/timing; no explicit fidelity-cost model in abstract. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract only. |
| physical implementation in the loop | PARTIAL | Predicts actual RTL resource utilization and critical-path timing (ground truth from downstream flow); per-candidate P&R in loop not stated. |
| multi-benchmark transfer | NOT_REPORTED | Abstract only. |
| decision/Pareto stability | NOT_REPORTED | Abstract only. |
| energy/power | NOT_REPORTED | Objectives listed are resource types, area, latency, CP timing; power not mentioned. |
| CPU-FPGA interaction | NOT_REPORTED | Abstract only. |
| memory/data movement | NOT_REPORTED | Abstract only. |

## 14. Possible overlap
POTENTIAL OVERLAP (partial evidence) on: cost/fidelity modeling; physical implementation in the loop

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/lydiawunan/IronMan (also linked as https://github.com/sharc-lab/IronMan)

## Open questions / reviewer notes
Published title uses 'Multiobjective' and 'Network-Based Modeling' (hint title is the author-page wording). Early access June 2022; issue vol. 42 no. 3 (2023). No legitimate open-access PDF found (OpenAlex: closed; Sharc Lab page links only to IEEE Xplore). Predecessor: 'IronMan: GNN-assisted Design Space Exploration in High-Level Synthesis via Reinforcement Learning', GLSVLSI 2021 (arXiv:2102.08138) is a different, open-access paper and was NOT substituted.
