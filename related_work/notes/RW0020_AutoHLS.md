# RW0020 — AutoHLS: Learning to Accelerate Design Space Exploration for HLS Designs

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Ahmed, Md Rubel; Koike-Akino, Toshiaki; Parsons, Kieran; Wang, Ye
- Year / venue: 2023 / IEEE MWSCAS
- DOI: 10.1109/MWSCAS57524.2023.10405914 · URL: https://doi.org/10.1109/MWSCAS57524.2023.10405914
- Metadata source: arXiv abs page (comment 'MWSCAS 2023') + PDF + OpenAlex (DOI)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/hls_dse/RW0020_Ahmed2023_AutoHLS_MWSCAS_arxiv.pdf`
- SHA-256: `252730fe15bf87d2c7484c5de2770457802a089beae4a4089da1d5a624245a57`
- Source: https://arxiv.org/pdf/2403.10686

## Code / dataset / artifact provenance
NOT_REPORTED (no code link in paper); MERL tech report TR2023-097 also available

## 1. Research question
BO-based multi-objective HLS DSE wastes time synthesizing candidates that fail within resource/synthesis-time budgets.

## 2. Problem setting
Budget-constrained DSE of a single CNN convolution kernel on an FPGA with pragma and kernel-operation (quantization) transformations.

## 3. Search space
Pragmas (unroll factor, pipeline II, latency min/max; also mentions array partition) and kernel/operation transforms (MAC vs PoT vs APoT quantization, fixed-point precision)

## 4. Evaluation method
Vitis HLS 2022.1 synthesis (csim + synth) with synthesis-time budget; ML classifier/regressor predictions used to skip candidates.

## 5. Benchmarks
CNN convolution block (Cin=100, L=7, Cout=106) with MAC/PoT/APoT variants; 3302 BO-generated design points

## 6. Hardware
Xilinx ZCU104 (target); Intel i7-8700K host

## 7. Toolchain
Vitis HLS 2022.1; Optuna (TPE)

## 8. Metrics
Failure prediction ROC-AUC, MSE of resource prediction, exploration time speedup, Pareto front (LUT vs processing time), FF/LUT/DSP/latency

## 9. Baselines
Plain BO (Optuna TPE); SVM, logistic regression, lasso, KRR, Bayesian ridge for prediction

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 'Our experimental results demonstrate up to a 70-fold speedup in exploration time' (Table III: ~14x-74x depending on threshold).

## 11. Limitations
Single CNN kernel case study; generality to unseen designs not evaluated (stated); QNN is proof-of-concept (simulated); HLS-level results only; although power is listed as an objective in the intro, no power results are reported.

## 12. What the paper does NOT evaluate
Multi-kernel/system designs, post-route/on-board results, power/energy results, cross-benchmark transfer, Pareto stability.

## 13. Relationship to our Studies
- Direct (dimension = YES): S32 S34 S88
- Partial (dimension = PARTIAL): S04 S05 S06 S20 S21 S23 S33 S72

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Single kernel. |
| measured interactions | NO | Not addressed. |
| staged evaluation | YES | ML failure/resource predictor screens BO samples before full HLS synthesis. |
| adaptive evidence acquisition | PARTIAL | BO sequential sampling plus threshold-based filtering decides which samples get synthesized. |
| cost/fidelity modeling | PARTIAL | Synthesis-time budget treated as a constraint; exploration time measured. |
| lifecycle/configuration cost | NO | Not addressed. |
| physical implementation in the loop | NO | HLS synthesis only. |
| multi-benchmark transfer | NO | Single kernel; authors list generality as future work. |
| decision/Pareto stability | NOT_REPORTED | Not reported. |
| energy/power | NO | Power listed as a consideration but not reported. |
| CPU-FPGA interaction | NO | Not addressed. |
| memory/data movement | NO | Not addressed. |

## 14. Possible overlap
PARTIAL OVERLAP on: staged evaluation

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; measured interactions; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no code link in paper); MERL tech report TR2023-097 also available

## Open questions / reviewer notes
Identity matches hint. arXiv posted Mar 2024; published at MWSCAS 2023 (IEEE Xplore document 10405914). MERL TR2023-097 is another legitimate copy.
