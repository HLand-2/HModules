import base64

def seal_script(file_path):
    """Reads a file and returns a Base64 encoded string for memory execution."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Encode to bytes, then base64, then back to a string
        return base64.b64encode(content.encode('utf-8')).decode('utf-8')
    except Exception as e:
        return None
