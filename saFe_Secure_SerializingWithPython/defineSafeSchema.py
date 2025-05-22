
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

"""
WHY is this schema safe?
- NO arbitrary code execution - Unlike pickle, json.load() only parses data, not code
- Explicit schema - The class knows how to serialize and deserialize with full control.
- Limited attack surface - Only expected fields are loaded, and no hidden code paths are involved
- Auditability - You can easily see what's in the json file - it's human readable

"""

# Safety Software context - Cyber Security -> Server agents -> ML pipelines, Key desing pricibples incl: 

"""
- Trust no external input by DEFAULT
- Avoid deserialization formats that can invoke code (like pickle, marshal with unsafe modes)
- Use data-only formats like JSON, TOML, or protobuf, paid=red with manual validation & schema enforcement

"""

# This pattern enforces deterministic (you remain in conrtrol), auditable deserialization that aligns with;

"""
- Zero Trust principles
- Secure software supply chain guides
- Compliance with OWASP, etc 

NB the DOWNSIDE - is manually update to 'to_dict()' and 'from_dict()' if the object changes.
- No automatic support for nested or complex stuctures unless you build it in. 

"""


