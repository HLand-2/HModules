# --- IMPORTING THE 10-MODULE ECOSYSTEM ---
import math_utils      # 1. The Logic
import ai_engine       # 2. The Brain
import data_loader     # 3. The Input
import visualiser      # 4. The Output
import logger          # 5. The Historian
import user_interface  # 6. The Command Centre
import security        # 7. The Protector
import api_connector   # 8. The Google Link
import validator       # 9. The Safety Net
import config_manager  # 10. The Secret Vault

def startup_sequence():
    """Initializes the entire 10-module suite."""
    print(">>> INITIALISING SYSTEM NODES [1-10]...")
    
    # 1. Load Config (Module 10)
    config = config_manager.get_config()
    
    # 2. Log System Start (Module 5)
    logger.log_event("SYSTEM", "All 10 modules online.")
    
    print(">>> ALL SYSTEMS NOMINAL. LAUNCHING INTERFACE...\n")

def main():
    # Run the startup check
    startup_sequence()
    
    # Start the Interactive UI (Module 6)
    # This loop handles all your modules (Math, AI, Security, etc.)
    user_interface.run_interface()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] EMERGENCY SHUTDOWN INITIATED by USER.")
        logger.log_event("SYSTEM", "Manual Override: Shutdown.")
    except Exception as e:
        print(f"\n[!] FATAL CRASH: {e}")
        logger.log_event("ERROR", str(e))
