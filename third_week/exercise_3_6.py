import random


def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side


choice = input('Choose heads or tails: ')
result = flip_coin()

if result == choice:
    print('The coin landed on {}, YOU WIN!!!!!!'. format(result))
else:
    print('The coin landed on {}, YOU LOSE :-('.format(result))

