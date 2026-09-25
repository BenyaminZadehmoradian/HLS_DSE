# HLS-DSE V22.8 — Canonical Implementation-Ready Master

## Status
**READY FOR P0 IMPLEMENTATION — NOT YET SCIENTIFICALLY VALIDATED**

## Core research question
Under a fixed expensive-evaluation budget, does selecting between local and joint evidence improve discovery of the global feasible Pareto frontier in concurrent HLS DSE?

## Scientific core
1. User/benchmark designer defines a bounded legal pragma/design space.
2. Candidate generation creates concrete configurations inside that space.
3. Local evidence is acquired first where appropriate.
4. Joint evidence is acquired selectively when it can change a decision.
5. Physical evidence is treated as a separate fidelity/stage, not conflated with logical interaction.
6. All decisions are evaluated against explicit cost and, where possible, an exhaustive small-space oracle.

## What is not novelty by itself
Automatic pragma generation, Bayesian optimization, GNN/RL, multi-fidelity, Pareto search, multi-kernel deployment, and physical-aware DSE are established research directions and are treated as baselines/components rather than standalone novelty claims.

## Canonical execution chain
Benchmark contract → Pragma Space → Candidate Generator → Legality → Correctness → Local HLS → Joint HLS/Synthesis → Physical implementation when authorized → Evidence → Metrics → Decision Selection → Oracle/Reference → Report.

## Evidence classes
MEASURED, DERIVED, PREDICTED, LITERATURE_REPORTED, REPRODUCED, REFERENCE_ORACLE.
These classes must never be silently mixed.

## Canonical phases
P0 Contract & reproducibility → P1 Flow validation → P2 Local HLS → P3 Interaction → P4 Decision relevance → P5 Oracle → P6 Evidence selection → P7 Budget scaling → P15 Final validation.

## Hard execution rule
Exactly one phase may be IMPLEMENTING. Future phases may be documented but may not be implemented or executed before human Gate approval.

## Implementation boundary
V22.8 supplies contracts, schemas, isolated study workspaces, a minimal executable Python layer, validation scripts, timing accounting, plotting contracts, pragma-space handling, evidence/provenance rules, and external-baseline reproduction infrastructure. Vendor-specific HLS/Vivado execution remains environment-dependent and begins only in P1 after P0 approval.
