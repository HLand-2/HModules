import security  # Module 7
import logger    # Module 5

def run_interface():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 0:
            break
        elif choice == 6:  # Security Option
            raw_text = input("Enter text to encrypt: ")
            secret = security.encrypt_data(raw_text)
            print(f"Locked Data: {secret}")
            
            # Log the security action using Module 5
            logger.log_event("security", f"Encrypted data: {secret}")
        
        input("\nPress [ENTER] to continue...")
