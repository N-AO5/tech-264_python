Guidance:

* Work in your groups of 2-3 to make a single game
* API documentation: PokéAPI (pokeapi.co)
* Recommended: Understand the Pokemon lookup program first (code below) to fully understand accessing data from the API.
* The Pokémon data MUST come from the PokeApi
* Get random Pokémon for at least the CPU (Player can be chosen or random)
* Pokémon should fight and a winner should be declared in some way
* No Pygame. Focus on interacting with the API.
* Be as creative as you like after this. Can you incorporate different abilities/stats etc.?
* Try and work collaboratively on the one repo using Git
* To deliver: Give it your best shot! Share your code (message your Ramon + Luke directly, NOT a message in the main chat) by COB (17:00)

User Stories:
* as a player i want get a random pokemon to play as CPU so each battle is with pokemon
* as a player i want to be able to choose my pokemon so i can battle with the CPU
* as a player i want to have a winner declared after the battle so i can know if my chosen pokemon won

*as a player i want to be able to see stats of my chose pokemon before i battle so that i can choose the right pokemon for the battle
````

Starter code:

import requests
import json

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))
````