import math

meal_cost = 20

meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have discount? y/n ')
discount_applicable = discount_choice == 'y'
meal_applicable = meal_price > meal_cost

if meal_applicable and discount_applicable:
    meal_price = (math.trunc(meal_price * 0.9))
    print('Discount applied')
else: print('No Discount')

print('Total cost: {} '.format(meal_price))
