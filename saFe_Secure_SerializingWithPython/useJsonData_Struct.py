# 1. Using Json Basic Data Structure

import json

data = {"task": "do_something", "param": 42}

# Serialize
with open("safe_task.json", "w") as f:
    json.dump(data, f)

#De-serialize
with open("safe_task.json", "w") as f:
    task = json.load(f)

print(task)

# This is safe because 'json.load()' cannot EXECUTE CODE
# HOWEVER, this doesn't support Python objects directly
