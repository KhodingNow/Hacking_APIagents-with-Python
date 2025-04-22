
# 2. Define a safe schema for objects and manually reconstruct them:

class SafeTask:
    def __init__(self, name, param):
        self.name = name
        self.param = param

    def to_dict(self):
        return {"name": self.name, "param": self.param}
    
    @staticmethod
    def from_dict(d):
        return SafeTask(d["name"], d["param"])
    
# Serialize
task = SafeTask("clean_temp", 5)
with open("task.json", "w") as f:
    json.dump(task.to_dict(), f)

# Deserialize
with open("task.json", "r") as f:
    data = json.load(f)
    safe_task = SafeTask.from_dict(data)

# Full control, no suprises
# BUT, reqires manual mapping


