#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from hlsdse.scanning.environment import scan_environment

required=['vivado','vitis','vitis_hls','git']
env=scan_environment()
print(json.dumps(env, indent=2))
missing=[k for k in required if not env['tools'][k]['present']]
print('--- PREFLIGHT ---')
if missing:
    print('MISSING_TOOLS='+','.join(missing))
    print('STATUS=BLOCKED_UNTIL_ENVIRONMENT_READY')
    raise SystemExit(2)
print('STATUS=ENVIRONMENT_TOOLS_VISIBLE')
