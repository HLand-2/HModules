import ollama, os, datetime, getpass, sys, time, psutil, threading, random, ctypes, re, io
import pandas as pd
from budget_manager import BudgetManager as budget_manager  # Your local module
from colorama import init, Fore, Back, Style
from cryptography.fernet import Fernet

init(autoreset=True)

class AI:
    def __init__(self, model="llama3"):
        self.REAL_CODE = "1475963284521235789"
        self.EARNING_LIMIT = 50.0
        self.ATTEMPT_LIMIT = 3
        self.model = model
        self.log_file = "ai_session_log.txt"
        self.master_key_file = "master.key"
        self.income_tracker = ".income_audit.csv"
        self.attempt_file = ".sys_fail_log"
        self.history, self.current_mode, self.override = [], "personal", False
        self.financial_actions = []

        self.modes = {
            "personal": "Witty, loyal friend.",
            "work": "Professional executive assistant.",
            "education": "World-class tutor.",
            "programming": "Senior software engineer.",
            "security": "Cybersecurity operative.",
            "medical": "Medical research assistant.",
            "financial": "Quantitative financial analyst."
        }

        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + Style.BRIGHT + "--- [SYSTEM BOOTING] ---")
        
        # Access Check & Decoy
        entered_code = getpass.getpass(Fore.GREEN + "CODE > ")
        if entered_code != self.REAL_CODE:
            self.register_failure()
            self.launch_decoy()
            exit()

        if os.path.exists(self.attempt_file): os.remove(self.attempt_file)
        self.self_heal()
        if not self.check_vpn():
            print(Fore.RED + "VPN REQUIRED."); exit()
        
        self.master_key = self.get_master_key()
        self.master_cipher = Fernet(self.master_key)
        self.session_key = Fernet.generate_key()
        self.session_cipher = Fernet(self.session_key)

        with open(self.log_file, "ab") as f:
            header = f"\n--- SESSION {datetime.datetime.now()} ---\n"
            f.write(header.encode() + b"KEY_HEADER:" + self.master_cipher.encrypt(self.session_key) + b"\n")

        threading.Thread(target=self.kill_switch_monitor, daemon=True).start()
        print(Fore.CYAN + "--- NEURAL ENGINE ONLINE ---")

    def auto_burn_wipe(self, reason):
        print(Fore.RED + f"\n!!! {reason} DETECTED: INITIATING AUTO-BURN !!!")
        files = [self.log_file, self.master_key_file, self.attempt_file, self.income_tracker]
        backup_dir = os.path.join(os.getenv('APPDATA'), 'SystemAI_Vault') if os.name == 'nt' else os.path.expanduser('~/.systemai_vault')
        files.append(os.path.join(backup_dir, 'master.bak'))
        for file in files:
            if os.path.exists(file):
                with open(file, "wb") as f: f.write(os.urandom(os.path.getsize(file)))
                os.remove(file)
        os._exit(1)

    def check_48h_limit(self, new_income):
        now = datetime.datetime.now()
        ago = now - datetime.timedelta(hours=48)
        df = pd.read_csv(self.income_tracker) if os.path.exists(self.income_tracker) else pd.DataFrame(columns=['Date', 'Amount'])
        df['Date'] = pd.to_datetime(df['Date'])
        df = pd.concat([df, pd.DataFrame([{'Date': now, 'Amount': float(new_income)}])], ignore_index=True)
        recent = df[df['Date'] > ago]
        recent.to_csv(self.income_tracker, index=False)
        if recent['Amount'].sum() >= self.EARNING_LIMIT: self.auto_burn_wipe("48H INCOME LIMIT")

    def check_vpn(self):
        itfs = psutil.net_if_stats()
        return any(any(k in i.lower() for k in ['tun','tap','ppp','vpn']) and itfs[i].isup for i in itfs)

    def kill_switch_monitor(self):
        while True:
            if not self.check_vpn(): self.auto_burn_wipe("VPN DISCONNECT")
            time.sleep(2)

    def get_master_key(self):
        if not os.path.exists(self.master_key_file):
            key = Fernet.generate_key()
            with open(self.master_key_file, "wb") as f: f.write(key); return key
        with open(self.master_key_file, "rb") as f: return f.read()

    def self_heal(self):
        path = os.path.join(os.getenv('APPDATA'), 'SystemAI_Vault') if os.name == 'nt' else os.path.expanduser('~/.systemai_vault')
        if not os.path.exists(path): os.makedirs(path)
        bak = os.path.join(path, 'master.bak')
        if not os.path.exists(self.master_key_file) and os.path.exists(bak):
            with open(bak, 'rb') as f: content = f.read()
            with open(self.master_key_file, 'wb') as f: f.write(content)
        elif os.path.exists(self.master_key_file):
            with open(self.master_key_file, 'rb') as f: content = f.read()
            with open(bak, 'wb') as f: f.write(content)

    def launch_decoy(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.WHITE + "--- SYSTEM DIAGNOSTIC UTILITY v4.2.1 ---")
        while True:
            cmd = input("DIAG> ")
            if cmd.lower() in ["exit", "quit"]: break
            print(f"Executing {cmd.upper()}... Complete.")

    def run(self):
        while True:
            inp = input(Fore.GREEN + f"\n[{self.current_mode.upper()}] > ")
            if inp.lower() in ["exit", "quit"]: break
            
            # Financial Triggers
            if self.current_mode == "financial":
                nums = re.findall(r'\d+', inp)
                amt = int(nums[0]) if nums else None
                if "add" in inp.lower() and amt:
                    name = inp.lower().replace("add", "").replace(str(amt), "").strip()
                    budget_manager.add_budget(name, amt)
                    self.check_48h_limit(amt)
                    continue
                elif "spend" in inp.lower() and amt:
                    name = inp.lower().replace("spend", "").replace(str(amt), "").strip()
                    budget_manager.spend_budget(name, amt)
                    continue
                elif "summary" in inp.lower():
                    budget_manager.print_summary()
                    continue

            # Context & Response
            res = ollama.chat(model=self.model, messages=[{'role': 'system', 'content': self.modes[self.current_mode]}, {'role': 'user', 'content': inp}])['message']['content']
            with open(self.log_file, "ab") as f:
                f.write(self.session_cipher.encrypt(f"USER: {inp} | AI: {res}".encode()) + b"\n")
            print(Fore.GREEN + f"\nAI >> {res}")

if __name__ == "__main__":
    AI().run()
