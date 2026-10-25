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

#Game chooses on pokemon_list, function of guessing round
def play():
    answer_name = random.choice(POKEMON_LIST)
    pokemon = get_pokemon(answer_name)

    if pokemon is None:
        print("The game need to restart. Please check your connection and try again.")
        return

    print("=== WHO'S THAT POKEMON? ===")
    print(f"Height: {pokemon['height'] / 10} m")
    print(f"Weight: {pokemon['weight'] / 10} kg")
    print(f"You have {MAX_ATTEMPTS} attempts.\n")

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        guess = input(f"Attempt {attempts + 1}/{MAX_ATTEMPTS} - Your guess: ").strip().lower()

#Handles empty input
        if not guess:
            print("Please enter a Pokemon name.")
            continue

 
        attempts += 1
 
        if guess == pokemon["name"]:
            print(f"Correct! It's {pokemon['name'].capitalize()}! You win!")
            return