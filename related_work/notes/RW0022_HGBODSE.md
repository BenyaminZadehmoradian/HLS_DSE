# RW0022 — HGBO-DSE: Hierarchical GNN and Bayesian Optimization based HLS Design Space Exploration

> **Relevance (2026-09-25 correction audit): HOLD** — Hierarchical GNN + BO HLS DSE; abstract-only review. Primary Studies: S72 S05. Prior-art boundary: UNRESOLVED.
> **HOLD:** reviewed from the abstract only; no legitimate open full text found (OpenAlex: closed). Classification to be revisited when full text is available.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_ABSTRACT_ONLY`.

## Bibliographic identity
- Authors: Kuang, Huizhen; Cao, Xianfeng; Li, Jingyuan; Wang, Lingli
- Year / venue: 2023 / ICFPT
- DOI: 10.1109/ICFPT59805.2023.00017 · URL: https://doi.org/10.1109/ICFPT59805.2023.00017
- Metadata source: IEEE Xplore abstract (document 10416120) + OpenAlex (pp. 106-114) + FPT'23 program

## PDF provenance
- Status: `METADATA_ONLY_PAYWALLED` (no PDF)
- Canonical path: `none`
- SHA-256: `none`
- Source: none

## Code / dataset / artifact provenance
NOT_REPORTED (abstract mentions a constructed standard dataset; no URL found)

## 1. Research question
Finding Pareto-optimal HLS designs in a vast directive configuration space with accurate post-implementation PPA estimation.

## 2. Problem setting
Multi-objective HLS directive DSE (power, delay, resources) using a learned post-implementation predictor and BO.

## 3. Search space
HLS directive configurations at function/loop/array/operator level, with invalid configurations removed by a tree-structured modeler

## 4. Evaluation method
Post-implementation PPA (as predictor target and for evaluation), per abstract; exact tool flow NOT_REPORTED in abstract

## 5. Benchmarks
NOT_REPORTED (abstract states a standard dataset was constructed)

## 6. Hardware
NOT_REPORTED (abstract only)

## 7. Toolchain
NOT_REPORTED (abstract only)

## 8. Metrics
Prediction error of power, critical path delay, resource utilization; Pareto front quality (PPA gain); DSE speedup

## 9. Baselines
State-of-the-art predictors (unnamed in abstract); SA and NSGA-II for exploration

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: HGP reduces prediction error of power, critical path delay and resource utilization to 4.21%-7.72%; BOME with MOTPE-FL achieves better Pareto fronts than SA and NSGA-II with PPA gains of 72.00% and 30.47%; BOME with HGP accelerates DSE by up to 24x (average 14x).

## 11. Limitations
Full text not reviewed; limitations cannot be assessed beyond abstract.

## 12. What the paper does NOT evaluate
From abstract: no mention of multi-kernel joint evaluation, CPU-FPGA interaction, on-board measurement, or staged fidelity selection.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20
- Partial (dimension = PARTIAL): S02 S04 S05 S06 S21 S23 S33 S36 S37 S56 S59 S61 S72 S73 S78 S81

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract only. |
| measured interactions | PARTIAL | Tree-structured modeler removes invalid directive combinations. |
| staged evaluation | NOT_REPORTED | Abstract only. |
| adaptive evidence acquisition | PARTIAL | BO (MOTPE-FL) sequentially selects configurations; no fidelity/evidence choice described. |
| cost/fidelity modeling | PARTIAL | GNN predictor of post-implementation PPA used to accelerate DSE; no explicit cost model in abstract. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract only. |
| physical implementation in the loop | PARTIAL | Targets post-implementation PPA; whether P&R runs in loop not stated. |
| multi-benchmark transfer | NOT_REPORTED | Abstract only. |
| decision/Pareto stability | NOT_REPORTED | Abstract only. |
| energy/power | YES | Power is a predicted/optimized objective (PPA). |
| CPU-FPGA interaction | NOT_REPORTED | Abstract only. |
| memory/data movement | PARTIAL | Array-level directives in search space. |

## 14. Possible overlap
PARTIAL OVERLAP on: energy/power

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (abstract mentions a constructed standard dataset; no URL found)

## Open questions / reviewer notes
Identity confirmed: FPT 2023 (Yokohama), Fudan University authors. No open-access PDF found (OpenAlex closed; only ResearchGate listing, not used). Intelligent4DSE (arXiv:2504.19649) reuses the HGBO-DSE dataset.
