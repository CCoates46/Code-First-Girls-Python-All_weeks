#today = input('What day is it? ')
#is_monday = today == 'Monday'
#print('Today is Monday: {}'.format(is_monday))

myBudget = 10.00
price = input('What is the price of the burger? ')
veggie = input('Do you have Vegetarian option? y/n ')
within_budget = float(price) <= 10.00
has_vegetarian = veggie == 'y'

if has_vegetarian and within_budget:
    print('This restaurant is a great choice!')
else:
    print('Probably not a good idea')






