# AI DATA ISOLATION POLICY
Every run belongs to exactly one Study and has a unique RUN_ID.

Each run capsule must contain:
manifest.json, command.txt, environment.json, input_hashes.json,
stdout.log, stderr.log, raw/, parsed/, evidence/, status.json.

Cross-study reuse requires an explicit dependency recorded in the Study contract.
Raw evidence is immutable after validation.
