# RW0066 — Multi-Information Source Optimization

> **Relevance (2026-09-25 full-text review): SUPPORTING** — No HLS/FPGA work, so not CORE. Supplies the model and acquisition S99 would build on: one GP over (source, x) with f(l,x) = f(0,x) + delta_l(x) and a cost-normalized knowledge gradient choosing both design and information source. The additive discrepancy lines up with the S98 residual if joint evaluation is IS0 (truth) and composed-local a biased source. Primary Studies: S99 S98. Prior-art boundary: METHOD FOUNDATIONAL.
> **Identity:** Reviewed text is arXiv:1603.00389v2 (15 Nov 2016), not the NeurIPS 2017 proceedings version; numbers may differ from the camera-ready.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Poloczek, Matthias; Wang, Jialei; Frazier, Peter I.
- Year / venue: 2017 / NeurIPS 2017
- DOI: none recorded · URL: https://arxiv.org/abs/1603.00389

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: arxiv (v2, Nov 2016)
- Canonical path: `related_work/papers/bo_mobo/RW0066_Poloczek2017_MISO_NeurIPS_arxiv.pdf` (local only, gitignored)
- SHA-256: `e6c593a32b4effafb10483c1227b68c42a68765388907b4ff4b102bfb41c063f`
- Source: https://arxiv.org/pdf/1603.00389

## Code provenance
NOT_REPORTED

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Maximize an expensive black box g(x) when cheaper information sources are biased by a domain-varying model discrepancy (not only noise) and need not form a fidelity hierarchy.

## 2. Problem setting / 3. Search space / 4. Evaluation method
misoKG. One GP prior over [M]_0 x D with f(l,x) = f(0,x) + delta_l(x), delta_l ~ GP(0, Sigma_l) independent, delta_0 = 0; Sigma((l,x),(m,x')) = Sigma_0(x,x') + 1_{l=m} Sigma_l(x,x'). Acquisition (Eq. 1): CKG(l,x) = E[(max mu^{n+1}(0,.) - max mu^n(0,.)) / c_l(x)], computed via the Frazier 2009 h function over a discrete Latin-hypercube set, maximized by multi-start gradient ascent over (l,x). Cost c_l(x) and noise lambda_l(x) assumed known/differentiable. Hyperparameters by MAP on difference data. One scalar output per query; no constraints, no failure handling, single objective.

## 5. Benchmarks
2-D Rosenbrock with an oscillatory biased source; MNIST logistic-regression hyperparameters with USPS as cheap source; 8-D assemble-to-order inventory with 3 sources.

## 6. Hardware
NOT_APPLICABLE

## 7. Toolchain
Python 2.7 / C++ on Metrics Optimization Engine (MOE); Theano (MNIST).

## 8. Metrics
Gain over best initial solution vs log total cost; test error vs log total cost; mean +/- 2 SE over at least 100 runs.

## 9. Baselines
MTBO+ (improved cost-sensitive multi-task BO); misoEI (Lam et al. 2015).

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: ATO (Fig. 3; source costs 17.1/0.5/3.9): misoKG average gain 26.1 at average query cost 54.6, 6.3% of the query cost misoEI needs for a comparable score. MNIST/USPS (Fig. 2): ~7.1% test error after ~80 queries; MTBO+ worse at equal cost late. Rosenbrock (IS0 cost 1000 vs IS1 cost 1): near-optimal within 5-10 samples using only the cheap source.

## 11. Limitations
AUTHOR-STATED: inner maximization discretized; O(M|A|^2 log|A|) outer discretization; cost/noise must be known or estimated. REVIEWER: myopic one-step, single scalar objective, unconstrained, independent discrepancies, no failed evaluations, one output per query, only synthetic/ML benchmarks; reviewed text is arXiv v2 (Nov 2016), not the NeurIPS camera-ready.

## 12. What the paper does NOT evaluate
Constraints; multi-objective; failed evaluations; one evaluation informing several outputs; sources on sub-spaces of x; hardware/HLS; batch acquisition.

## 13. Relationship to our Studies (S99 S98)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | one source, one x, scalar output per query |
| measured interactions | NO | discrepancy is source bias, not component interaction |
| staged evaluation | PARTIAL | multiple non-hierarchical sources of different cost |
| adaptive evidence acquisition | YES | cost-sensitive knowledge gradient over (source, design), Eq. 1 |
| cost/fidelity modeling | YES | per-source cost, noise and discrepancy GP |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | NOT_APPLICABLE |  |
| multi-benchmark transfer | NO |  |
| decision/Pareto stability | NO |  |
| energy/power | NO |  |
| CPU-FPGA interaction | NOT_APPLICABLE |  |
| memory/data movement | NOT_APPLICABLE |  |

## 14. Possible overlap
METHOD FOUNDATIONAL

## 15. Possible research gap (not a novelty claim)
S99 can take the misoKG form: IS0 = joint co-resident evaluation, IS_k = composed-local, delta = the S98 residual, KG-per-cost choosing between them. Three gaps: a local evaluation informs only one kernel's projection (covariance needs structure); the KG target is a scalar max, not a feasible Pareto front (needs a hypervolume/Pareto KG); no feasibility or failure handling. S98 must report residual size relative to tool noise, because it decides whether KG ever selects the joint source.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED.
