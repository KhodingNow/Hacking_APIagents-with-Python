# EXAMPLE of vulnerable code snippet for lateral movement, exfiltration of sensitive date, or system compromise:
from jupyter_client import KernelManager

def execute_code(user_input):
    km = KernelManager()
    km.start_kernel()
    kc = km.client()
    kc.start_channels()

    kc.execute(user_input)

    # Fetch the reply from the kernel
    reply = kc.get_shell_msg(timeout=5)
    
    return reply['content']

# Example input
user_payload = "print('Hello, world!')"

print(execute_code(user_payload))


