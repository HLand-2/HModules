import os

def clear_screen():
    """Clears the terminal for a clean look."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """The main dashboard for your 10-module suite."""
    print("=" * 40)
    print("      MEGA-SUITE v1.0 COMMAND CENTRE      ")
    print("=" * 40)
    print("1. [MATH]      Run Calculations")
    print("2. [AI]        Generate Predictions")
    print("3. [DATA]      Load External Files")
    print("4. [VISUAL]    View Data Charts")
    print("5. [LOGS]      Check System History")
    print("6. [SECURITY]  Encrypt Sensitive Data")
    print("7. [GOOGLE]    Fetch Live API Data")
    print("8. [VALIDATE]  Check System Integrity")
    print("9. [CONFIG]    Manage API Keys")
    print("0. [EXIT]      Shut Down System")
    print("=" * 40)

def get_user_choice():
    """Handles user input safely."""
    try:
        choice = int(input("\nSELECT PROTOCOL (0-9): "))
        return choice
    except ValueError:
        return -1 # Invalid input signal

def run_interface():
    """Main loop to keep the UI running."""
    while True:
        clear_screen()
        display_menu()
        
        choice = get_user_choice()
        
        if choice == 0:
            print("\nShutting down... Goodbye!")
            break
        elif choice == 1:
            print("\n[Action] Accessing math_utils...")
            # Here you would call math_utils.add() etc.
        elif choice == 7:
            print("\n[Action] Connecting to Google API via api_connector...")
        elif choice == -1:
            print("\n[!] ERROR: Please enter a number between 0 and 9.")
        else:
            print(f"\n[Action] Initialising Module #{choice}...")

        input("\nPress [ENTER] to return to menu...")

if __name__ == "__main__":
    run_interface()
