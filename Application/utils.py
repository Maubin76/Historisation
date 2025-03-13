import json
import os
from datetime import datetime

def log_update(person_instance):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"db_updates_{datetime.today().strftime('%Y-%m-%d')}.log")
    log_entry = {
        "first_name": person_instance.first_name,
        "last_name": person_instance.last_name,
        "age": person_instance.age,
        "address": person_instance.address,
        "timestamp": datetime.now().isoformat()
    }

    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")