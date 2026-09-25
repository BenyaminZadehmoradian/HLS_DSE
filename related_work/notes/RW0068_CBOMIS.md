# RW0068 — Constrained Bayesian Optimisation with Multiple Information Sources

> **Relevance (2026-09-25 full-text review): SUPPORTING** — No HLS work, but a constrained, cost-normalized multi-source acquisition targeting the best feasible target-source value, assuming each query returns objective and all constraints together (as an HLS/Vivado run does). Its correlation-based variance inflation that down-weights weakly correlated sources is a candidate feasibility mechanism for S99 when local and joint evidence disagree. Primary Studies: S99 S98. Prior-art boundary: METHOD FOUNDATIONAL.
> **Identity:** none (arXiv:2607.00865v1, 1 Jul 2026; Maathuis, De Breuker, Castro (TU Delft), Osborne (Oxford)).

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Maathuis, Hauke; De Breuker, Roeland; Castro, Saullo; Osborne, Maike
- Year / venue: 2026 / arXiv 2607.00865
- DOI: none recorded · URL: https://arxiv.org/abs/2607.00865

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: arxiv v1
- Canonical path: `related_work/papers/bo_mobo/RW0068_Maathuis2026_CBOMIS_arXiv.pdf` (local only, gitignored)
- SHA-256: `39f564f4f240b915b383f24f2df0fd3b2249f0d39b1f8ad9b470d6b646449b00`
- Source: https://arxiv.org/pdf/2607.00865

## Code provenance
NOT_REPORTED (placeholder github.com/released/upon/acceptance)

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Constrained BO with small/hard-to-find feasible regions when cheaper biased auxiliary sources exist for the objective and every constraint.

## 2. Problem setting / 3. Search space / 4. Evaluation method
MS-CMES. MISO additive GP per output, u^(l) = u^(L) + Delta^(l), Matern-5/2 with masked discrepancy kernels, nested DOE. Acquisition (Eqs. 8/21): argmax alpha_n(x,l) / lambda(x,l) in a TuRBO-style trust region, alpha ~ -(1/K) sum log Pr(u^(l) in F), F = (-inf, f*_k] x (-inf, 0]^g, Pr = Phi((f* - mu_f)/sigma~_f) * prod Phi(-mu_ci/sigma~_ci); f*_k by Thompson sampling at the target (K = 32). Source bias via sigma~^(l) = sigma^(L) (1 - rho^2 Psi(gamma)), rho = sigma_L / (sigma_L + sigma_Delta). Cost lambda = 1 + (l/1e5) c_l. Feasibility judged at the target source; minimum-violation fallback when nothing is feasible.

## 5. Benchmarks
Pressure Vessel (d=4, g=4); BBOB-constrained Different Powers, Rastrigin, Rotated Rastrigin (d=40, g=9); Rosenbrock (d=100, g=2); auxiliary sources are synthetic oscillatory distortions.

## 6. Hardware
NOT_APPLICABLE (Intel Xeon Gold 5218 CPU cluster).

## 7. Toolchain
GPyTorch, BoTorch.

## 8. Metrics
Best feasible target objective vs cumulative cost (10 seeds); normalized RMSE for model comparison.

## 9. Baselines
SCBO, FuRBO, vanilla BO + LogCEI, CMES-IBO/+, CMFBO (re-implemented), random search; model baselines KOH, MTGP, single-source GP.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED (curves only): on d=40, g=9 problems (Fig. 4) CMFBO, CMES-IBO+, VBO and random search never find a feasible sample within ~2e5 cost (~200 target evaluations) while MS-CMES finds feasible points right after the initial design; on Rosenbrock d=100 MS-CMES clearly beats VBO and CMES-IBO+; Pressure Vessel similar across methods. MISO model robust at weak/zero correlation where KOH degrades (Fig. 3).

## 11. Limitations
AUTHOR-STATED: objective and constraints evaluated together; auxiliary sources assumed for every output; depends on user cost function. REVIEWER: single objective; synthetic auxiliary sources; CMFBO baseline needed c_L = 0 (possibly unfair); 10 seeds, figures only; Eq. 1 min vs Eq. 9 max inconsistency; code placeholder; unreviewed 2026 preprint; heuristic cost scaling.

## 12. What the paper does NOT evaluate
Multi-objective; real multi-fidelity simulators; failed evaluations; decoupled constraint queries; hardware/HLS.

## 13. Relationship to our Studies (S99 S98)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | 'joint' here means objective and constraints observed together |
| measured interactions | NO |  |
| staged evaluation | PARTIAL | non-hierarchical multiple sources |
| adaptive evidence acquisition | YES | constrained max-value entropy search / source cost in a trust region |
| cost/fidelity modeling | YES | lambda(x,l), discrepancy GP, rho-based variance correction |
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
S99 could adopt the feasibility-aware information term: Pr(f <= f*) x prod Pr(resource_i <= cap), with local-source variance inflated by 1 - rho^2 where the S98 residual sets rho. Joint observation of all metrics is natural for HLS runs. Must be extended from a single f* to a Pareto front; no code, so an S72 baseline needs reimplementation.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED (placeholder github.com/released/upon/acceptance).
