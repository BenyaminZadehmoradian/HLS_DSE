import shlex, time
from pathlib import Path
import yaml
from .models import RunRecord
from . import control


def _study_phase(root, study_id):
    p = Path(root) / 'studies' / str(study_id) / 'CONTRACT.yaml'
    try:
        return (yaml.safe_load(p.read_text(encoding='utf-8')) or {}).get('phase_id')
    except Exception:
        return None                                   # unknown phase -> the control plane denies


def run_command(run: RunRecord, command, log_path, *, action, actor='hlsdse.flow', phase=None, root=None):
    """Execute a tool command for a run through the control plane. Authorization happens before any process is
    started; on DENY nothing is executed and run.status is DENIED. `command` is an argv list (a string is split
    with shlex; it is never given to a shell)."""
    root = root or control.ROOT
    argv = shlex.split(command) if isinstance(command, str) else list(command)
    start = time.time()
    try:
        # append mode: a denied request must not truncate an existing log
        with open(log_path, 'a', encoding='utf-8') as log:
            res = control.run_authorized(argv, action=action, phase=phase or _study_phase(root, run.study_id),
                                         study=run.study_id, environment=run.environment_id, actor=actor,
                                         caller=f'hlsdse.flow.run_command:{run.run_id}', root=root,
                                         stdout=log, stderr=log)
    except control.ExecutionDenied as e:
        run.status = 'DENIED'
        run.metrics['control_reason'] = f'EXECUTION_REFUSED: {e}'
        run.metrics['wall_clock_s'] = time.time() - start
        return run
    except OSError:
        run.status = 'FAILED'; run.failure_class = 'INFRASTRUCTURE_FAILURE'
        run.metrics['wall_clock_s'] = time.time() - start
        return run
    run.metrics['control_request_id'] = res.decision.request_id
    run.metrics['control_decision'] = res.decision.decision
    if not res.executor_called:
        run.status = 'DENIED'
        run.metrics['control_reason'] = f'{res.decision.reason_code}: {res.decision.reason}'
    elif res.returncode is None:
        run.status = 'FAILED'; run.failure_class = 'INFRASTRUCTURE_FAILURE'
    else:
        run.status = 'SUCCESS' if res.returncode == 0 else 'FAILED'
        if res.returncode != 0: run.failure_class = 'UNKNOWN_ERROR'
    run.metrics['wall_clock_s'] = time.time() - start
    return run
