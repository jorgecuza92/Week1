# cars = [{'make': 'Honda'}, {'make': 'Toyota'}]
# car = cars[0] # change by reference
# car['make'] = "TESLA" # replaces index 0 of the cars array. Honda will be replaced to 'TESLA' at position 0
# print(cars)

# OPTION 1
# import pizza # pizza.create_pizza(12, ['onions', 'mushrooms', 'chicken'])
# import american_pizza

# OPTION 2
# from pizza import create_pizza, deliver_pizza # do not need pizza. prefix

# OPTION 3 (Alias)
import pizza as p # p.create_pizza(16, ['onions', 'mushrooms', 'chicken'])
import american_pizza as ap # ap.create_pizza(16, ['onions', 'mushrooms', 'chicken'])

# OPTION 4
from pizza import * # from everything from pizza module (file) call create_pizza(?, ?)

# import utils # import more than one file example
#
# utils.is_palindrome('cat')

print('enter 1 to create pizza: ')
print('enter 2 to add delivery address: ')
print('enter q to quit: ')
print()
# american_pizza.create_pizza(14, ['onions'])
# pizza.create_pizza(16, ['onions', 'mushrooms', 'chicken']) # name_of_import.function_name
#
# pizza.deliver_pizza('1200 richmond ave Houston, TX')


create_pizza(16, ['onions', 'mushrooms', 'chicken']) # name_of_import.function_name

deliver_pizza('1200 richmond ave Houston, TX')



print('hello world')