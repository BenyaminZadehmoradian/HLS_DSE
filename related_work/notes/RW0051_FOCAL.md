# RW0051 — FOCAL: A First-Order Carbon Model to Assess Processor Sustainability

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Eeckhout, Lieven
- Year / venue: 2024 / ASPLOS
- DOI: 10.1145/3620665.3640415 · URL: https://doi.org/10.1145/3620665.3640415
- Metadata source: PDF first page (ACM reference format, ASPLOS '24 Vol. 2)

## PDF provenance
- Status: `LOCAL_EXISTING` (published)
- Canonical path: `related_work/papers/energy_sustainability/RW0051_Eeckhout2024_FOCAL_ASPLOS.pdf`
- SHA-256: `2127c50699eeafdbc493ae513d6e7229b0be80e9b8628000def7f6147efda6ab`
- Source: /home/benyamin/Desktop/Sustainable_Design_Explorer/Papers/FOCAL_A_First-Order_Carbon_Model_to_Assess_Processor_Sustainability_2024.pdf

## Code / dataset / artifact provenance
NOT_REPORTED (analytical model fully specified in paper)

## 1. Research question
How can computer architects reason about processor sustainability despite pervasive uncertainty in carbon data?

## 2. Problem setting
Early-stage, first-order analytical carbon modeling of processor design choices.

## 3. Search space
NOT_APPLICABLE (analyses archetypal mechanisms: multicore, heterogeneity, hardware acceleration, dark silicon, caching, OoO vs in-order, branch prediction, runahead, DVFS, turbo, pipeline gating, die shrink)

## 4. Evaluation method
Analytical modeling with literature/first-principles inputs (e.g., Pollack's rule); case study combining with chip-manufacturing carbon data across technology nodes.

## 5. Benchmarks
NOT_APPLICABLE

## 6. Hardware
NOT_APPLICABLE

## 7. Toolchain
NOT_REPORTED

## 8. Metrics
NCF under fixed-work and fixed-time scenarios

## 9. Baselines
Reference designs within each analysis (e.g., single core, OoO core without accelerator)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: multicore, low-complexity cores, DVFS, pipeline gating, die shrink are strongly sustainable; heterogeneity, speculation and parallelizing software weakly sustainable; turboboosting and dark silicon not sustainable; hardware acceleration strongly sustainable if operational footprint dominates, otherwise only if heavily used (Finding #6).

## 11. Limitations
First-order proxies; less detailed than ACT and not for fine-grained trade-offs; ignores market dynamics/Jevons effects beyond fixed-time scenario; validation hard due to data scarcity.

## 12. What the paper does NOT evaluate
FPGAs/HLS; reconfiguration cost; measured designs; design-space search.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20 S85 S86 S94
- Partial (dimension = PARTIAL): S04 S06 S21 S43 S45 S72 S73 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE |  |
| measured interactions | NOT_APPLICABLE |  |
| staged evaluation | NOT_APPLICABLE |  |
| adaptive evidence acquisition | NOT_APPLICABLE |  |
| cost/fidelity modeling | PARTIAL | Carbon-data uncertainty handled via alpha sweeps and fixed-work/fixed-time scenarios. |
| lifecycle/configuration cost | YES | Embodied vs operational footprint weighting; accelerator usage amortization. |
| physical implementation in the loop | NOT_APPLICABLE |  |
| multi-benchmark transfer | NOT_APPLICABLE |  |
| decision/Pareto stability | PARTIAL | Strong/weak sustainability classification is robustness of decision across scenarios. |
| energy/power | YES | Energy and power are operational proxies. |
| CPU-FPGA interaction | NO |  |
| memory/data movement | PARTIAL | Caching analysed as design choice. |

## 14. Possible overlap
PARTIAL OVERLAP on: lifecycle/configuration cost; energy/power

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED (analytical model fully specified in paper)

## Open questions / reviewer notes
none
