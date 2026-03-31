This is HL2's module list:
1: Budget manager,
2: HMath,
3: AI
# 🟢 NEON-TERMINAL PERSONAL AI (OLLAMA EDITION)

An elite, encrypted personal assistant built in Python. Features auto-context switching, VPN kill-switch, and multi-layer encryption.

## 🔐 ACCESS PROTOCOLS
*   **Access Code:** `1475963284521235789`
*   **Security Requirement:** Active VPN Tunnel (tun, tap, ppp, vpn) must be detected to boot.
*   **Encryption:** Fernet (AES-128) symmetric encryption.

## 🧠 AI MODES (AUTO-SWITCHING)
The AI analyzes your message history and automatically shifts its persona:
1.  **PERSONAL**: Casual, witty, and loyal friend.
2.  **WORK**: Professional, efficient, and brief.
3.  **EDUCATION**: Patient tutor; breaks down complex topics.
4.  **PROGRAMMING**: Senior engineer; optimized code and technical depth.
5.  **SECURITY**: Cybersecurity operative; alert and privacy-focused.

## ⌨️ COMMAND CONSOLE
Type these directly into the `USER >` prompt:


| Command | Action |
| :--- | :--- |
| `ghost mode` | Toggles logging ON/OFF. (Chats aren't saved to disk). |
| `lock mode` | Freezes the current AI persona (Disables Auto-Switch). |
| `unlock mode` | Re-enables the Neural Engine's context analyzer. |
| `self destruct` | Wipes `secret.key` and `ai_session_log.txt` with random data. |
| `exit` / `quit` | Safely closes the session. |

## 📁 FILE STRUCTURE
*   **`AI.py`**: The main engine (Requires Ollama + Llama3).
*   **`decryptor.py`**: Utility to read your encrypted logs in neon green.
*   **`secret.key`**: **CRITICAL.** If deleted, logs are permanently unreadable.
*   **`ai_session_log.txt`**: The encrypted archive of your interactions.

## 🛠️ INSTALLATION
1. Install [Ollama](https://ollama.com) and run `ollama run llama3`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Launch: `python AI.py`.
