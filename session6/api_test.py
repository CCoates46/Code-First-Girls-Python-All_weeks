import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
res = requests.get(url)

print(res)

pokemon = res.json()

allAbilities = pokemon['abilities']
#print(type(allAbilities))

for ability in allAbilities:
    print(ability['name'])


