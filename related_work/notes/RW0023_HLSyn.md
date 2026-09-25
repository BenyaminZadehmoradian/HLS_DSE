# RW0023 — Towards a Comprehensive Benchmark for High-Level Synthesis Targeted to FPGAs

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Bai, Yunsheng; Sohrabizadeh, Atefeh; Qin, Zongyue; Hu, Ziniu; Sun, Yizhou; Cong, Jason
- Year / venue: 2023 / NeurIPS (Datasets and Benchmarks Track)
- DOI: NOT_REPORTED · URL: https://proceedings.neurips.cc/paper_files/paper/2023/hash/8dfc3a2720a4112243a285b98e0d4415-Abstract-Datasets_and_Benchmarks.html
- Metadata source: PDF first page (NeurIPS 2023 Datasets and Benchmarks footer) + NeurIPS proceedings page via web search

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/hls_dse/RW0023_Bai2023_HLSyn_NeurIPS.pdf`
- SHA-256: `9797c1e70e9ea803d5d0868d53f76ffc675d2ab7e484f2ca7a9f373528bcef92`
- Source: https://papers.neurips.cc/paper_files/paper/2023/file/8dfc3a2720a4112243a285b98e0d4415-Paper-Datasets_and_Benchmarks.pdf

## Code / dataset / artifact provenance
Dataset/code: https://github.com/UCLA-DM/HLSyn ; OpenReview: https://openreview.net/forum?id=HvcLKgtbco

## 1. Research question
Open datasets for training HLS design-quality predictors are limited in program complexity and available optimizations.

## 2. Problem setting
Benchmark for predicting validity (classification) and latency/DSP/BRAM/LUT/FF (regression) of Merlin-pragma HLS designs, including generalization to held-out kernels.

## 3. Search space
Merlin PIPELINE (off/cg/fg), PARALLEL, TILE options per loop (labels collected via AutoDSE-driven exploration)

## 4. Evaluation method
HLS tool reports (Merlin + SDx/Vitis) as labels; model RMSE and classification accuracy on test splits.

## 5. Benchmarks
42 kernels from MachSuite and PolyBench (linear algebra, data mining, stencils, encryption, dynamic programming)

## 6. Hardware
AMD/Xilinx Alveo U200 @250 MHz (synthesis target)

## 7. Toolchain
Merlin Compiler; AMD/Xilinx SDx (v1) and Vitis (v2) (exact versions not stated in extracted text)

## 8. Metrics
RMSE for PERF/DSP/BRAM/LUT/FF; classification accuracy

## 9. Baselines
code2vec, CodeT5 (rand/frozen/fine-tuned), GraphCodeBERT (and -L), GNN-DSE, GNN-DSE-2L, concatenated code+graph encoders

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: releases 42 kernels with over 42,000 labeled designs; no baseline consistently wins, pre-training helps code transformers, more GNN layers do not necessarily help, and generalization to unseen kernels is difficult without adaptation.

## 11. Limitations
Labels are HLS estimates; DSE stage not included in benchmark (future work); limited kernel count and single device; Merlin-specific pragma space.

## 12. What the paper does NOT evaluate
Post-route QoR; power; DSE task itself; multi-kernel/system interactions; other toolchains/devices.

## 13. Relationship to our Studies
- Direct (dimension = YES): S10 S11 S90
- Partial (dimension = PARTIAL): S71 S85 S86 S94

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Benchmark of single-kernel designs |
| measured interactions | NO | Not studied |
| staged evaluation | NOT_APPLICABLE | Benchmark |
| adaptive evidence acquisition | NOT_APPLICABLE | Benchmark |
| cost/fidelity modeling | NO | Not modeled |
| lifecycle/configuration cost | PARTIAL | Two tool versions provided, enabling study of tool-version shift |
| physical implementation in the loop | NO | HLS labels only |
| multi-benchmark transfer | YES | Held-out kernels with zero-shot and few-shot adaptation |
| decision/Pareto stability | NOT_APPLICABLE | Benchmark |
| energy/power | NO | Not included |
| CPU-FPGA interaction | NO | Not included |
| memory/data movement | NO | Not included |

## 14. Possible overlap
PARTIAL OVERLAP on: multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: measured interactions

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Dataset/code: https://github.com/UCLA-DM/HLSyn ; OpenReview: https://openreview.net/forum?id=HvcLKgtbco

## Open questions / reviewer notes
Dataset name is HLSyn; key chosen as 'HLSyn'. NeurIPS D&B papers have no DOI (ACM DL mirror id 10.5555/3666122.3668084 exists but is not a registered DOI). Other papers (HARP, LIFT) indicate v1 = SDx 2018.3 and v2 = Vitis 2020.2. | Duplicate acquisition: the same PDF (identical sha256) was also downloaded from https://papers.neurips.cc/paper_files/paper/2023/file/8dfc3a2720a4112243a285b98e0d4415-Paper-Datasets_and_Benchmarks.pdf; one canonical copy kept.
