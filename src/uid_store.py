import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

UID_FILE = Path("data/uid_map.json")

def load_uid_map():
    if UID_FILE.exists():
        return json.loads(UID_FILE.read_text())
    return {}

def save_uid_map(m):
    UID_FILE.parent.mkdir(exist_ok=True)
    UID_FILE.write_text(json.dumps(m, indent=2, sort_keys=True))

def uid_for_event(event, uid_map):
    key = event["url"]

    if key in uid_map:
        return uid_map[key]["uid"]

    uid = hashlib.sha256(key.encode()).hexdigest() + "@areces"

    # uid_map[key] = uid
    uid_map[key] = {
    "uid": uid,
    # Also save date event was first created
    "dtstamp": datetime.now(timezone.utc).isoformat()
    }
    return uid

