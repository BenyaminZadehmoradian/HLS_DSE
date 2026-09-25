# RW0062 — HLSFactory-Agent: Large-Scale Agentic HLS Dataset Construction from Academic and Open-Source Projects

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Chandana, Kaushik; Imperatori, Jay; Shukla, Tanmay; Zhou, Justin; Abi-Karam, Stefan; Hao, Callie
- Year / venue: 2026 / OSCAR Workshop @ ISCA (arXiv)
- DOI: 10.48550/arXiv.2609.09519 · URL: https://arxiv.org/abs/2609.09519
- Metadata source: PDF first page + arXiv abs page (comment: presented at OSCAR workshop at ISCA 2026)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/other/RW0062_Chandana2026_HLSFactoryAgent_OSCAR_arxiv.pdf`
- SHA-256: `4a91ff723c1f02b08042786f649eb3b6109be3e0f3c3bd34e5755a6003c4e8ba`
- Source: https://arxiv.org/pdf/2609.09519

## Code / dataset / artifact provenance
Open source: https://github.com/sharc-lab/hlsfactory-agent

## 1. Research question
Curating large, diverse HLS design datasets requires manual location and extraction of standalone designs from academic and open-source codebases.

## 2. Problem setting
Automated LLM-agent extraction of standalone Vitis-HLS-compatible projects from GitHub repositories for dataset construction (feeding HLSFactory/HLS-Eval).

## 3. Search space
NOT_APPLICABLE

## 4. Evaluation method
Extracted designs validated by running generated synth.tcl in Vitis HLS synthesis (pass only if synthesis completes).

## 5. Benchmarks
26 public repositories (e.g., fpgaconvnet-hls, S2CBench, balor, DP-HLS, HP-FFT-HLS, CLINK, ThunderGP, gemm_hls, NN2FPGA, SFU-HiAccel repos)

## 6. Hardware
NOT_REPORTED (target part set in synth.tcl)

## 7. Toolchain
Pi agent framework, DeepSeek-V4-Flash LLM, Clang syntax check, Vitis HLS (version NOT_REPORTED), Docker

## 8. Metrics
Number of extracted/passing/failing designs per repo; inference cost and agent runtime per repo

## 9. Baselines
NOT_REPORTED

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 'Our evaluation run extracts 271 candidate designs across 26 repositories: 130 passing and 141 failing'; five repositories yielded no designs.

## 11. Limitations
Short 2-page workshop paper with initial results; validation is synthesis-completion only (no functional or QoR check); human review still needed for paper/repo discovery; Vitis synthesis not yet in the agent loop.

## 12. What the paper does NOT evaluate
QoR, functional correctness of extracted designs, DSE, energy, physical implementation.

## 13. Relationship to our Studies
- Direct (dimension = YES): none
- Partial (dimension = PARTIAL): S04 S06 S21 S32 S34 S72 S88

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE | Dataset construction tool. |
| measured interactions | NOT_APPLICABLE | Dataset construction tool. |
| staged evaluation | PARTIAL | Clang syntax-only check inside agent, then external Vitis HLS synthesis validation. |
| adaptive evidence acquisition | NOT_APPLICABLE | Not an optimization method. |
| cost/fidelity modeling | PARTIAL | Reports inference cost and runtime per repository; suggests designs-per-dollar metric. |
| lifecycle/configuration cost | NOT_APPLICABLE | Not addressed. |
| physical implementation in the loop | NO | HLS synthesis only. |
| multi-benchmark transfer | NOT_APPLICABLE | Dataset tool. |
| decision/Pareto stability | NOT_APPLICABLE | Dataset tool. |
| energy/power | NO | Not addressed. |
| CPU-FPGA interaction | NO | Not addressed. |
| memory/data movement | NO | Not addressed. |

## 14. Possible overlap
POTENTIAL OVERLAP (partial evidence) on: staged evaluation; cost/fidelity modeling

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). Open source: https://github.com/sharc-lab/hlsfactory-agent

## Open questions / reviewer notes
Hint said ~2025; actual arXiv posting Sep 2026 (workshop at ISCA 2026). Related but distinct: HLSFactory (MLCAD 2024, arXiv 2405.00820) and HLS-Eval (ICLAD 2025). Venue is a non-archival workshop; DOI given is the arXiv DOI.
