def encrypt_data(text, key=3):
    """A simple Caesar Cipher for basic security."""
    result = ""
    for char in text:
        result += chr(ord(char) + key)
    return result
