import requests

BASE_URL = "https://rickandmortyapi.com/api/character"

def get_characters():
    response = requests.get(BASE_URL)
    return response.json()