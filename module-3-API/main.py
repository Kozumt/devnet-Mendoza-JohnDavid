import random
import requests

#3 max guesses
POKEMON_LIST = ["pikachu", "charmander", "bulbasaur", "squirtle", "lugia", "snorlax"]
MAX_ATTEMPTS = 3

#Fetches one pokemon data, return
def get_pokemon(name):
    """Fetch a Pokemon from PokeAPI and return its name, height and weight.
    Returns None if the Pokemon is not found or a network error occurs."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

#Sends request
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")
        return None

# Checking the HTTP status if it responds
    if response.status_code != 200:
        print(f"Could not get data for '{name}' (status code: {response.status_code}).")
        return None

#Json response into python dictionary
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"], 
        "weight": data["weight"], 
    }

