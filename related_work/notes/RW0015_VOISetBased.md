# RW0015 — A value of information methodology for multiobjective decisions in quantitative set-based design

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_ABSTRACT_ONLY`.

## Bibliographic identity
- Authors: Shallcross, Nicholas J.; Parnell, Gregory S.; Pohl, Ed; Goerger, Simon R.
- Year / venue: 2021 / Systems Engineering (Wiley/INCOSE) 24(6):409-424
- DOI: 10.1002/sys.21593 · URL: https://doi.org/10.1002/sys.21593
- Metadata source: Crossref + Semantic Scholar/OpenAlex abstract

## PDF provenance
- Status: `METADATA_ONLY_PAYWALLED` (no PDF)
- Canonical path: `none`
- SHA-256: `none`
- Source: none

## Code / dataset / artifact provenance
NOT_REPORTED

## 1. Research question
Lack of quantitative methodologies to inform design-maturation and convergence decisions in set-based design (SBD) for complex systems under multiobjective uncertainty.

## 2. Problem setting
Sequential multiobjective system-design decisions under uncertainty within set-based design, deciding whether to use costly higher-resolution models.

## 3. Search space
Sets of system design alternatives / design options; choice among higher-resolution models (details NOT_REPORTED in abstract)

## 4. Evaluation method
Demonstration on an SBD design example (details NOT_REPORTED in abstract; full text not reviewed)

## 5. Benchmarks
NOT_REPORTED

## 6. Hardware
NOT_APPLICABLE

## 7. Toolchain
NOT_REPORTED

## 8. Metrics
Value of information (multiobjective); others NOT_REPORTED

## 9. Baselines
Traditional point-based design (as contrast; per abstract)

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): presents a VOI-based methodology for multiobjective decisions applicable to SBD, and demonstrates 'the inherent issues associated with premature decisions and traditional point-based design approaches which run the risk of selecting an alternative that later proves infeasible.'

## 11. Limitations
NOT_REPORTED (abstract only).

## 12. What the paper does NOT evaluate
No hardware/HLS; no automated search/optimizer loop evident from abstract; no physical implementation, energy, CPU-FPGA or memory aspects.

## 13. Relationship to our Studies
- Direct (dimension = YES): S04 S05 S06 S20 S21 S23 S33 S72
- Partial (dimension = PARTIAL): S32 S34 S43 S45 S88 S92

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract only. |
| measured interactions | NOT_REPORTED | Abstract only. |
| staged evaluation | PARTIAL | Design maturation from low- to higher-resolution models (abstract). |
| adaptive evidence acquisition | YES | VOI decides whether/which higher-resolution model to use (abstract). |
| cost/fidelity modeling | YES | Compares high-resolution models given usage cost and information value (abstract). |
| lifecycle/configuration cost | NOT_REPORTED | Abstract mentions affordability/cost objectives generally; not verified. |
| physical implementation in the loop | NOT_APPLICABLE | No hardware. |
| multi-benchmark transfer | NOT_REPORTED | Abstract only. |
| decision/Pareto stability | PARTIAL | Addresses risk of premature decisions / later-infeasible alternatives (abstract). |
| energy/power | NOT_APPLICABLE | No hardware. |
| CPU-FPGA interaction | NOT_APPLICABLE | No hardware. |
| memory/data movement | NOT_APPLICABLE | No hardware. |

## 14. Possible overlap
PARTIAL OVERLAP on: adaptive evidence acquisition; cost/fidelity modeling

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_REPORTED

## Open questions / reviewer notes
Verified venue: Systems Engineering 24(6), 2021 (published online 2021-07-22). Unpaywall/OpenAlex list no OA copy. The same authors published a companion paper in the same issue: 'Using value of information in quantitative set-based design', Systems Engineering 24(6):439-455, DOI 10.1002/sys.21595; do not confuse the two. Related content likely in Shallcross's University of Arkansas dissertation 'Quantitative Set-Based Design for Complex System Development' (scholarworks.uark.edu), which was not used as the source.
