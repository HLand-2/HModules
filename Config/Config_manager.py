import json

def get_config():
    """Loads API keys safely from a config file."""
    with open("config.json", "r") as f:
        return json.load(f)
