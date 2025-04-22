import pickle

class SafeUnpickler(pickle.Unpickler):
    safe_builtins = {
        'range', 'complex', 'set', 'frozenset'
    }

    def find_class(self, module_name, global_name):
        if module_name == "builtins" and global_name in self.safe_builtins: 
        
            return getattr(__builtins__, global_name)
        raise pickle.UnpicklingError(f" Unsafe class: {module_name}.{global_name}")
    
    def safe_load(file_path):
        with open(file_path, "rb") as f:
            return SafeUnpickler(f).load()

# Blocks dangerous files
# WARNING: Still not bulletProof - don't use it on untrusted data / input.  
