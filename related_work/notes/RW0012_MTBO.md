# RW0012 — Multi-Task Bayesian Optimization

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Swersky, Kevin; Snoek, Jasper; Adams, Ryan P.
- Year / venue: 2013 / NeurIPS (NIPS 2013)
- DOI: NOT_REPORTED · URL: https://papers.nips.cc/paper/2013/hash/f33ba15effa5c10e873bf3842afb46a6-Abstract.html
- Metadata source: PDF first page + NeurIPS proceedings page

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (published)
- Canonical path: `related_work/papers/multifidelity/RW0012_Swersky2013_MTBO_NeurIPS.pdf`
- SHA-256: `294123432b98a2fa5dc3eed6a2e3a6f5c3df03473f0f5350aa046640cb0acb57`
- Source: https://papers.nips.cc/paper_files/paper/2013/file/f33ba15effa5c10e873bf3842afb46a6-Paper.pdf

## Code / dataset / artifact provenance
No code URL given in paper; experimental details deferred to supplementary material; uses public datasets.

## 1. Research question
Whether knowledge from previous or related hyperparameter optimizations can be transferred to new tasks to make Bayesian optimization faster (the cold-start problem), and how to exploit cheap related tasks.

## 2. Problem setting
Black-box hyperparameter tuning of ML models across several correlated tasks (datasets, CV folds, data subsets) with differing evaluation costs.

## 3. Search space
ML model hyperparameters (e.g., 4 LR hyperparameters, CNN hyperparameters, PMF learning rate/l2/rank/epochs, online LDA grid); 2D Branin-Hoo input domain

## 4. Evaluation method
Real training/validation runs of ML models (validation error, perplexity, RMSE) plus a synthetic shifted Branin-Hoo function; wall-clock time used as cost.

## 5. Benchmarks
Shifted Branin-Hoo; logistic regression on MNIST (USPS as related task); CNN on SVHN (from CIFAR-10 / SVHN subset); CNN on k-means features for STL-10 (from CIFAR-10); PMF on MovieLens-100k (5-fold CV); online LDA on 200k-document corpus (50k-document subset as auxiliary)

## 6. Hardware
NOT_APPLICABLE

## 7. Toolchain
Own GP/BO code (Spearmint-style GP EI MCMC); cuda-convnet and Deepnet for CNNs; versions NOT_REPORTED

## 8. Metrics
Best (min) validation error / perplexity / RMSE vs function evaluations and vs time; average cumulative error (ACE); time to reach given error

## 9. Baselines
Single-task BO (GP EI MCMC / STBO) from scratch; direct transfer of best settings from the related task; full k-fold cross-validation

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: multi-task BO 'significantly speeds up the optimization process when compared to the standard single-task approach'; e.g., MTBO reaches the LR minimum in ~40 min vs 100 min for STBO, and finds the online-LDA minimum in ~6 days vs 10 days (saving almost 4 days) by dynamically querying the cheaper task.

## 11. Limitations
GP cost cubic in total observations across tasks; assumes positive task correlation (Cholesky elements sampled in log space); entropy-search acquisition evaluated over a fixed candidate set (top-C EI points); average-objective method uses a heuristic (impute then EI) rather than a principled criterion; single objective only.

## 12. What the paper does NOT evaluate
No hardware/HLS, no multi-objective or constrained optimization, no physical implementation, energy, or CPU-FPGA/memory aspects; no Pareto stability analysis.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S05 S06 S10 S11 S20 S21 S23 S33 S72 S90
- Partial (dimension = PARTIAL): S02 S32 S34 S36 S37 S56 S88

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Tasks are related datasets/folds, not jointly composed components. |
| measured interactions | PARTIAL | Inter-task correlation learned via task covariance Kt; not component interactions. |
| staged evaluation | PARTIAL | Cheap auxiliary task (small dataset) queried before expensive primary; not an explicit staged pipeline. |
| adaptive evidence acquisition | YES | Cost-sensitive multi-task entropy search chooses which task/fold to query; fast CV chooses which fold. |
| cost/fidelity modeling | YES | Evaluation cost c_t(x) modeled by multi-task GP on log cost; information gain per unit cost. |
| lifecycle/configuration cost | NOT_APPLICABLE | Not addressed. |
| physical implementation in the loop | NOT_APPLICABLE | No hardware. |
| multi-benchmark transfer | YES | Transfer across datasets (USPS->MNIST, CIFAR-10->SVHN/STL-10, shifted Branin). |
| decision/Pareto stability | NO | Not analyzed. |
| energy/power | NOT_APPLICABLE | No hardware. |
| CPU-FPGA interaction | NOT_APPLICABLE | No hardware. |
| memory/data movement | NOT_APPLICABLE | No hardware. |

## 14. Possible overlap
PARTIAL OVERLAP on: adaptive evidence acquisition; cost/fidelity modeling; multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). No code URL given in paper; experimental details deferred to supplementary material; uses public datasets.

## Open questions / reviewer notes
Identity unambiguous. NeurIPS 2013 has no DOI; proceedings URL used.
