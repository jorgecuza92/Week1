# DICTIONARIES

# Dictionary = {key: value}
airport = {'IAH': 'Intercontinental Airport'}

# access value

name = airport['IAH']
print(name)

empty_dic = {}

empty_dic['drink_of_choice'] = 'Jack Daniels'

print(empty_dic)
print(empty_dic['drink_of_choice']) # remember, accesses value

for key in empty_dic:
    print(empty_dic[key]) # prints all values in the dictionary
    print(key)  # prints all keys in the dictionary
    print(empty_dic['drink_of_choice']) # prints specfic value with specified key

for key, value in empty_dic.items():    # option to access keys and values
    print(key,'is the key',value, 'is the value')

for value in empty_dic.values():    # option to access values
    print(value)

print()
# ACTIVITY 1

# first = input('whats your first name?: ')
# last = input('whats your last name?: ')

name_info = {}

name_info['first_name'] = 'Ivonne'
name_info['last_name'] = 'Cuza'

print(f"my name is {name_info['first_name']} {name_info['last_name']}") # f strings with dictionary keys to show value

# for key, value in name_info.items():
#     print(f"my first name is {key}, my last name is {value}")

# NESTING DICTIONARIES AND ARRAYS

first_name = input('what is your first name?: ')
last_name = input('what is your last name?: ')

home_address = {'street': '123 poo st.', 'city': 'houston'}
vacation_home = {'street': "345 fart st., 'city: Austin"}

addresses = [home_address, vacation_home]

user_info = {'first_name': first_name, 'last_name': last_name, 'address(s)': addresses}

print(user_info)



