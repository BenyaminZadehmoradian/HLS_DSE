from pathlib import Path
import json, yaml, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]; warnings=[]

def load_yaml(p):
    try: return yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    except Exception as e: errors.append(f'YAML {p}: {e}'); return {}

def require(path, label=None):
    if not path.exists(): errors.append(f'Missing required {label or path}: {path}')

state=load_yaml(ROOT/'RESEARCH_STATE.yaml')
expected_version = state.get('project_version')
expected_source = state.get('canonical_source')
if not expected_version: errors.append('Missing project_version')
if not expected_source: errors.append('Missing canonical_source')
if expected_source and not (ROOT/expected_source).exists(): errors.append('Canonical source file missing')
# Phase/state machine, P1 authorization, active_environment, approval artifacts, transition provenance and
# AI_CONTROL policy consistency: the same checks the runtime control plane (hlsdse.control) enforces.
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT/'src'))
from hlsdse.control import repository_control_errors
errors.extend(f'CONTROL: {e}' for e in repository_control_errors(ROOT))
for name in ['CONTROL_PLANE_POLICY.yaml','PHASE_CONTROL.yaml','AUTO_PUSH_POLICY.yaml','AI_EXECUTION_POLICY.yaml','AGENT_PERMISSIONS.yaml','AI_CONDUCT.md','AI_PHASE_GATE_POLICY.md']:
    require(ROOT/'AI_CONTROL'/name, 'AI_CONTROL policy')
if state.get('fixed_reference_device') != 'xc7z020clg484': errors.append('Reference device must be xc7z020clg484')

registry=load_yaml(ROOT/'contracts/STUDY_ID_REGISTRY.yaml')
for sid in ['S00','S01','S09','S71']:
    if sid not in registry.get('reserved',{}): errors.append(f'Missing registry entry {sid}')

ids={}
for p in (ROOT/'studies').glob('S*/CONTRACT.yaml'):
    d=load_yaml(p); sid=d.get('study_id')
    if sid: ids.setdefault(sid,[]).append(str(p))
for sid,paths in ids.items():
    if len(paths)>1: errors.append(f'Duplicate study_id {sid}: {paths}')

s71=load_yaml(ROOT/'studies/S71/CONTRACT.yaml')
if not s71 or s71.get('study_id')!='S71': errors.append('S71 contract invalid')
s09=load_yaml(ROOT/'studies/S09/CONTRACT.yaml')
if s09 and s09.get('status')!='ARCHIVED_ID_COLLISION': errors.append('S09 must be archived')

required_contracts=[
'HARDWARE_PLATFORM_CONTRACT.yaml','ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml',
'BENCHMARK_CONTRACT.yaml','STATISTICS_CONTRACT.yaml','SEARCH_ALGORITHM_CONTRACT.yaml','MEASUREMENT_CONTRACT.yaml',
'SYSTEM_ARCHITECTURE_CONTRACT.yaml','CONCURRENCY_FAIRNESS_CONTRACT.yaml','REPRODUCTION_CONTRACT.yaml','DATA_LEAKAGE_CONTRACT.yaml',
'CACHE_CONTRACT.yaml','FAILURE_AND_RETRY_CONTRACT.yaml','P1_IMPLEMENTATION_CONTRACT.yaml','EXTERNAL_BASELINE_CONTRACT.yaml',
'STAGED_EVALUATION_CONTRACT.yaml','STAGE_DECISION_CONTRACT.yaml','METRIC_PROVENANCE_CONTRACT.yaml']
for name in required_contracts: require(ROOT/'contracts'/name, 'contract')

schemas={}
for name in ['METRIC_PROVENANCE_SCHEMA.json','STAGE_DECISION_SCHEMA.json','EVIDENCE_RECORD_SCHEMA.json',
             'RUN_MANIFEST_SCHEMA.json','RUN_TIMING_SCHEMA.json','PRAGMA_CANDIDATE_SCHEMA.json']:
    p=ROOT/'schemas'/name
    try: schemas[name]=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'JSON {p}: {e}')
if not (ROOT/'schemas/PRAGMA_SPACE_SCHEMA.yaml').exists(): errors.append('Missing schemas/PRAGMA_SPACE_SCHEMA.yaml')

# The run template must satisfy the run-manifest schema's required fields and top-level types.
# Statistical and budget protocol must be complete (STATISTICS_CONTRACT / BUDGET_CONTRACT 2.0).
stats=load_yaml(ROOT/'contracts/STATISTICS_CONTRACT.yaml')
for k in ['pre_registration','units_of_analysis','replication','noise_floor','objectives_and_fronts','quality_metrics','inference','failures_and_missing_data']:
    if k not in stats: errors.append(f'STATISTICS_CONTRACT missing section {k}')
for k in ['adrs','hypervolume','decision_loss','time_to_target']:
    if k not in (stats.get('quality_metrics') or {}): errors.append(f'STATISTICS_CONTRACT missing metric definition {k}')
budget=load_yaml(ROOT/'contracts/BUDGET_CONTRACT.yaml')
if (budget.get('primary_budget') or {}).get('name')!='tool_seconds': errors.append('BUDGET_CONTRACT must declare primary_budget tool_seconds')
for k in ['charging_rules','stage_timeouts','parallelism','stopping']:
    if k not in budget: errors.append(f'BUDGET_CONTRACT missing section {k}')
if not (ROOT/'templates/PREREGISTRATION_TEMPLATE.yaml').exists(): errors.append('Missing templates/PREREGISTRATION_TEMPLATE.yaml')
prereq=set(stats.get('pre_registration',{}).get('required_fields',[]))
tmpl_keys=set(load_yaml(ROOT/'templates/PREREGISTRATION_TEMPLATE.yaml')) if (ROOT/'templates/PREREGISTRATION_TEMPLATE.yaml').exists() else set()
if prereq-tmpl_keys: errors.append(f'PREREGISTRATION template lacks required fields {sorted(prereq-tmpl_keys)}')

tmpl=ROOT/'runs/_TEMPLATE/manifest.yaml'
if not tmpl.exists(): errors.append('Missing runs/_TEMPLATE/manifest.yaml')
elif 'RUN_MANIFEST_SCHEMA.json' in schemas:
    m=load_yaml(tmpl); rs=schemas['RUN_MANIFEST_SCHEMA.json']
    pytypes={'object':dict,'string':str,'integer':int,'boolean':bool,'null':type(None)}
    for k in rs['required']:
        if k not in m: errors.append(f'runs/_TEMPLATE manifest missing required field {k}')
    for k,spec in rs['properties'].items():
        if k in m and 'type' in spec:
            allowed=spec['type'] if isinstance(spec['type'],list) else [spec['type']]
            if not isinstance(m[k],tuple(pytypes[a] for a in allowed if a in pytypes)):
                errors.append(f'runs/_TEMPLATE manifest field {k} is not {allowed}')
        if k in m and 'const' in spec and m[k]!=spec['const']:
            errors.append(f'runs/_TEMPLATE manifest field {k} must be {spec["const"]}')
if not (ROOT/'benchmarks/templates/BENCHMARK_TEMPLATE.yaml').exists(): errors.append('Missing benchmark template')
if not (ROOT/'configs/preflight/default.yaml').exists(): errors.append('Missing preflight config')
if not (ROOT/'audit/gates/P0_EXIT_CRITERIA.md').exists(): errors.append('Missing P0 exit criteria')

for p in (ROOT/'evidence/measured').rglob('*'):
    if p.is_file(): warnings.append(f'Unexpected measured evidence before P0: {p}')

# Reports must identify the current version; historical/archived reports may be exempt.
for p in (ROOT/'REPORTS').glob('*.md'):
    txt=p.read_text(encoding='utf-8')
    if 'project_version:' not in txt and 'Historical' not in txt: warnings.append(f'Report metadata missing: {p}')

artifact=load_yaml(ROOT/'contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml')
if artifact.get('reference_device',{}).get('part') != 'xc7z020clg484': errors.append('Artifact contract reference device mismatch')

hardware=load_yaml(ROOT/'contracts/HARDWARE_PLATFORM_CONTRACT.yaml')
if hardware.get('reference_device',{}).get('part') != 'xc7z020clg484': errors.append('Hardware contract reference device mismatch')

print(f'errors={len(errors)} warnings={len(warnings)}')
for x in errors: print('ERROR:',x)
for x in warnings: print('WARNING:',x)
sys.exit(1 if errors else 0)
