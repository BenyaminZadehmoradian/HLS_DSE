# RW0028 — LIFT: LLM-Based Pragma Insertion for HLS via GNN Supervised Fine-Tuning

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Prakriya, Neha; Ding, Zijian; Sun, Yizhou; Cong, Jason
- Year / venue: 2025 / arXiv
- DOI: 10.48550/arXiv.2504.21187 · URL: https://arxiv.org/abs/2504.21187
- Metadata source: PDF first page (arXiv:2504.21187v1, 29 Apr 2025) + web search (no peer-reviewed venue found)

## PDF provenance
- Status: `LOCAL_EXISTING` (arxiv)
- Canonical path: `related_work/papers/hls_dse/RW0028_Prakriya2025_LIFT_arXiv.pdf`
- SHA-256: `921d038cefa1395c43efbdc3861d2fcbc82ad75aa770927bd764f8ba22bd1bd2`
- Source: /home/benyamin/Desktop/Library/LIFT: LLM-Based Pragma Insertion for HLS via GNN Supervised Fine-Tuning.pdf

## Code / dataset / artifact provenance
NOT_REPORTED (no code URL in paper; uses public HLSyn dataset)

## 1. Research question
Selecting HLS pragmas needs expertise and slow DSE; general LLMs insert poor pragmas and naive fine-tuning fails to capture the microarchitectural impact of small pragma changes.

## 2. Problem setting
Direct prediction of Merlin pragma values for unseen C kernels (single-pass code infilling) to minimize latency within resource limits.

## 3. Search space
Merlin PIPELINE/PARALLEL/TILE factors per loop (HLSyn design spaces)

## 4. Evaluation method
HLS synthesis (Merlin + Vitis) latency of generated designs on 10 held-out kernels; tool-version shift test on Vitis 2021.1.

## 5. Benchmarks
HLSyn (PolyBench and MachSuite kernels; 10 held-out test kernels, e.g., trmm-opt, fdtd-2d-large, gesummv-medium)

## 6. Hardware
AMD/Xilinx Alveo U200 (HLSyn target); training on 8 AMD MI250 GPUs

## 7. Toolchain
Merlin Compiler; Vitis 2020.2 (training labels) and 2021.1 (shift test); HLSyn built with SDx 2018.3/Vitis 2021.1; PyTorch; DeepSeek-Coder 7B

## 8. Metrics
Design latency (cycles), speedup vs baselines, validity

## 9. Baselines
AutoDSE (6h/10h/24h budgets), HARP (1 h DSE), GPT-4o

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: on average LIFT designs are 3.52x faster than AutoDSE-24h, 2.16x faster than HARP and 66x faster than GPT-4o; under Vitis 2020.2->2021.1 shift, 2.74x over HARP; all generated configurations were valid.

## 11. Limitations
No explicit resource modeling (validity learned implicitly from perf=0); evaluated on HLSyn kernels only; single-pass prediction without verification loop; preprint.

## 12. What the paper does NOT evaluate
Post-route QoR; power; multi-kernel designs; non-Merlin pragma sets; statistical variance across runs.

## 13. Relationship to our Studies
- Direct (dimension = YES): S10 S11 S90
- Partial (dimension = PARTIAL): S85 S86 S94

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Single kernels |
| measured interactions | NO | Not studied |
| staged evaluation | NO | Single-pass generation then HLS evaluation |
| adaptive evidence acquisition | NO | No acquisition loop |
| cost/fidelity modeling | NO | Not modeled |
| lifecycle/configuration cost | PARTIAL | Evaluates robustness to HLS tool version change |
| physical implementation in the loop | NO | HLS latency only |
| multi-benchmark transfer | YES | Unseen kernels and tool-version shift |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | NO | Not modeled beyond TILE pragma |

## 14. Possible overlap
PARTIAL OVERLAP on: multi-benchmark transfer

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; measured interactions; adaptive evidence acquisition; staged evaluation; decision/Pareto stability

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (no code URL in paper; uses public HLSyn dataset)

## Open questions / reviewer notes
arXiv DOI constructed from arXiv ID (10.48550 convention). Latency labels come from HLSyn (Vitis 2020.2).
