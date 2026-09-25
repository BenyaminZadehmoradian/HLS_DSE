# RW0036 — Fast and Accurate Estimation of Quality of Results in High-Level Synthesis with Machine Learning

> **Relevance (2026-09-25 correction audit): SUPPORTING** — Estimates post-implementation QoR from HLS reports: cross-fidelity model. Primary Studies: S04 S21 S89. Prior-art boundary: METHOD FOUNDATIONAL.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Dai, Steve; Zhou, Yuan; Zhang, Hang; Ustun, Ecenur; Young, Evangeline F.Y.; Zhang, Zhiru
- Year / venue: 2018 / FCCM
- DOI: 10.1109/FCCM.2018.00029 · URL: https://doi.org/10.1109/FCCM.2018.00029
- Metadata source: PDF first page (title/authors; no venue on PDF) + web search (CUHK research portal / Semantic Scholar) for venue, year, DOI

## PDF provenance
- Status: `LOCAL_EXISTING` (accepted)
- Canonical path: `related_work/papers/multifidelity/RW0036_Dai2018_QoRML_FCCM_accepted.pdf`
- SHA-256: `a51995b15e309d66eb2b70240e1dbe9dfaeef148d74983dcdae633590db0854b`
- Source: /home/benyamin/Desktop/Library/Fast and Accurate Estimation of Quality of Results in High-Level Synthesis with Machine Learning.pdf

## Code / dataset / artifact provenance
Dataset stated as publicly available on authors' website (URL not given in the PDF)

## 1. Research question
HLS-reported resource and timing estimates deviate strongly from post-implementation QoR (e.g., 125% LUT and 98% FF relative error), preventing meaningful DSE without running implementation.

## 2. Problem setting
Predict post-implementation (post place-and-route) resource usage and timing closure of HLS designs from features in HLS reports.

## 3. Search space
NOT_APPLICABLE (estimator)

## 4. Evaluation method
Held-out test set (20%) of post-implementation results from Vivado implementation; random-permutation cross-validation.

## 5. Benchmarks
CHStone, MachSuite, S2CBench, Rosetta (65 designs; clock periods 1,2,3,5,10 ns)

## 6. Hardware
Xilinx Zynq-7000, Artix-7, Kintex-7, Virtex-7 (implementation targets)

## 7. Toolchain
Xilinx Vivado (HLS and implementation) 2017.1; scikit-learn; XGBoost

## 8. Metrics
Relative absolute error (RAE) for LUT/FF/DSP/BRAM; timing classification error rate; feature importance

## 9. Baselines
HLS tool built-in estimates; Lasso vs ANN vs XGBoost; multi-task variants

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: models reduce HLS estimation errors by up to 138%; XGBoost achieves less than 5% error for LUT and FF and less than 1% for DSP and BRAM in a majority of single-task cases, with millisecond inference.

## 11. Limitations
Requires running HLS to obtain features; dataset lacks directive variation (noted as future augmentation); random split rather than unseen-design evaluation; older 7-series devices.

## 12. What the paper does NOT evaluate
Use inside a DSE loop; latency/throughput prediction; power; unseen-kernel generalization; multi-kernel interactions.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S06 S21 S59 S61 S72 S78 S81
- Partial (dimension = PARTIAL): S10 S11 S32 S34 S73 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Estimator |
| measured interactions | NO | Not studied |
| staged evaluation | PARTIAL | Positions HLS-report features as a cheap stage to predict post-implementation QoR |
| adaptive evidence acquisition | NO | No acquisition loop |
| cost/fidelity modeling | YES | Explicitly models the gap between low-fidelity HLS estimates and high-fidelity implementation results |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | YES | Labels are post-implementation (place and route) resource and timing |
| multi-benchmark transfer | PARTIAL | Four device families and many designs; random split |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not estimated |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | PARTIAL | Memory words/banks features used for BRAM prediction |

## 14. Possible overlap
PARTIAL OVERLAP on: cost/fidelity modeling; physical implementation in the loop

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: measured interactions; adaptive evidence acquisition; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Dataset stated as publicly available on authors' website (URL not given in the PDF)

## Open questions / reviewer notes
PDF has no venue header; venue/DOI confirmed via web search. Local filename lacks the trailing asterisk from the task list. pdf_version assumed 'accepted' (author-formatted version without IEEE header).
