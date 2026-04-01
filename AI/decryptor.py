import os
from cryptography.fernet import Fernet
from colorama import init, Fore

init(autoreset=True)

def decrypt_multi_key_logs(log_file="ai_session_log.txt", master_key_file="master.key"):
    if not os.path.exists(master_key_file): return
    with open(master_key_file, "rb") as f: master_cipher = Fernet(f.read())
    current_cipher = None

    with open(log_file, "rb") as f:
        for line in f:
            line = line.strip()
            if line.startswith(b"KEY_HEADER:"):
                current_cipher = Fernet(master_cipher.decrypt(line.replace(b"KEY_HEADER:", b"")))
                continue
            if current_cipher:
                try: print(Fore.GREEN + current_cipher.decrypt(line).decode())
                except: continue

if __name__ == "__main__":
    decrypt_multi_key_logs()
