import hashlib, json
from pathlib import Path
from datetime import datetime, timezone

ALLOWED_STATUS = {"MEASURED","TOOL_REPORTED","DERIVED","ESTIMATED","PREDICTED","LITERATURE_REPORTED","REPRODUCED","REFERENCE_ORACLE","UNKNOWN"}

def sha256_file(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def canonical_hash(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()

def build_metric(metric_id, metric, value, unit, status, source_stage, *, project_version, study_id, run_id,
                 candidate_id, benchmark_id, device_part, tool, tool_version, source_artifact,
                 source_artifact_sha256, source_field_or_measurement, recorded_at_utc=None,
                 input_metric_ids=None, estimator=None):
    if status not in ALLOWED_STATUS:
        raise ValueError(f"invalid metric status: {status}")
    if status == "UNKNOWN" and value is not None:
        raise ValueError("UNKNOWN metrics cannot contain a fabricated value")
    if status in {"MEASURED","TOOL_REPORTED"} and not source_artifact:
        raise ValueError("measured/tool-reported metric requires source_artifact")
    if status == "DERIVED" and not input_metric_ids:
        raise ValueError("derived metric requires input_metric_ids")
    if status == "ESTIMATED" and not estimator:
        raise ValueError("estimated metric requires estimator")
    if status == "PREDICTED" and not estimator:
        raise ValueError("predicted metric requires model/estimator identity")
    return {
        "metric_id": metric_id, "metric": metric, "value": value, "unit": unit,
        "status": status, "source_stage": source_stage,
        "provenance": {
            "project_version": project_version, "study_id": study_id, "run_id": run_id,
            "candidate_id": candidate_id, "benchmark_id": benchmark_id,
            "device_part": device_part, "tool": tool, "tool_version": tool_version,
            "source_artifact": source_artifact,
            "source_artifact_sha256": source_artifact_sha256,
            "source_field_or_measurement": source_field_or_measurement,
            "recorded_at_utc": recorded_at_utc or datetime.now(timezone.utc).isoformat(),
        },
        "input_metric_ids": input_metric_ids or [],
        "estimator": estimator,
    }
