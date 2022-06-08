import random
import requests
from pprint import pprint

wizard_name = random.choice()
url = 'http://hp-api.herokuapp.com/api/characters'.format(wizard_name)
response = requests.get(url)
pprint(response)
wizards = response.json()
print(wizard_name)