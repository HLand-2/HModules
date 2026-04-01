import json

def load_data(file_path):
    """Loads raw data for the AI to process."""
    try:
        with open(file_path, 'r') as f:
            if file_path.endswith('.json'):
                return json.load(f)
            return f.read().splitlines()
    except FileNotFoundError:
        return "Error: File not found!"
