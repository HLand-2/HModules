import budget_manager  # <--- YOUR MODULE

# ... inside your AI class ...

    def check_budget_alerts(self):
        """Proactive check for overspending (90% threshold)"""
        try:
            # Assuming your module has a way to check thresholds
            # If not, the AI can just call your summary
            overspent = budget_manager.get_overspent_categories() 
            for cat in overspent:
                print(Fore.RED + Style.BRIGHT + f"!!! ALERT: {cat} is over 90% spent !!!")
        except:
            pass # Silent if feature not in module

    def run(self):
        while True:
            # Status line
            prefix = f"[{self.current_mode.upper()}]"
            print(Fore.GREEN + Style.BRIGHT + f"\n{prefix} > ", end="")
            user_input = input()

            if user_input.lower() in ["exit", "quit"]: break

            # 1. TRIGGER YOUR EXISTING SUMMARY
            if "summary" in user_input.lower() or "show budget" in user_input.lower():
                print(Fore.GREEN + "\n--- LOADING FINANCIAL DATA ---")
                budget_manager.print_summary() # Calling your specific function
                continue

            # 2. ANALYZE CONTEXT (Auto-Switching)
            self.analyze_context(user_input)

            # 3. HANDLE COMMANDS (If in Financial Mode)
            if self.current_mode == "financial":
                numbers = re.findall(r'\d+', user_input)
                amount = int(numbers[0]) if numbers else None

                if "add" in user_input.lower() and amount:
                    name = user_input.lower().replace("add", "").replace(str(amount), "").strip()
                    budget_manager.add_budget(name, amount)
                    print(Fore.CYAN + f"--- [MODIFIED] Added {amount} to {name} ---")
                    self.check_budget_alerts() # Auto-check after changes
                    continue

                elif "spend" in user_input.lower() and amount:
                    name = user_input.lower().replace("spend", "").replace(str(amount), "").strip()
                    budget_manager.spend_budget(name, amount)
                    print(Fore.CYAN + f"--- [DEBIT] Spent {amount} from {name} ---")
                    self.check_budget_alerts()
                    continue

                elif "change" in user_input.lower() and amount:
                    name = user_input.lower().replace("change", "").replace(str(amount), "").strip()
                    budget_manager.change_budget(name, amount)
                    print(Fore.CYAN + f"--- [UPDATED] {name} set to {amount} ---")
                    continue

            # 4. DEFAULT AI RESPONSE
            # (Standard Ollama chat logic here...)
