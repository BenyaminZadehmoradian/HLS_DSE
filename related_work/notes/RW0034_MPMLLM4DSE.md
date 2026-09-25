# RW0034 — MPM-LLM4DSE: Reaching the Pareto Frontier in HLS with Multimodal Learning and LLM-Driven Exploration

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Xu, Lei; Wang, Shanshan; Xiao, Chenglong
- Year / venue: 2026 / DATE
- DOI: 10.23919/DATE69613.2026.11539388 · URL: https://arxiv.org/abs/2601.04801
- Metadata source: PDF first page (arXiv v1, 'Accepted for publication at DATE 2026') + arXiv abs page + OpenAlex (DATE DOI)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/hls_dse/RW0034_Xu2026_MPMLLM4DSE_DATE_arxiv.pdf`
- SHA-256: `3fc8c97cb72af9abbcd00c8463706203c2b53516b047022852d0d5dd53585eb7`
- Source: https://arxiv.org/pdf/2601.04801

## Code / dataset / artifact provenance
Code and models: https://github.com/wslcccc/MPM-LLM4DSE (stated in paper); dataset derived from GNN-DSE.

## 1. Research question
GNN-only QoR surrogates miss source-level semantics of pragmas, and generic multi-objective optimizers do not exploit domain knowledge about how pragmas affect QoR in HLS DSE.

## 2. Problem setting
Single-kernel pragma DSE for Vitis HLS with a learned QoR surrogate replacing HLS runs during search.

## 3. Search space
Per-kernel HLS pragma configurations (pipeline off/flatten, unroll/parallel factors, tiling etc., GNN-DSE/Merlin-style design spaces); up to ~7.6M configs (jacobi-2d)

## 4. Evaluation method
Surrogate predictions during DSE; ground truth labels from Vitis HLS 2022.1 synthesis reports (C-synthesis latency and LUT/DSP/FF/BRAM); ADRS against reference Pareto set.

## 5. Benchmarks
GNN-DSE dataset: 15 training kernels from MachSuite and PolyBench (adi, aes, atax, bicg, doitgen, fdtd-2d, gemm-blocked, gemm-ncubed, gemver, gemm-p, gesummv, mvt, spmv-crs, spmv-ellpack, 2mm, 3mm; 4,353 graph-text samples); unseen test kernels heat-3d, jacobi-1d, jacobi-2d, nw, seidel-2d, stencil

## 6. Hardware
AMD UltraScale+ MPSoC ZCU104 (target)

## 7. Toolchain
Vitis HLS 2022.1, Vivado 2022.1; LLVM + ProGraML; CodeBERT-c; GPT-3.5-turbo/GPT-4o/Qwen3-235B-A22B-Thinking-2507 via API

## 8. Metrics
RMSE of latency, LUT, DSP, FF, BRAM predictions; ADRS; DSE runtime

## 9. Baselines
Predictors: GNN-DSE, HGBO, IronMan-Pro, ProgSG, ECoGNN-only, LM-only. DSE: NSGA-II, SA, ACO, LLMMH, GNN-DSE exact DSE; prompting strategies (zero-shot, few-shot, OPRO, CoT)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: MPM outperforms ProgSG QoR prediction by up to 10.25x; LLM4DSE achieves an average 39.90% performance gain over prior methods (Qwen3 variant: 46.07% average ADRS improvement over metaheuristics, 21.39% over LLMMH; 32.66% ADRS reduction vs GNN-DSE under equal time on large spaces).

## 11. Limitations
QoR only at HLS-report level (no post-route/on-board); single-kernel DSE; relies on commercial LLM APIs (runtime dominated by API latency); small unseen-kernel test set (6 kernels); reference Pareto set construction for ADRS not detailed beyond standard.

## 12. What the paper does NOT evaluate
Multi-kernel/joint system evaluation, post-implementation QoR, power/energy, CPU-FPGA interaction, stability of Pareto sets across runs, cost of HLS runs in the loop (surrogate only).

## 13. Relationship to our Studies
- Direct (dimension = YES): S10 S11 S90
- Partial (dimension = PARTIAL): S05 S20 S23 S33 S71

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Each kernel explored independently. |
| measured interactions | NO | No inter-kernel interactions. |
| staged evaluation | NO | Surrogate-only evaluation during DSE; no staged fidelity escalation described. |
| adaptive evidence acquisition | PARTIAL | LLM iteratively proposes configurations using updated elite examples, but evaluations are surrogate predictions, not acquired tool runs. |
| cost/fidelity modeling | NO | Runtime reported, but evaluation cost not modeled in search. |
| lifecycle/configuration cost | NO | Not addressed. |
| physical implementation in the loop | NO | Labels from Vitis HLS synthesis reports. |
| multi-benchmark transfer | YES | Predictor trained on 15 kernels and tested on 6 unseen kernels. |
| decision/Pareto stability | NOT_REPORTED | No variance across repeated LLM runs reported. |
| energy/power | NO | Objectives are latency and resources. |
| CPU-FPGA interaction | NO | Kernel-only. |
| memory/data movement | NO | Only BRAM utilization as a metric. |

## 14. Possible overlap
PARTIAL OVERLAP on: multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; measured interactions; staged evaluation; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code and models: https://github.com/wslcccc/MPM-LLM4DSE (stated in paper); dataset derived from GNN-DSE.

## Open questions / reviewer notes
Hint said ~2025; actual arXiv posting Jan 2026, DATE 2026. DOI 10.23919/DATE69613.2026.11539388 taken from OpenAlex, not verified on IEEE Xplore. Some ADRS table columns were garbled in text extraction; headline numbers taken from abstract/text.
