from typing import Dict, Any
from app.config import CONF
from quantum_compute import QuantumDevice

# Global reference (can be improved with dependency injection)
ACTIVE_DEVICE = QuantumDevice(wires=3, backend="default.qubit")

def get_backend_choice() -> Dict[str, Any]:
    cfg = CONF["cfg"]["quantum_backends"]
    default = cfg["default"]
    meta = cfg["options"][default]
    return {"name": default, "wires": ACTIVE_DEVICE.wires, **meta}

def select_backend(name: str) -> Dict[str, Any]:
    global ACTIVE_DEVICE
    opts = CONF["cfg"]["quantum_backends"]["options"]
    if name not in opts:
        raise ValueError(f"Unknown backend: {name}")
    
    # Simulate switching backend (in reality we would re-init device)
    # ACTIVE_DEVICE = QuantumDevice(wires=3, backend=name) 
    return {"name": name, **opts[name]}
