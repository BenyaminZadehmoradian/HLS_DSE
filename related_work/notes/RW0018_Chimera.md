# RW0018 — Chimera: A Hybrid Machine Learning Driven Multi-Objective Design Space Exploration Tool for FPGA High-Level Synthesis

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Active-learning HLS DSE that selects which designs to synthesize, single fidelity, per benchmark. Primary Studies: S05 S72. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** Name shared by unrelated works (HPCA 2023 operator fusion, SC 2021 pipeline training); HLS DSE tool by Yu, Huang, Chen selected.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Yu, Mang; Huang, Sitao; Chen, Deming
- Year / venue: 2022 / arXiv (extended version of IDEAL 2021 paper)
- DOI: 10.48550/arXiv.2207.07917 · URL: https://arxiv.org/abs/2207.07917
- Metadata source: arXiv PDF first page + arXiv abs page; conference version metadata from Springer LNCS listing

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/hls_dse/RW0018_Yu2022_Chimera_arXiv.pdf`
- SHA-256: `9be54035dfb9985b3f7d2b6199d0fe4fd7be8dfacad1efdb8d0511b3473c3eb6`
- Source: https://arxiv.org/pdf/2207.07917

## Code / dataset / artifact provenance
NOT_REPORTED (paper states source code will be released; no URL given)

## 1. Research question
Applying HLS optimization directives to reach expert-level designs requires expertise and many slow HLS runs; DSE must be sample-efficient, multi-objective and escape local optima.

## 2. Problem setting
Single-application multi-objective (latency vs weighted resource) HLS directive DSE with a fixed evaluation budget (170 HLS runs, <24 h).

## 3. Search space
HLS directives on selected loops and arrays (unroll, pipeline, array partition type/factor), pruned by basic HLS design rules

## 4. Evaluation method
Xilinx Vivado HLS 2019.2 synthesis reports (latency, BRAM/DSP/LUT/FF); weighted resource = 0.4 BRAM + 0.4 DSP + 0.1 LUT + 0.1 FF

## 5. Benchmarks
Rosetta: 3D Rendering, BNN, Digit Recognition, Face Detection, Optical Flow, Spam Filtering

## 6. Hardware
NOT_REPORTED (target FPGA part not stated; DSE run on AMD 3900X workstation)

## 7. Toolchain
Xilinx Vivado HLS 2019.2

## 8. Metrics
Latency (us), weighted resource usage, Pareto frontier, DSE time

## 9. Baselines
Rosetta hand-tuned designs; random-proposal-only exploration

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: in less than 24 hours, explored design points with the same or superior performance compared to expert hand-tuned Rosetta designs; Pareto elbow point can save up to 26% flip-flops with negligibly higher latency (3D rendering).

## 11. Limitations
Only HLS-estimated QoR; single tool/version; manual pruning of knobs; fixed 170-point budget; results vary run to run; no comparison against other published DSE tools; resources scalarized with fixed weights.

## 12. What the paper does NOT evaluate
Post-implementation timing/resources, power, multi-kernel joint evaluation, cross-benchmark transfer, statistical stability across runs, CPU-FPGA interaction.

## 13. Relationship to our Studies
- Direct (dimension = YES): S05 S20 S23 S33
- Partial (dimension = PARTIAL): S02 S04 S06 S21 S36 S37 S43 S45 S56 S72 S73 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Each benchmark explored independently. |
| measured interactions | PARTIAL | Qualitative example of directive interaction (array partition vs unroll in Face Detection). |
| staged evaluation | NO | Single HLS-synthesis evaluation level. |
| adaptive evidence acquisition | YES | Active learning with probabilistic evaluation and Thompson-sampling switching between proposal engines. |
| cost/fidelity modeling | PARTIAL | Timeout/error prediction model avoids expensive failing syntheses; no multi-fidelity. |
| lifecycle/configuration cost | NO | Not considered. |
| physical implementation in the loop | NO | Vivado HLS reports only. |
| multi-benchmark transfer | NO | Same hyper-parameters used across benchmarks, but no knowledge transfer. |
| decision/Pareto stability | PARTIAL | Acknowledges run-to-run variation; not quantified. |
| energy/power | NO | Power not evaluated. |
| CPU-FPGA interaction | NO | Not considered. |
| memory/data movement | PARTIAL | Array partitioning directives only. |

## 14. Possible overlap
PARTIAL OVERLAP on: adaptive evidence acquisition

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; staged evaluation; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (paper states source code will be released; no URL given)

## Open questions / reviewer notes
Name ambiguity. Selected: Yu, Huang, Chen (UIUC) HLS DSE tool. Conference version: 'Chimera: A Hybrid Machine Learning-Driven Multi-Objective Design Space Exploration Tool for FPGA High-Level Synthesis', IDEAL 2021, LNCS 13113, DOI 10.1007/978-3-030-91608-4_52 (Best Paper); downloaded PDF is the extended arXiv version. Related UIUC thesis: 'Chimera: An efficient design space exploration tool for FPGA high-level synthesis' (IDEALS, https://www.ideals.illinois.edu/items/118601). Unrelated same-name works: Chimera operator-fusion compiler (HPCA 2023), Chimera bidirectional pipelines for training large-scale neural networks (SC 2021).
