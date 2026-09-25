# Isolated Run Workspace

Copy this directory to `runs/<STUDY_ID>/<RUN_ID>/` before execution.

Never point Vivado or Vitis to another Study's mutable workspace.
Never overwrite an existing completed Run.

Required top-level directories:
- config/
- vivado/
- vitis/
- bitstreams/
- measurements/
- raw/
- normalized/
- logs/
- report/
