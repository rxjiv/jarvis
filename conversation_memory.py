import json
from datetime import datetime
import os

LOG_FILE = "brain/memory_log.json"

def save_conversation(user, jarvis):
    timestamp = datetime.now().isoformat()
    entry = {
        "timestamp": timestamp,
        "user": user,
        "jarvis": jarvis
    }

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([entry], f, indent=4)
    else:
        with open(LOG_FILE, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=4)

def load_memory():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
