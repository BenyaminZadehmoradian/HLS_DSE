# RW0072 — Bayesian Optimization for Efficient Accelerator Synthesis

> **Relevance (2026-09-25 web-search update): HOLD** — Prospector: multi-objective BO for HLS directives compared against random search, simulated annealing and genetic algorithm at equal iterations/wall-clock with HLS + place-and-route evaluation. Primary Studies: S72 S71. Prior-art boundary: PRIOR ART (candidate) for S72.
> **Identity:** PARTIAL (DOI/authors verified; venue not verified).
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Mehrabi, Atefeh; Manocha, Aninda; Lee, Benjamin C.; Sorin, Daniel J.
- Year / venue: 2020 / ACM journal (DOI 10.1145/3427377; venue to verify)
- DOI: 10.1145/3427377 · URL: https://doi.org/10.1145/3427377

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: NOT_CHECKED

## 1. Research question
Efficient HLS/FPGA design space exploration when each point needs synthesis and place-and-route.

## 2. Method
Gaussian-process Bayesian optimization over latency and FPGA resources (1D-5D variants).

## 3. Benchmarks / hardware / metrics
- Benchmarks: fdtd-2d, 2mm, bbgemm, stencil, heat-3d, fft (per highlights)
- Hardware: FPGA (details NOT_REPORTED in highlights)
- Metrics: Pareto frontier; latency; LUT/FF/DSP/BRAM

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (highlights): reveals design optima after evaluating <1% of the space; RS/SA/GA do not accurately describe the Pareto frontier.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S72 S71)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | YES | Abstract/highlights only. |
| cost/fidelity modeling | PARTIAL | Abstract/highlights only. |
| lifecycle/configuration cost | NOT_REPORTED | Abstract/highlights only. |
| physical implementation in the loop | PARTIAL | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | NOT_APPLICABLE | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
PRIOR ART (candidate) for S72

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
