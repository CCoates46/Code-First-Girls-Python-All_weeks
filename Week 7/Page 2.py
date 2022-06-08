import requests


listOfPokiIds = []
allPokiNames = []

for x in range(4):
    userInput = input("Give me a poki ID: ")
    listOfPokiIds.append(userInput)

for pokiId in listOfPokiIds:
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokiId)
    res = requests.get(url)
    pokemon = res.json()
    allPokiNames.append(pokemon["name"])

print(allPokiNames)

with open("pokieFile.txt", "w") as f:
    for name in allPokiNames:
        f.write(name + "\n")