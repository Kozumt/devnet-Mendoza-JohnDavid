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
