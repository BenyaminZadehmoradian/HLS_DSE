# RW0079 — ZyCAP: Efficient Partial Reconfiguration Management on the Xilinx Zynq

> **Relevance (2026-09-25 web-search update): HOLD** — Measured Zynq (ZedBoard) reconfiguration throughput: PCAP ~128 MB/s, AXI_HWICAP 19 MB/s, ZyCAP 382 MB/s; full Zynq-7020 bitstream 4,045,564 bytes. Source for programming-cost terms. Primary Studies: S85 S86 S12. Prior-art boundary: RELEVANT BUT DIFFERENT (candidate).
> **Identity:** VERIFIED_WEB.
> **HOLD:** reviewed from the abstract/search highlights only. Classification to be revisited after full-text review.

> Literature evidence only (`LITERATURE_REPORTED`). Nothing here is an HLS-DSE measurement or a novelty claim.
> Review status: `REVIEWED_ABSTRACT_ONLY`. Source: Web search 2026-09-25 (Consensus, Exa, Firecrawl research index, WebSearch); abstract/highlights only.

## Bibliographic identity
- Authors: Vipin, Kizheppatt; Fahmy, Suhaib A.
- Year / venue: 2014 / IEEE Embedded Systems Letters 6(3):41-44
- DOI: 10.1109/LES.2014.2314390 · URL: https://doi.org/10.1109/LES.2014.2314390

## PDF provenance
- Status: `METADATA_ONLY` (no PDF held) · Availability: OPEN_COPY_AVAILABLE (author site; not downloaded)

## 1. Research question
PR on Zynq is inefficient or blocks the processor with vendor methods.

## 2. Method
Custom PR controller (soft DMA + ICAP manager) with software driver; overlapped reconfiguration.

## 3. Benchmarks / hardware / metrics
- Benchmarks: Image processing pipeline
- Hardware: ZedBoard (Zynq-7020)
- Metrics: Reconfiguration throughput; application throughput

## 4. Main findings (as reported by the authors)
LITERATURE_REPORTED (full text via search highlights): ZyCAP 382 MB/s (95.5% of theoretical) vs PCAP 128 MB/s; full bitstream 4,045,564 bytes; partial 1,018,080 bytes.

## 5. Limitations
NOT_REPORTED (abstract only).

## 6. Relationship to our Studies (S85 S86 S12)

| Dimension | Value | Evidence note |
|---|---|---|
| joint (multi-kernel/component) evaluation | NOT_REPORTED | Abstract/highlights only. |
| measured interactions | NOT_REPORTED | Abstract/highlights only. |
| staged evaluation | NOT_REPORTED | Abstract/highlights only. |
| adaptive evidence acquisition | NOT_REPORTED | Abstract/highlights only. |
| cost/fidelity modeling | NOT_REPORTED | Abstract/highlights only. |
| lifecycle/configuration cost | YES | Abstract/highlights only. |
| physical implementation in the loop | YES | Abstract/highlights only. |
| multi-benchmark transfer | NOT_REPORTED | Abstract/highlights only. |
| decision/Pareto stability | NOT_REPORTED | Abstract/highlights only. |
| energy/power | NOT_REPORTED | Abstract/highlights only. |
| CPU-FPGA interaction | YES | Abstract/highlights only. |
| memory/data movement | PARTIAL | Abstract/highlights only. |

## 7. Possible overlap
RELEVANT BUT DIFFERENT (candidate)

## 8. Reproducibility status
Not reproduced by HLS-DSE (`REPRODUCED` would require an S71 run).
