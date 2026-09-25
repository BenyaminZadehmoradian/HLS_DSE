# RW0055 — The Architectural Sustainability Indicator

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Roelandts, Jaime; Naithani, Ajeya; Eeckhout, Lieven
- Year / venue: 2025 / IEEE CAL
- DOI: NOT_REPORTED · URL: https://biblio.ugent.be/publication/01KAV3F3SE1E4HHJ6DXWD7JE28
- Metadata source: PDF (title/authors, no venue header) + web search (IEEE Computer Architecture Letters vol. 24 no. 2, pp. 205-208, 2025; Ghent University biblio record)

## PDF provenance
- Status: `LOCAL_EXISTING` (accepted)
- Canonical path: `related_work/papers/energy_sustainability/RW0055_Roelandts2025_ASI_CAL_accepted.pdf`
- SHA-256: `167ee80bbf3419e5aaa97c6c08e8e5c241134b23488d46a6a1cea72a3e08afe4`
- Source: /home/benyamin/Desktop/Sustainable_Design_Explorer/Papers/The_Architectural_Sustainability_Indicator_2025.pdf

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Need a single metric telling architects whether a design is strongly, weakly or un-sustainable (robust to rebound effects) and how to improve it.

## 2. Problem setting
Relative sustainability assessment of microarchitecture design points against a reference using FOCAL proxies.

## 3. Search space
SVR vector length (8-128) x LLC size (64-1024 KiB)

## 4. Evaluation method
Sniper v7.3 timing simulation + McPAT v1.0 (22 nm) area/power

## 5. Benchmarks
Database and graph analytics workloads from the SVR paper

## 6. Hardware
Simulated Arm Cortex-A510-like in-order core with 512 KiB LLC

## 7. Toolchain
Sniper v7.3 (modified), McPAT v1.0

## 8. Metrics
ASI, speedup, NCF

## 9. Baselines
Reference in-order core without SVR (512 KiB LLC)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: default SVR (3.3x speedup) is weakly sustainable with 38% lower ASI; SVR-16 with 128 KiB LLC is strongly sustainable with reference-level ASI while keeping 3.2x speedup.

## 11. Limitations
Relative metric specific to reference design and workloads; first-order proxies; single case study; alpha fixed at 0.8.

## 12. What the paper does NOT evaluate
FPGAs/accelerators; lifecycle reconfiguration; HLS.

## 13. Relationship to our Studies
- Direct (dimension = YES): S19 S20
- Partial (dimension = PARTIAL): S02 S36 S37 S43 S45 S56 S73 S85 S86 S92 S94

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE |  |
| measured interactions | PARTIAL | Interaction of vector length and LLC size on ASI shown. |
| staged evaluation | NOT_APPLICABLE |  |
| adaptive evidence acquisition | NOT_APPLICABLE |  |
| cost/fidelity modeling | NO |  |
| lifecycle/configuration cost | PARTIAL | Embodied vs operational weighting via alpha. |
| physical implementation in the loop | NO |  |
| multi-benchmark transfer | NOT_APPLICABLE |  |
| decision/Pareto stability | PARTIAL | Classification robust to rebound effect (fixed-work vs fixed-time). |
| energy/power | YES | McPAT power. |
| CPU-FPGA interaction | NOT_APPLICABLE |  |
| memory/data movement | PARTIAL | LLC size and prefetching studied. |

## 14. Possible overlap
PARTIAL OVERLAP on: energy/power

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Local 4-page PDF has no journal header (likely accepted/author version). DOI not found in search; left empty. Venue from web search. A related extended work 'ASI: A Unifying Metric to Assess and Improve Processor Microarchitecture Sustainability' appears in Ghent biblio (different paper).
