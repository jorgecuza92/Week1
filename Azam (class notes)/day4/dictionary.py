# DICTIONARIES

# airport_code = 'IAH'
# airport_name = 'Intercontinental Airport'

# dictionary = {Key: Value}

# creating a dictionary
# airport = {'IAH': 'Intercontinental Airport'}

# access value from dictionary

# name = airport['IAH']
#
# print(name)

# Cars

# car = {'make': 'BMW', 'model': 'M3', 'price': 50000, 'isElectric': False}
#
# print(car['model'])

# empty dictionary
# user = {}
#
# user['first_name'] = 'John'
# user['last_name'] = 'Doe'
#
# print(user['middle_name']) # error, does not exist
# print(user)

# ACTIVITY 1
#
# first_name = input('first name: ')
# last_name = input('last name: ')

# user = {'first_name': first_name, 'last_name': last_name}
#
# print('my name is' + user['first_name'] + ' ' + user['last_name'])
#
# print(f"my name is {user['first_name']}, {user['last_name']}") # using fstrings with dictionaries

# NESTED DICTIONARIES
# first_name = input('first name: ')
# last_name = input('last name: ')
# # street = input('street: ')
# # city = input('city: ')
#
# home_address = {'street': '1200 Richmond ave', 'city': 'houston'}
# vacation_home_address = {'street': '123 poo st', 'city': 'Austin'}
#
# addresses = [home_address, vacation_home_address] # array with two addresses (array of dictionaries)
#
# user = {'first_name': first_name, 'last_name': last_name, 'addresses': addresses}
# print(user)
#

# ITERATING THROUGH THE DICTIONARY

# OPTION 1
dictionary = {'first': 'jorge', 'last': 'cuza'}
for key in dictionary:
    print(dictionary[key])  # prints the values
    print(key)  # prints the keys
print()

# OPTION 2

for value in dictionary.values():   # another option to print values
    print(value)

# OPTION 3
for key, value in dictionary.items():
    print(key)
    print(value)
print()
print()
# DELETE ITEM FROM DICTIONARY

electric_car = {'make': 'TESLA', 'model': 'Model S'}
print(electric_car)

print(electric_car)
