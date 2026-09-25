# RW0059 — The Sustainability Gap for Computing: Quo Vadis?

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Generated 2026-09-25 from the full-text/abstract review recorded in `related_work/RELATED_WORK_REGISTRY.csv`; review status: `REVIEWED_FULL_TEXT`.

## Bibliographic identity
- Authors: Eeckhout, Lieven
- Year / venue: 2025 / Communications of the ACM
- DOI: 10.1145/3699595 · URL: https://doi.org/10.1145/3699595
- Metadata source: PDF (title/author, 2024 preprint template with placeholder DOI) + web search (CACM vol. 68 no. 3, 2025, DOI 10.1145/3699595)

## PDF provenance
- Status: `LOCAL_EXISTING` (preprint)
- Canonical path: `related_work/papers/energy_sustainability/RW0059_Eeckhout2025_SustGap_CACM_preprint.pdf`
- SHA-256: `c9d6ad1dce432165717c63ae744e4c32244dce0c39a7592f0ff08a2720dadcc2`
- Source: /home/benyamin/Desktop/Sustainable_Design_Explorer/Papers/The_Sustainability_Gap_for_Computing_Quo_Vadis_2024.pdf

## Code / dataset / artifact provenance
NOT_APPLICABLE

## 1. Research question
How large is the gap between computing's projected carbon footprint and the Paris agreement given population and affluence growth?

## 2. Problem setting
Macro-level IPAT-style analysis of computing's carbon footprint (population x devices per person x carbon per device).

## 3. Search space
NOT_APPLICABLE

## 4. Evaluation method
Analytical projection + published product carbon footprint reports

## 5. Benchmarks
NOT_APPLICABLE

## 6. Hardware
NOT_APPLICABLE (consumer devices from vendor reports)

## 7. Toolchain
NOT_APPLICABLE

## 8. Metrics
Per-device carbon footprint CAGR, sustainability gap

## 9. Baselines
Status quo per-device footprint vs Paris-agreement trajectory

## 10. Main findings (as reported by the authors)
LITERATURE_REPORTED: keeping per-device footprint constant leads to a 5.4x gap vs the Paris agreement within a decade; closing it requires reducing per-device footprint by 15.5% per year; observed vendor reductions appear insufficient.

## 11. Limitations
Relies on a select number of vendor LCA reports; aggregate growth assumptions.

## 12. What the paper does NOT evaluate
Any design-level method, FPGAs, DSE.

## 13. Relationship to our Studies
- Direct (dimension = YES): none
- Partial (dimension = PARTIAL): S19 S20 S85 S86 S94

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_APPLICABLE |  |
| measured interactions | NOT_APPLICABLE |  |
| staged evaluation | NOT_APPLICABLE |  |
| adaptive evidence acquisition | NOT_APPLICABLE |  |
| cost/fidelity modeling | NOT_APPLICABLE |  |
| lifecycle/configuration cost | PARTIAL | Embodied + operational per-device lifecycle footprints from vendor reports. |
| physical implementation in the loop | NOT_APPLICABLE |  |
| multi-benchmark transfer | NOT_APPLICABLE |  |
| decision/Pareto stability | NOT_APPLICABLE |  |
| energy/power | PARTIAL | Via operational carbon only. |
| CPU-FPGA interaction | NOT_APPLICABLE |  |
| memory/data movement | NOT_APPLICABLE |  |

## 14. Possible overlap
POTENTIAL OVERLAP (partial evidence) on: lifecycle/configuration cost; energy/power

## 15. Possible research gap
UNRESOLVED

## 16. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run). NOT_APPLICABLE

## Open questions / reviewer notes
Local file is a 2024 preprint (ACM 'Conference'17' template, placeholder DOI); published in CACM 2025 (issue listed as March 2025 vol. 68(3) pp. 70-79 by search; the ASI paper cites it as Feb. 2025).
