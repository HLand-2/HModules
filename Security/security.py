# security.py
def encrypt_data(text, key=3):
    """Shifts characters to hide data."""
    return "".join(chr(ord(char) + key) for char in text)

def decrypt_data(text, key=3):
    """Reverses the shift to reveal data."""
    return "".join(chr(ord(char) - key) for char in text)
