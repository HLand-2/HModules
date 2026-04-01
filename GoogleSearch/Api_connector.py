import requests

def google_search(query, api_key, cse_id):
    """Fetches live search results from Google."""
    url = f"https://googleapis.com{api_key}&cx={cse_id}&q={query}"
    response = requests.get(url)
    return response.json().get("items", [])
