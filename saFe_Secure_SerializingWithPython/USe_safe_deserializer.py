import pickle

class SafeUnpickler(pickle.Unpickler):
    safe_builtins = {
        'range', 'complex', 'set', 'frozenset' 
        
        # safe built-in Python classes - ONLY these will be allowed at de-serialization
    }

    def find_class(self, module_name, global_name): 
        
        # overrides the calss, gets called internally by pickle when it needs to resolve a class or func while loading pickle data

        if module_name == "builtins" and global_name in self.safe_builtins: 

        # checks wherther class/ func comes from the built-in safe modules AND whether its one of the explicitly allowed safe types

            return getattr(__builtins__, global_name) # IF it passes the check, returns the actual built-in type from __builtins__
        raise pickle.UnpicklingError(f" Unsafe class: {module_name}.{global_name}")
    
    @staticmethod    
    def safe_load(file_path):
        with open(file_path, "rb") as f:
            return SafeUnpickler(f).load() # this uses the overrided 'find_class' method to filter what gets loaded.

# Blocks dangerous files
# WARNING: Still not bulletProof - don't use it on untrusted data / input.  
