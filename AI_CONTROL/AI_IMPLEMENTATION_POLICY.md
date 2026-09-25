# AI Implementation Policy — V22.8

1. The AI may implement only the active phase.
2. Shared infrastructure may be implemented only when required by the active phase and recorded in the change log.
3. The AI must not invent benchmark metadata, device parameters, tool paths, measured values, timing, or literature results.
4. Unknown values remain `UNKNOWN`.
5. Raw evidence is immutable; corrections create a new evidence record/version.
6. CSV is an export/view layer, never the authoritative evidence store.
7. Every scientific result must trace to Study → Run → Evidence → Derived Metric → Figure/Table → Report.
8. The AI cannot approve its own Gate.
9. Vendor-specific commands are generated only from an explicitly registered environment.
10. If a required environment detail is absent, execution stops and escalates rather than guessing.
