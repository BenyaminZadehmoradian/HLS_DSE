def decision_loss(hv, hv_ref):
    if hv_ref <= 0: raise ValueError("Reference hypervolume must be positive")
    return 1.0 - hv/hv_ref

def interaction_residual(joint, composition):
    return joint-composition
