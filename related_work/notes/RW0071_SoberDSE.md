# RW0071 — SoberDSE: Sample-Efficient Design Space Exploration via Learning-Based Algorithm Selection

> **Relevance (2026-09-25 full-text review): SUPPORTING** — SoberDSE runs ten existing HLS DSE algorithms (seven heuristics and three RL methods) on the same single-kernel benchmarks, all scored with a GNN QoR predictor, then learns which algorithm to pick per benchmark. Direct empirical background for S72 (search-algorithm comparison). Not CORE: every benchmark is explored alone, no joint evaluation, no fidelity/evidence-source choice. Primary Studies: S72 S04 S97. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** Page footer: 'PREPRINT - Accepted for publication at the 2026 Design Automation Conference (DAC)'. Venue: DAC 2026 (accepted); arXiv 2603.00986v1.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_FULL_TEXT` (full text read 2026-09-25; an earlier abstract-only HOLD note is superseded and stays in git history).

## Bibliographic identity
- Authors: Xu, Lei; Wang, Shanshan; Xiao, Chenglong
- Year / venue: 2026 / DAC 2026 (accepted; arXiv 2603.00986)
- DOI: none recorded · URL: https://arxiv.org/abs/2603.00986

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` · version: arxiv v1 (accepted at DAC 2026)
- Canonical path: `related_work/papers/hls_dse/RW0071_Xu2026_SoberDSE_DAC_arxiv.pdf` (local only, gitignored)
- SHA-256: `a00e3815f6af518e66b453db1fefae65d703ab56d21bc7497e786c22e13b0416`
- Source: https://arxiv.org/pdf/2603.00986

## Code provenance
https://anonymous.4open.science/r/Sober-4377

## Dataset/artifact provenance
See benchmarks below; no dataset artifact recorded unless listed there.

## 1. Research question
No single HLS DSE algorithm is best on every benchmark (No-Free-Lunch); can the best DSE algorithm for a kernel be predicted from its code features?

## 2. Problem setting / 3. Search space / 4. Evaluation method
Ten DSE algorithms (NSGA-II, SA, ACO, PSO, Lattice-Traversing, HGBO-DSE, MOEDA, IRONMAN-PRO AC/PG, QL-MOEA) run on 20 training benchmarks; every configuration scored by a pre-trained ECoGNN QoR predictor (not HLS). Label = algorithm with lowest ADRS; ProGraML graphs embedded by ECoGNN; supervised MLP recommender initialises a PPO agent. ADRS reference set = 'average performance of the ten algorithms', not a ground-truth front.

## 5. Benchmarks
Training: 20 MachSuite/PolyBench kernels (spaces 970 to 1.77e13). Inference: nw, stencil, atax-medium, bicg-medium, correlation, jacobi-2d, mvt, symm-opt, syrk.

## 6. Hardware
States Xilinx Alveo U200 at 250 MHz (predictor target); no place-and-route or on-board measurement.

## 7. Toolchain
Pre-trained ECoGNN GNN predictor (Intelligent4DSE); HLS tool/version of its training data NOT_REPORTED; Python, PyTorch, LLVM + ProGraML.

## 8. Metrics
ADRS; recommendation accuracy; total DSE runtime (s) over 9 inference kernels; objectives latency and resources.

## 9. Baselines
NSGA-II, SA, ACO, PSO, Lattice, HGBO-DSE, MOEDA, IRONMAN-PRO AC/PG, QL-MOEA; classifiers RF, XGBoost, K-NN, SVM, supervised-only.

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: Table 3 average ADRS over 9 kernels: SoberDSE 0.0172, HGBO-DSE 0.0804, SA 0.0839, Lattice 0.0921, MOEDA 0.1026, PSO 0.1063, NSGA-II 0.1390, ACO 0.1509 (81.32% better than Lattice, 78.61% than HGBO-DSE). Fig. 5: 76.31% better than AC, 54.81% than PG, 75.29% than QL-MOEA. Fig. 4: +35.57% recommendation accuracy. Fig. 6 runtime: SoberDSE 862 s vs Lattice 412 s, SA 1742 s, PG 3538 s. 'No single algorithm dominates' rests on Fig. 1(b) (4 heuristics x 5 kernels) and per-kernel winners in Table 3.

## 11. Limitations
AUTHOR-STATED: few real benchmarks; stochastic algorithms may be non-deterministic. REVIEWER: all ADRS on GNN-predicted QoR, not HLS/implementation; reference set built from the suite's own outputs; apparently single runs, no seeds/variance; SoberDSE (which only selects and runs a suite algorithm) beats every suite member by wide margins on several kernels, implying re-run variance comparable to between-algorithm gaps; budgets per algorithm NOT_REPORTED; headline numbers inconsistent (abstract 5.7x/4.2x vs 81.06%/68.80% vs Table 3); runtime excludes synthesis; only single-kernel designs.

## 12. What the paper does NOT evaluate
Real HLS or post-route evaluation; wall-clock incl. synthesis; equal budgets; repeated runs/significance; multi-kernel designs; feasibility; energy; exhaustive Pareto reference.

## 13. Relationship to our Studies (S72 S04 S97)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | each kernel explored in isolation |
| measured interactions | NO | none measured |
| staged evaluation | NO | single GNN-predictor fidelity |
| adaptive evidence acquisition | PARTIAL | adaptive at algorithm-selection level, not per-configuration evidence |
| cost/fidelity modeling | NO | runtime reported only as a result |
| lifecycle/configuration cost | NO |  |
| physical implementation in the loop | NO | QoR from ECoGNN, no synthesis/P&R |
| multi-benchmark transfer | YES | disjoint training (20) and inference (9) kernels |
| decision/Pareto stability | NOT_REPORTED | no seeds or repeats |
| energy/power | NOT_REPORTED | only latency and resources used |
| CPU-FPGA interaction | NO |  |
| memory/data movement | NO |  |

## 14. Possible overlap
PARTIAL OVERLAP

## 15. Possible research gap (not a novelty claim)
For S72 the closest prior algorithm comparison, but weak evidence (single runs on a GNN surrogate, self-referential ADRS reference, run-to-run variance comparable to between-algorithm gaps). S72 must rank algorithms at equal budget, with multiple seeds, against the S04 oracle, and report whether rankings survive noise. Not prior art for S97/S99.

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://anonymous.4open.science/r/Sober-4377.
