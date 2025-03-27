import requests

def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        response.raise_for_status()  # Raise error for bad response
        word = response.json()[0]
        return word.lower()  # Ensure lowercase consistency
    except requests.RequestException:
        return "default"  # Fallback word in case of API failure