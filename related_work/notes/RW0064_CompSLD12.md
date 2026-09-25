# RW0064 — Compositional System-Level Design Exploration with Planning of High-Level Synthesis

> **Relevance (2026-09-25 full-text review): CORE** — Jointly selects knob-settings of 14 HLS components of an MPEG2 encoder under a system throughput constraint while minimizing HLS oracle queries: boundary (a), also relevant to budgeted evidence selection. Origin of the compositional TMG/LP formulation reused by COSMOS; its component dominance pruning is exactly the local-Pareto pruning S97 tests. Primary Studies: S97 S99 S72 S04. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** none (Hung-Yi Liu, Michele Petracca, Luca P. Carloni; DATE 2012, pp. 641-646).

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Liu, Hung-Yi; Petracca, Michele; Carloni, Luca P.
- Year / venue: 2012 / DATE 2012, pp. 641-646 (Best Paper Award)
- DOI: 10.1109/DATE.2012.6176550 · URL: http://www.cs.columbia.edu/~luca/research/liu_DATE12.pdf

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: accepted
- Canonical path: `related_work/papers/core/RW0064_Liu2012_CompSLD12_DATE_accepted.pdf` (local only, gitignored)
- SHA-256: `7f38e096eab05949815e7656b5880ed888928e31c1f70c717e965dbe44444cd3`
- Source: http://www.cs.columbia.edu/~luca/research/liu_DATE12.pdf

## Code provenance
NOT_REPORTED

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
Build a system area-vs-throughput Pareto front with consecutive points within ratio delta while querying the HLS oracle on individual components as few times as possible.

## 2. Problem setting / 3. Search space / 4. Evaluation method
Component knob-setting trade-off library (clock sweep extremes per knob-setting); component design-space pruning by dominance per atomic lambda interval (Alg. 1, segment tree); convex piecewise-linear f_i fits; system LP min sum f_i(tau_i) s.t. A*sigma + M0/theta >= tau swept by (1+delta), plus an alpha-constrained LP to fill gaps; HLS queries issued after planning (parallelizable). COMPOSITION OPERATOR: system cost = SUM of component areas; throughput = 1 / TMG cycle time.

## 5. Benchmarks
MPEG2 encoder in SystemC (22 components; 14 in the strongly connected TMG; ~10.9 knob-settings per component).

## 6. Hardware
Industrial 45 nm ASIC library.

## 7. Toolchain
Unnamed commercial SystemC HLS tool; LP/QP solvers.

## 8. Metrics
Area, effective latency/throughput, area mismatch between LP approximation and 'oracle result' point, oracle queries, sequential HLS runtime.

## 9. Baselines
Exhaustive querying (19 x 14 queries); exhaustive sequential runtime.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: dominance pruning keeps 2.8 of 10.9 knob-settings per interval (74% of invocations pruned). delta = 0.2: 19 system points, average area mismatch 1%, max 7%; 57 vs 266 queries (4.7x); 35 h vs 124 h (3.5x). delta = 0.15 / 0.1: max mismatch 10% / 11%; 5.3x / 6.4x query efficiency; 4.1x / 5.0x runtime.

## 11. Limitations
AUTHOR-STATED: cost functions assumed convex; accuracy depends on segment count. REVIEWER: the 'oracle result' system point is itself composed (summed HLS areas + TMG throughput); no integrated system is synthesized, so mismatch measures fitting error, not composition error. Dominance pruning is lossless only if cost is additive/monotone and components do not interact; assumed, not tested. Single benchmark, ASIC, HLS fidelity.

## 12. What the paper does NOT evaluate
Joint synthesis/implementation; measured cross-component interaction; whether pruned knob-settings could be system-optimal under non-additive composition; FPGA, P&R, power, variability.

## 13. Relationship to our Studies (S97 S99 S72 S04)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | PARTIAL | joint LP choice, sum-of-components evaluation |
| measured interactions | NO | TMG timing only |
| staged evaluation | PARTIAL | library, LP planning, targeted queries; same fidelity |
| adaptive evidence acquisition | PARTIAL | planner selects component queries; deterministic, not VOI |
| cost/fidelity modeling | PARTIAL | query count / HLS runtime as cost; no fidelity levels |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | NO | HLS/ASIC report area |
| multi-benchmark transfer | PARTIAL | libraries claimed reusable; one system evaluated |
| decision/Pareto stability | NO |  |
| energy/power | NO |  |
| CPU-FPGA interaction | NO |  |
| memory/data movement | PARTIAL | memory configuration as a knob |

## 14. Possible overlap
PARTIAL OVERLAP

## 15. Possible research gap (not a novelty claim)
S97: canonical statement of per-component dominance pruning + additive composition — the hypothesis S97 falsifies or confirms with an exhaustive joint oracle; its 1%/7% mismatch must not be cited as evidence that composition holds (both sides are composed). S99/S72: the LP plan-then-query strategy is a strong local-only baseline (4.7-6.4x query efficiency as reference).

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: NOT_REPORTED.
