# AI Execution Checklist

Before every implementation run:
- Read RESEARCH_STATE.yaml.
- Confirm active phase and study.
- Confirm Gate state permits execution.
- Load active study contract.
- Load benchmark and environment contracts.
- Verify output paths are inside the study workspace.
- Verify no future-phase artifacts will be generated.
- Record command, environment, seed, and timestamp.
- On failure, classify failure before retry.
- On completion, generate evidence manifest and report update.
