# RW0069 — Constrained multi-fidelity Bayesian optimization with automatic stop condition

> **Relevance (2026-09-25 full-text review): SUPPORTING** — No HLS work; a constrained multi-fidelity BO whose source-specific constraints mirror HLS-estimate vs post-route resource feasibility, plus a posterior-optimum stability stop rule. Candidate component or weak baseline for S99 (stopping when the decision no longer changes) and S72; validated only on analytic functions and judges feasibility on posterior means only. Primary Studies: S99 S72. Prior-art boundary: RELEVANT BUT DIFFERENT.
> **Identity:** none (arXiv:2503.01126v2, 21 Mar 2025, UC Irvine). Family name is 'Zanjani Foumani'.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Zanjani Foumani, Zahra; Bostanabad, Ramin
- Year / venue: 2025 / arXiv 2503.01126
- DOI: none recorded · URL: https://arxiv.org/abs/2503.01126

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: arxiv v2
- Canonical path: `related_work/papers/bo_mobo/RW0069_ZanjaniFoumani2025_CMFBO_arXiv.pdf` (local only, gitignored)
- SHA-256: `9a6ef133260d849998c1880454996953639bd27684e39e6593edc1bc0f48d55c`
- Source: https://arxiv.org/pdf/2503.01126

## Code provenance
https://github.com/Bostanabad-Research-Group/GP-Plus

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Cost-aware constrained multi-fidelity BO with unknown constraints that may vary across sources, plus a systematic stopping criterion.

## 2. Problem setting / 3. Search space / 4. Evaluation method
CMFBO with the GP+ latent-map emulator (source as categorical latent input, source-dependent nugget, interval-score regularized MLE). LF acquisition = exploration part of EI; HF acquisition = mean improvement; constraints via posterior means only (-sum of constraint means when violated); divided by source cost. Stop when the variance of the normalized posterior-optimum over the last 10 iterations falls below a threshold.

## 5. Benchmarks
Analytic: Branin-Hoo 3D, Hartman 6D, Wing 10D, WingSep 10D, PolyMix 20D.

## 6. Hardware
NOT_APPLICABLE

## 7. Toolchain
GP+ (PyTorch), L-BFGS; botorch baselines.

## 8. Metrics
Convergence value vs ground truth (10 repetitions), sampling cost, samples per source.

## 9. Baselines
TuRBO, qEI (single-fidelity), CSFBO.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: lowest sampling cost on all 5 analytic benchmarks under both noise levels (Figs. 3-4); qEI never reaches ground truth on 6D-20D; on PolyMix 20D TuRBO errors ~9-30%, CSFBO ~4-19%.

## 11. Limitations
AUTHOR-STATED: sensitive to initial data and dimensionality; user-set stop threshold. REVIEWER: feasibility on posterior means only; no HF exploration; sums all constraint means; no multi-fidelity baselines; analytic only; single objective; stop rule without guarantee; fails in RW0068's benchmarks.

## 12. What the paper does NOT evaluate
Multi-objective; failed evaluations; real simulators/hardware; other constrained multi-fidelity methods; stop-rule guarantees.

## 13. Relationship to our Studies (S99 S72)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO |  |
| measured interactions | NO |  |
| staged evaluation | PARTIAL |  |
| adaptive evidence acquisition | YES | heuristic cost-scaled constrained EI-style |
| cost/fidelity modeling | YES |  |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | NOT_APPLICABLE |  |
| multi-benchmark transfer | NO |  |
| decision/Pareto stability | PARTIAL | posterior-optimum stop rule |
| energy/power | NO |  |
| CPU-FPGA interaction | NOT_APPLICABLE |  |
| memory/data movement | NOT_APPLICABLE |  |

## 14. Possible overlap
RELEVANT BUT DIFFERENT

## 15. Possible research gap (not a novelty claim)
Its posterior-optimum stability stop rule is a cheap analogue of 'stop when the decision no longer changes' (would need a Pareto-set version); otherwise only a weak baseline.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/Bostanabad-Research-Group/GP-Plus.
