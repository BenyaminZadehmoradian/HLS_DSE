# RW0014 — Bayesian optimization of cooperative components for multi-stage aero-structural compressor blade design

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Pretsch, Lisa; Arsenyev, Ilya; Bartoli, Nathalie; Duddeck, Fabian
- Year / venue: 2025 / Structural and Multidisciplinary Optimization 68:84
- DOI: 10.1007/s00158-025-03998-w · URL: https://doi.org/10.1007/s00158-025-03998-w
- Metadata source: PDF first page + Crossref

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (published)
- Canonical path: `related_work/papers/bo_mobo/RW0014_Pretsch2025_CoopBO_SMO.pdf`
- SHA-256: `62192a8fbea6c95933f66a86f95218e0b7535ccc9f483fa434417046e48d8a84`
- Source: https://link.springer.com/content/pdf/10.1007/s00158-025-03998-w.pdf

## Code / dataset / artifact provenance
CC GP model fit open-sourced in SMT v2.7.0 (https://github.com/SMTorg/smt); Branin problem reproducible from equations; blade problem confidential (MTU). Data availability: not applicable.

## 1. Research question
Standard BO fails on very high-dimensional, highly constrained multi-component engineering design (multi-stage compressor blades) because of the curse of dimensionality.

## 2. Problem setting
Single-objective constrained high-dimensional optimization of a coupled multi-component system with expensive coupled high-fidelity (CFD+FE) evaluations.

## 3. Search space
100 continuous variables (multi-component Branin); 223 blade geometry parameters of a 4-stage high-pressure compressor frontblock

## 4. Evaluation method
Full coupled system evaluation each time: analytic function for Branin; for blades, 3D geometry generation, CalculiX FE structural/modal analysis (~5 min on 6 CPUs per row) and TRACE RANS CFD at two operating points (~119 min on 32 CPUs per design point).

## 5. Benchmarks
100D multi-component Branin function; 223D 4-stage aero-structural HPC blade design (industrial MTU case)

## 6. Hardware
NOT_APPLICABLE

## 7. Toolchain
SMT (Surrogate Modeling Toolbox; CC GP fit released in v2.7.0), CalculiX, DLR/MTU TRACE; AutoOpti; compute: Intel Xeon Gold 6142 CPUs

## 8. Metrics
Best feasible objective vs iterations (Branin); isentropic efficiency improvement, constraint fulfillment, simulation success rate, wall time

## 9. Baselines
Standard BO, constrained PCA-BO, SCBO, AutoOpti (blade case: BO and AutoOpti)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: informed and random CC-BO 'significantly enhance the originally poorly performing BO and largely outperform the compared algorithms'; on the blade design BO gains only marginally while informed CC-BO gains ~0.5% and random CC-BO ~0.84% average isentropic efficiency.

## 11. Limitations
Single objective; blade case industrial and confidential (not reproducible); only 5 runs on blade case due to cost; high DoE failure rate (22% successful samples); informed decomposition requires known structure; wall time increases with component count.

## 12. What the paper does NOT evaluate
No hardware/HLS; no multi-fidelity or staged cheap/expensive evidence (always full coupled evaluation); no energy, CPU-FPGA, or memory aspects; no transfer across problems; no Pareto stability.

## 13. Relationship to our Studies
- Direct (dimension = YES): S07 S15 S65
- Partial (dimension = PARTIAL): S02 S36 S37 S56 S72

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Component subproblems optimized separately but every high-fidelity evaluation is of the full coupled multi-stage system. |
| measured interactions | PARTIAL | Component interactions captured implicitly via context vectors and full-system evaluation; inter-stage effects discussed, not quantified separately. |
| staged evaluation | NO | Evaluation pipeline is a single full evaluation (geometry, FE, CFD). |
| adaptive evidence acquisition | NO | Standard constrained EI infill; no choice among evidence sources. |
| cost/fidelity modeling | NO | Single fidelity; costs reported but not modeled. |
| lifecycle/configuration cost | NOT_APPLICABLE | Not addressed. |
| physical implementation in the loop | NOT_APPLICABLE | Mechanical design; no hardware implementation. |
| multi-benchmark transfer | NO | Two independent problems, no transfer. |
| decision/Pareto stability | NO | Single objective; seed variability reported only. |
| energy/power | NOT_APPLICABLE | No electronics. |
| CPU-FPGA interaction | NOT_APPLICABLE | No hardware. |
| memory/data movement | NOT_APPLICABLE | No hardware. |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; staged evaluation; decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). CC GP model fit open-sourced in SMT v2.7.0 (https://github.com/SMTorg/smt); Branin problem reproducible from equations; blade problem confidential (MTU). Data availability: not applicable.

## Open questions / reviewer notes
Hint title 'Cooperative Components Bayesian Optimization' is the method name (CC-BO); the actual paper title is 'Bayesian optimization of cooperative components for multi-stage aero-structural compressor blade design', SMO 2025 (CC BY). Not related to 'Cooperative Bayesian Optimization for Imperfect Agents' (arXiv 2403.04442). HAL copy also exists: hal-05641733. PDF fetched with a non-browser user agent (curl/8.5) and Accept: application/pdf because the Springer browser-UA request returned a bot-check page.
