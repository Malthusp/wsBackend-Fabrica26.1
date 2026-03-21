import requests

BASE_URL = "https://rickandmortyapi.com/api/episode"

def get_episodes():
    response = requests.get(BASE_URL)
    return response.json()