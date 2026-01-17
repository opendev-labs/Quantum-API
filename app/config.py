import json, os
from typing import Any, Dict

def load_config() -> Dict[str, Any]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.json")
    with open(config_path) as f:
        cfg = json.load(f)
    env = os.getenv("APP_ENV", cfg["app"]["default_env"])
    settings = cfg["environments"][env]
    return {"cfg": cfg, "env": env, "settings": settings}

CONF = load_config()
