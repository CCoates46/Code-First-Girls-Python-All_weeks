# To Do - Required Tasks

import requests
import random

# 1. Generate a random number between 1 and 151 to use as the Pokemon ID number
pokieDetails = {}
pokieId = random.randint(1, 151)
print('Task 1: Your random Pokemon Id is: {}'.format(pokieId))

# 2. Using the Pokemon API get a Pokemon based on its ID number

url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokieId)
res = requests.get(url)
pokemon = res.json()
print('Task 2: The name of your pokemon is: {}'.format(pokemon["name"]))

# 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (★
# https://pokeapi.co/)

pokieDetails.update({'Name': pokemon["name"],
                     'Id': pokemon["id"],
                     'Height': pokemon["height"],
                     'Weight': pokemon["weight"]})
print('Task 3: Dictionary {}'.format(pokieDetails))

# 4. Get a random Pokemon for the player and another for their opponent
my_Pokie = pokieId
print('Task 4: Random Player Pokemon is: {}'.format(my_Pokie))
randOpp = random.randint(1, 151)
print('Task 4: Opponent Pokemon is {}'.format(randOpp))

# 5. Ask the user which stat they want to use (id, height or weight)
user_stat = input('Which stat would you like to use? Choose from Id, Height or Weight')
# 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

my_stat = my_Pokie[user_stat]
opp_stat = randOpp[user_stat]
print('Task 6: My stat is {}'. format(my_stat))
print('Task 6: My opponent stat is {}'.format(opp_stat))




