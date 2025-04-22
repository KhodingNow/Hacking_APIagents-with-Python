# For internal systems:

# Store a cryptographic hash (SHA-256) of known-good pickles
# Verify integrity before loading:

import hashlib

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

trusted_hash = "abcdef123...jkl" # from secure source
if file_hash("task.pickle") != trusted_hash:

    raise Exception("Pickle file integrity compromised")


 
