price = input('How much is a burger? ')
vegetarian = input('Is there a vegetarian option? (y/n) ')
within_budget = float(price) <= 10.00
has_vegetarian = vegetarian == 'y'
is_good_choice = within_budget and has_vegetarian
print('Restaurant meets criteria: {}'.format(is_good_choice))