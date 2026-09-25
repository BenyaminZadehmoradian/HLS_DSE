# AI REPORT TEMPLATE POLICY

All project reports must use `AI_CONTROL/REPORT_TEMPLATE.md`. Gate reports use the same template with the
Gate section defined in `AI_PHASE_GATE_POLICY.md`.

Reports must distinguish: verified/measured results, deterministically derived results, model predictions,
assumptions, unknown/missing data, and interpretation. A report generator may not create a value merely to fill
an empty field.

Every report must identify report ID, type, project/phase/study/gate, creation/update dates, AI model, human owner when known, approval state, version and revision.

Every substantive result must be traceable: `Study → Run → Evidence → Derived Metric → Figure/Table → Report`.

Results use the metric statuses of `contracts/METRIC_PROVENANCE_CONTRACT.yaml`. Predictions must never be presented as measurements.

A complete report includes purpose, research questions, scope, methodology, inputs, implementation actually performed, results, figures/tables, analysis, validation, failures, limitations, reproducibility, conclusions, gate decision where applicable, change log and appendices.

The AI model name must come from the actual execution context. If unavailable, use `UNKNOWN`; never guess. Old report versions remain archived and immutable. AI cannot self-approve a Gate.
