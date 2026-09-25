# RW0065 — Efficient System-Level Design Space Exploration for High-Level Synthesis Using Pareto-Optimal Subspace Pruning

> **Relevance (2026-09-25 web-search update): HOLD** — Predecessor of RW0050 EtoE-DSE: prunes the system-level space using component-level Pareto-optimal subspaces, i.e. assumes local Pareto membership survives composition. Primary Studies: S97 S15. Prior-art boundary: POTENTIAL OVERLAP.
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Liao, Yuchao; Adegbija, Tosiron; Lysecky, Roman
- Year / venue: 2023 / ASP-DAC 2023
- DOI: 10.1145/3566097.3567841 · URL: https://doi.org/10.1145/3566097.3567841

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: NOT_CHECKED

## 1. Research question
System-level Pareto space is orders of magnitude larger than component-level spaces.

## 2. Method
Pareto-optimal subspace pruning of component implementations + elitist genetic algorithm (PG-DSE) at post-synthesis stage.

## 3. Benchmarks / hardware / metrics
- Benchmarks: ADAS subsystem + three synthetic systems
- Hardware: NOT_REPORTED in abstract
- Metrics: Pareto quality vs prior work

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): reduces the design space by several orders of magnitude and improves result quality by 58.1x on average vs prior work.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S97 S15)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | PARTIAL | Abstract/highlights only. |
| adaptive evidence acquisition | NOT_REPORTED | Abstract/highlights only. |
| cost/fidelity modeling | NOT_REPORTED | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | NOT_REPORTED | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_REPORTED | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
POTENTIAL OVERLAP

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
