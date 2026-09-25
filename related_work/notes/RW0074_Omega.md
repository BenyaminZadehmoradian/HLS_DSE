# RW0074 — Omega: A Hardware-Software Framework for Complete Design Space Exploration of FPGA-Based Heterogeneous Multi-Core SoCs

> **Relevance (2026-09-25 web-search update): HOLD** — Exhaustive (complete) DSE of FPGA multi-core SoCs with accelerators for up to five applications, using dynamic partial reconfiguration to make on-board evaluation cheap; positioned as a golden model for heuristics. Methodological precedent for S04/S97 oracles. Primary Studies: S04 S97 S85. Prior-art boundary: PARTIAL OVERLAP (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Montanaro, Gabriele; Galimberti, Andrea; Zoni, Davide
- Year / venue: 2026 / IEEE Transactions on Computers 75(2):435-447
- DOI: 10.1109/TC.2025.3624704 · URL: https://ieeexplore.ieee.org/document/11216106/

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: NOT_CHECKED (code: github.com/hardware-fab/Omega)

## 1. Research question
DSE of heterogeneous multi-core FPGA SoCs is too large for heuristic methods to guarantee optimality.

## 2. Method
Exhaustive exploration accelerated by dynamic partial reconfiguration on commercial FPGA platforms; open-source ecosystem.

## 3. Benchmarks / hardware / metrics
- Benchmarks: 16-core SoCs with accelerators for up to five applications
- Hardware: Commercial FPGA platforms (details NOT_REPORTED in abstract)
- Metrics: Optimality; DSE speedup

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (abstract): 29x average DSE speedup vs traditional techniques while guaranteeing solution optimality.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S04 S97 S85)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | YES | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | NOT_REPORTED | Abstract/highlights only. |
| cost/fidelity modeling | NOT_REPORTED | Abstract/highlights only. |
| lifecycle/configuration cost | PARTIAL | Abstract/highlights only. |
| physical implementation in the loop | YES | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | PARTIAL | Abstract/highlights only. |
| CPU-FPGA interaction | PARTIAL | Abstract/highlights only. |
| memory/data movement | NOT_REPORTED | Abstract/highlights only. |

## 7. Possible overlap
PARTIAL OVERLAP (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
