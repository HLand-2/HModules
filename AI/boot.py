import os
import sys
import base64
from vault_packer import seal_script

# TARGET: The hardened script we want to run in memory
TARGET_FILE = "hardened_ai_v2.py"

def volatile_boot():
    # 1. Use the custom module to get the payload
    payload = seal_script(TARGET_FILE)
    
    if not payload:
        print("BOOT_ERROR: TARGET NOT FOUND")
        os._exit(1)

    # 2. Clear the physical trace (Optional: Delete the source file after encoding)
    # os.remove(TARGET_FILE) 

    # 3. Execute payload directly in RAM
    try:
        # Decode and execute
        decoded_logic = base64.b64decode(payload).decode('utf-8')
        
        print("\033[94m--- [LOADING CORE TO VOLATILE MEMORY] ---\033[0m")
        # Direct execution within the global namespace
        exec(decoded_logic, globals())
        
    except Exception as e:
        os._exit(1)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    volatile_boot()
