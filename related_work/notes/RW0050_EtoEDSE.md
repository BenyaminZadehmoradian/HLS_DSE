# RW0050 — System-Level Design Space Exploration for High-Level Synthesis under End-to-End Latency Constraints

> **Relevance (2026-09-25 correction audit): CORE** — Component HLS alternatives combined and evaluated at system level under end-to-end latency; joint-composition boundary. Primary Studies: S15 S65 S66. Prior-art boundary: PARTIAL OVERLAP.
> **Identity:** Key renamed from placeholder ENERGY2.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Liao, Yuchao; Adegbija, Tosiron; Lysecky, Roman
- Year / venue: 2024 / IEEE TCAD
- DOI: 10.1109/TCAD.2024.3471892 · URL: https://doi.org/10.1109/TCAD.2024.3471892
- Metadata source: PDF first page (arXiv v2) + arXiv abs page ('Accepted in IEEE TCAD') + OpenAlex (DOI)

## PDF provenance
- Status: `DOWNLOADED_OPEN_ACCESS` (arxiv)
- Canonical path: `related_work/papers/core/RW0050_Liao2024_EtoEDSE_TCAD_arxiv.pdf`
- SHA-256: `db1a8c2a44ff9a06e54d4623a017c66538710e4cafbfbed7d56a36489dedd850`
- Source: https://arxiv.org/pdf/2408.10431

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
HLS DSE usually optimizes components individually and ignores end-to-end latency across interacting components of multi-component embedded systems.

## 2. Problem setting
System-level HLS DSE for multi-component FPGA embedded systems (PSMs with multiple computational components and handshakes) minimizing energy and area under variable timing and end-to-end latency constraints.

## 3. Search space
Per-component HLS design alternatives (MCC alternatives, e.g., unrolling), per-component clock frequencies (5 MHz steps) under a frequency-pin limit, FSM/handshake frequencies; 5.29e+128 configurations for the case study

## 4. Evaluation method
Estimated energy (from tool power estimates scaled with frequency) and area (FF+LUT) of HLS-generated alternatives combined analytically at system level; worst-case EtoE latency model; AEDRS vs merged reference front.

## 5. Benchmarks
Autonomous driving subsystem (10 PSMs, 18 MCCs, 490 MCC alternatives)

## 6. Hardware
Xilinx Artix-7 XC7A100T

## 7. Toolchain
HLS tools (Vitis/Vivado mentioned; versions NOT_REPORTED); EtoE-DSE in C++ on Intel Xeon, 48 threads

## 8. Metrics
Energy (mJ), area (FF+LUT), EtoE latency, AEDRS (modified ADRS), design space reduction, execution time

## 9. Baselines
GA and SA from prior HLS DSE work (ACO attempted but failed to converge); EtoE-DSE unsegmented/serial/parallel variants

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: 'improving the quality of results by up to 89.26%' vs prior DSE while identifying energy/area Pareto-optimal configurations; FDSS reduces the design space by ~2.15e+55x without QoR loss; parallel variant cuts execution time by 68.49%.

## 11. Limitations
Worst-case EtoE latency estimation (stated); single case study; energy/area estimated rather than measured; reference front built from merged runs (no exhaustive ground truth).

## 12. What the paper does NOT evaluate
On-board energy measurement, post-route timing effects of multi-component integration, CPU-FPGA interaction, cross-application transfer, stability of fronts beyond 5 runs.

## 13. Relationship to our Studies
- Direct (dimension = YES): S07 S15 S19 S20 S65
- Partial (dimension = PARTIAL): S02 S32 S34 S36 S37 S43 S45 S56 S73 S88 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Component alternatives combined and evaluated at system level under EtoE latency. |
| measured interactions | PARTIAL | Inter-component latency paths and handshakes modelled analytically; interactions not measured on hardware. |
| staged evaluation | PARTIAL | Component-level pruning (FDSS) before system-level GA search. |
| adaptive evidence acquisition | NO | No adaptive tool-run acquisition; GA over precomputed alternatives. |
| cost/fidelity modeling | NO | Execution time reported but not modelled. |
| lifecycle/configuration cost | NO | Not addressed. |
| physical implementation in the loop | NOT_REPORTED | Paper says systems were implemented on an FPGA for evaluation, but DSE metrics are tool estimates; extent of post-route use unclear. |
| multi-benchmark transfer | NO | Single system case study. |
| decision/Pareto stability | PARTIAL | AEDRS reported over five runs per configuration. |
| energy/power | YES | Energy is a primary objective (weighted 2:1 over area in fitness). |
| CPU-FPGA interaction | NO | All-FPGA components. |
| memory/data movement | PARTIAL | Handshake-based data transfer between components modelled for latency only. |

## 14. Possible overlap
PARTIAL OVERLAP on: joint (multi-kernel/component) evaluation; energy/power

## 15. Possible research gap
POTENTIAL GAP relative to this paper (not a novelty claim): not reported/evaluated here: adaptive evidence acquisition; lifecycle/configuration cost

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
ENERGY slot justification: energy-aware HLS DSE that is also multi-component/system-level, i.e., energy objective plus joint evaluation of interacting HLS components, directly relevant to concurrent multi-kernel HLS-DSE. Downloaded version is arXiv v2 (accepted manuscript for TCAD); DOI from OpenAlex.
