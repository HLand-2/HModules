import base64
import os

# This is the "Magic Header" your AI script MUST start with
SECURITY_ID = "import turtle"

def seal_script(file_path):
    """
    Checks for the Security ID, then encodes the script for memory execution.
    """
    if not os.path.exists(file_path):
        return None
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read the first line to verify the guard
            first_line = f.readline().strip()
            if first_line != SECURITY_ID:
                print(f"CRITICAL: INVALID SECURITY HEADER IN {file_path}")
                return None
            
            # Read the rest of the file
            content = first_line + "\n" + f.read()
        
        return base64.b64encode(content.encode('utf-8')).decode('utf-8')
    except Exception:
        return None
