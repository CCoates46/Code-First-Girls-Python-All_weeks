import requests

listOfPokiIds = [1, 2]

for pokiId in listOfPokiIds:
    url = 'https://pokeapi.co/api/v2/pokemon/{}'. format(pokiId)
    res = requests.get(url)
    pokemon = res.json()
    print(pokemon["name"])

