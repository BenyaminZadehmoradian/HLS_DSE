# RW0026 — Efficient Task Transfer for HLS DSE

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Transfers DSE knowledge across HLS programs/toolchains with active labelling: evidence reuse across tasks. Primary Studies: S10 S11 S87. Prior-art boundary: PARTIAL OVERLAP.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Ding, Zijian; Sohrabizadeh, Atefeh; Li, Weikai; Qin, Zongyue; Sun, Yizhou; Cong, Jason
- Year / venue: 2024 / ICCAD
- DOI: 10.1145/3676536.3676723 · URL: https://doi.org/10.1145/3676536.3676723
- Metadata source: PDF first page (ACM reference format, ICCAD '24)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/hls_dse/RW0026_Ding2024_TaskTransfer_ICCAD.pdf`
- SHA-256: `16ccd89b86d0cd8a0fedb27137e364ba13964e3fc45d2c0c8a55a93771c8284b`
- Source: /home/benyamin/Desktop/Library/Efficient Task Transfer for HLS DSE.pdf

## Code / dataset / artifact provenance
NOT_REPORTED (no code URL in paper; uses public HLSyn dataset)

## 1. Research question
HLS toolchain version changes shift QoR labels and design validity, so proxy models and best designs found for one toolchain do not carry over; re-running DSE on a new toolchain is sample-expensive.

## 2. Problem setting
Task transfer of pragma DSE for Merlin/Vitis HLS kernels from an old toolchain version (V20 or V21) to a new one (V21 or V23) under a limited HLS evaluation budget.

## 3. Search space
Merlin pragmas PIPELINE, PARALLEL, TILE per loop (HLSyn design spaces up to ~1e13 points); optional pruning of TILE pragmas

## 4. Evaluation method
Vitis HLS synthesis (via Merlin) of queried designs (30 per iteration, 8 iterations); HLS latency/resource reports.

## 5. Benchmarks
HLSyn: 13 programs for V20->V21 (dense linear algebra, data analytics, stencils), 5 large-space programs for V21->V23; domain-transfer splits with 8 test programs

## 6. Hardware
Xilinx Alveo U200 (fixed target)

## 7. Toolchain
AMD Xilinx Merlin Compiler; Vitis HLS 2020.2, 2021.1, 2023.2 (plus V18 data from HLSyn)

## 8. Metrics
Design speedup (latency) vs baselines, sample efficiency (#HLS evaluations, #valid), runtime, regression RMSE

## 9. Baselines
AutoDSE, HARP (pretrained + fine-tuned, BFS), AutoDSE+HARP; BFS, simulated annealing, genetic algorithm (optimizer comparison on model)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: abstract: 2.38x average performance improvement over AutoDSE and 1.2x over HARP with 5.75x sample efficiency and 2.7x lower runtime when transferring to V21 (Sec. 5 text reports 2.34x vs AutoDSE and 1.18x vs best of AutoDSE/HARP); for V23, 1.27x better than best of AutoDSE and HARP with 8.85x sample efficiency.

## 11. Limitations
Evaluation fixed to one device; TILE pruning heuristic applies to only 3/13 programs; results on HLS estimates only; variance across kernels in domain transfer (e.g., covariance).

## 12. What the paper does NOT evaluate
Device transfer (future work); post-route/on-board QoR; power; multi-kernel system interactions; Pareto stability across toolchains beyond best-design edit distance.

## 13. Relationship to our Studies
- Direct (dimension = YES): S05 S10 S11 S20 S23 S33 S90
- Partial (dimension = PARTIAL): S02 S04 S06 S21 S32 S34 S36 S37 S43 S45 S56 S72 S85 S86 S88 S92 S94

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Per-program DSE |
| measured interactions | PARTIAL | Measures how best designs/labels/validity shift across toolchain versions |
| staged evaluation | PARTIAL | Model-guided sampling then HLS labeling, plus final BFS round |
| adaptive evidence acquisition | YES | Active learning (coreset) selects which designs to synthesize each CEM iteration |
| cost/fidelity modeling | PARTIAL | Budget in HLS runs/timeouts accounted; no multi-fidelity model |
| lifecycle/configuration cost | PARTIAL | Addresses cost of re-optimizing when the HLS toolchain version changes |
| physical implementation in the loop | NO | HLS reports only |
| multi-benchmark transfer | YES | Transfer across toolchain versions and across programs (domain transfer) |
| decision/Pareto stability | PARTIAL | Quantifies change of best design across toolchains (pragma edit distance) |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | NO | Not analyzed beyond TILE pruning heuristic |

## 14. Possible overlap
PARTIAL OVERLAP on: adaptive evidence acquisition; multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no code URL in paper; uses public HLSyn dataset)

## Open questions / reviewer notes
Minor inconsistency between abstract (2.38x/1.2x) and results text (2.34x/1.18x).
