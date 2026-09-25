# RW0013 — Constrained Multi-objective Bayesian Optimization through Optimistic Constraints Estimation

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Li, Diantong; Zhang, Fengxue; Liu, Chong; Chen, Yuxin
- Year / venue: 2025 / AISTATS 2025 (PMLR 258)
- DOI: NOT_REPORTED · URL: https://proceedings.mlr.press/v258/li25a.html
- Metadata source: PDF first page (PMLR camera-ready) + PMLR landing page; arXiv:2411.03641

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (published)
- Canonical path: `related_work/papers/bo_mobo/RW0013_Li2025_CMOBOOCE_AISTATS.pdf`
- SHA-256: `ea366cbae1c5ec14fc7a9b6a991e710c42898914cd5cd52e0fefe20f61f340f0`
- Source: https://raw.githubusercontent.com/mlresearch/v258/main/assets/li25a/li25a.pdf

## Code / dataset / artifact provenance
Code: https://github.com/dancewithDianTong/COMBOO (linked from PMLR page); OpenReview: https://openreview.net/forum?id=BErNKnkpDn

## 1. Research question
Sample-efficient multi-objective BO when both objectives and constraints are unknown black-box functions, with theoretical guarantees that existing heuristic/approximate constrained MOBO methods lack.

## 2. Problem setting
Maximize multiple unknown objectives subject to multiple unknown black-box constraints (thresholds), with sequential (q=1) noisy queries.

## 3. Search space
Continuous low-dimensional inputs (d=2-7) and discrete molecule sets (Caco-2++ d=2175 features over 906 molecules; ESOL+ d=2133)

## 4. Evaluation method
Synthetic test functions and real-world problem simulators/datasets; 10 independent trials per method.

## 5. Benchmarks
Toy function (d=2,m=2,c=2); Branin-Currin (d=2,m=2,c=2); C2-DTLZ2 (d=4,m=2,c=1); Penicillin (d=7,m=3,c=3); Disc Brake Design (d=4,m=2,c=3); Caco-2++ (drug discovery, TDC); ESOL+

## 6. Hardware
NOT_APPLICABLE

## 7. Toolchain
Python, BoTorch (baselines except MESMOC); versions NOT_REPORTED

## 8. Metrics
Simple/cumulative hypervolume regret, cumulative constraint violation, combined constraint regret C_t, observed best hypervolume

## 9. Baselines
qNEHVI, qParEGO, MESMOC, Random Search; unconstrained qNEHVI

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: first constrained MOBO with guarantees similar to constrained single-objective algorithms (sample efficiency and infeasibility declaration); empirically COMBOO 'displayed a consistently strong performance, often aligning with the top-performing methods' and is comparable to all baselines in constraint regret on real-world problems.

## 11. Limitations
Theory relies on discretized domain (claimed not fundamental); sequential q=1 comparison; qNEHVI converges faster on small-scale test functions; small problem dimensions for continuous cases.

## 12. What the paper does NOT evaluate
No hardware/HLS design spaces, no multi-fidelity or evaluation-cost modeling, no staged evaluation, no physical implementation, energy, or CPU-FPGA/memory aspects.

## 13. Relationship to our Studies
- Direct (dimension = YES): none
- Partial (dimension = PARTIAL): S05 S20 S23 S33 S72

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Single monolithic black box. |
| measured interactions | NOT_APPLICABLE | Not addressed. |
| staged evaluation | NO | Single-stage evaluation of all objectives/constraints. |
| adaptive evidence acquisition | PARTIAL | Acquisition balances constraint level-set learning with MO optimization; no choice among evidence sources. |
| cost/fidelity modeling | NO | Uniform query cost assumed. |
| lifecycle/configuration cost | NOT_APPLICABLE | Not addressed. |
| physical implementation in the loop | NOT_APPLICABLE | No hardware. |
| multi-benchmark transfer | NO | Independent runs per problem; no transfer. |
| decision/Pareto stability | NO | Hypervolume/violation reported, not stability of chosen Pareto set. |
| energy/power | NOT_APPLICABLE | No hardware. |
| CPU-FPGA interaction | NOT_APPLICABLE | No hardware. |
| memory/data movement | NOT_APPLICABLE | No hardware. |

## 14. Possible overlap
POTENTIAL OVERLAP (partial evidence) on: adaptive evidence acquisition

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: staged evaluation; decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/dancewithDianTong/COMBOO (linked from PMLR page); OpenReview: https://openreview.net/forum?id=BErNKnkpDn

## Open questions / reviewer notes
Algorithm acronym is COMBOO (paper also says CMOBO for the problem class). PMLR has no DOI. arXiv version 2411.03641 also exists.
