import subprocess, time
from dataclasses import asdict
from .models import RunRecord

def run_command(run: RunRecord, command, log_path):
    start=time.time()
    try:
        with open(log_path,'w',encoding='utf-8') as log:
            cp=subprocess.run(command,shell=True,text=True,stdout=log,stderr=subprocess.STDOUT)
        run.status='SUCCESS' if cp.returncode==0 else 'FAILED'
        if cp.returncode!=0: run.failure_class='UNKNOWN_FAILURE'
    except Exception:
        run.status='FAILED'; run.failure_class='INFRASTRUCTURE_FAILURE'
    run.metrics['wall_clock_s']=time.time()-start
    return run
