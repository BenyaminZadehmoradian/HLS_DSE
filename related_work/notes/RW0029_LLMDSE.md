# RW0029 — LLM-DSE: Searching Accelerator Parameters with LLM Agents

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Wang, Hanyu; Wu, Xinrui; Ding, Zijian; Zheng, Su; Wang, Chengyue; Prakriya, Neha; Nowatzki, Tony; Sun, Yizhou; Cong, Jason
- Year / venue: 2025 / arXiv
- DOI: 10.48550/arXiv.2505.12188 · URL: https://arxiv.org/abs/2505.12188
- Metadata source: PDF first page (arXiv:2505.12188v3, 21 Nov 2025) + arXiv abs page via web search for author order

## PDF provenance
- Status: `LOCAL_EXISTING` (arxiv)
- Canonical path: `related_work/papers/hls_dse/RW0029_Wang2025_LLMDSE_arXiv.pdf`
- SHA-256: `5d75eca169c909724154fc3604f43a14b8dde95f3929db75a01da720f2bdeb56`
- Source: /home/benyamin/Desktop/Library/LLM-DSE: Searching Accelerator Parameters with LLM Agents.pdf

## Code / dataset / artifact provenance
Code: https://github.com/Nozidoali/LLM-DSE

## 1. Research question
Heuristic and learning-based HLS directive optimizers generalize poorly to new kernels and are sample-inefficient given hour-long synthesis per design and a huge, non-smooth design space.

## 2. Problem setting
Closed-loop HLS directive search per kernel under an 8-hour budget, minimizing cycle count with resource utilization below 80% (Merlin backend; ablations on Vitis and Cadence Stratus).

## 3. Search space
Merlin PIPELINE/PARALLEL/TILE parameters per loop (~1e13 points); array type/partition added for Stratus ASIC flow

## 4. Evaluation method
Actual HLS synthesis (Merlin end-to-end) reports for every evaluated design within an 8-hour search; two runs per experiment.

## 5. Benchmarks
10 HLSyn kernels from ML4HLS contest stage 2 (e.g., syr2k, atax-medium, jacobi-2d); 4 Rosetta programs (Conv2D, Spam Filter, KNN, 3D Rendering)

## 6. Hardware
NOT_REPORTED (FPGA target not stated in main text); ASIC via Stratus in appendix

## 7. Toolchain
AMD/Xilinx Merlin Compiler; Vitis; Cadence Stratus (appendix); GPT-4o via OpenAI API

## 8. Metrics
Latency (cycles), speedup, win ratio, token consumption/cost

## 9. Baselines
AutoDSE (8h, 24h), HARP (trained on 8h/24h AutoDSE data), RALAD, zero/one-shot LLM direct generation, ablated agent variants

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: speedups of 2.55x, 1.60x and 1.16x over AutoDSE-8, AutoDSE-24 and HARP-24 on HLSyn; 1.22x geometric-mean over the heuristic method on Rosetta; GPT-4o cost 1-7 USD per 8-hour run.

## 11. Limitations
Only two runs per experiment; relies on proprietary LLM; small kernels in HLSyn; per-kernel search from scratch with hours-long evaluations.

## 12. What the paper does NOT evaluate
Post-route/on-board QoR; power; multi-kernel joint optimization; formal sample-efficiency analysis vs Bayesian optimization.

## 13. Relationship to our Studies
- Direct (dimension = YES): S05 S20 S23 S33
- Partial (dimension = PARTIAL): S02 S04 S06 S10 S11 S21 S32 S34 S36 S37 S56 S71 S72 S88 S90

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NO | Per-kernel search |
| measured interactions | PARTIAL | Critic compares single-parameter changes to isolate effects |
| staged evaluation | PARTIAL | Two-stage proposal filtering (specialists then arbitrator) before synthesis |
| adaptive evidence acquisition | YES | LLM agents choose which designs to synthesize next based on feedback and remaining budget |
| cost/fidelity modeling | PARTIAL | Arbitrator predicts performance/resource/compile time; token cost reported |
| lifecycle/configuration cost | NO | Not addressed |
| physical implementation in the loop | NO | HLS reports only |
| multi-benchmark transfer | PARTIAL | Evaluated across HLSyn, Rosetta and different toolchains without retraining |
| decision/Pareto stability | NO | Not studied |
| energy/power | NO | Not measured |
| CPU-FPGA interaction | NO | Not modeled |
| memory/data movement | NO | Not modeled |

## 14. Possible overlap
PARTIAL OVERLAP on: adaptive evidence acquisition

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: joint (multi-kernel/component) evaluation; decision/Pareto stability; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Code: https://github.com/Nozidoali/LLM-DSE

## Open questions / reviewer notes
PDF author block order is scrambled by text extraction; order taken from arXiv listing. Peer-reviewed venue not confirmed.
