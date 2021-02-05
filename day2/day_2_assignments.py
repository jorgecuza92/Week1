# string concatenation
# first_name = 'john'
# last_name = 'doe'


# Immutability - string are immutable/ they can not be changed
# print(first_name + last_name + '22' + 'aa' + 'ff')

# string interpolation

# company = 'digitalcrafts'
# cohort = 'feb 2021'
#
# message = f'welcome to {company} and cohort is {cohort}' # f-strings
# print(message)


# asking for user input
# full_name = input('Please enter your full name: ')  # datatype is always a string
# car_name = input('enter make of your car: ')
# print(f'{full_name} is your name, {car_name} is your car')

# Assignment 1

# first = input('What is your first name?: ')
# last = input('What is your last name?: ')

# print(f'Hello, my name is {first} {last}')

# Assignment 2

# total = float(input('enter the total amount: '))
#
# tip = float(input('enter the tip percentage amount: '))
#
# tip_amount = ((tip / 100) * total)
# print(f'Your total bill for the day is: {tip_amount}')


# def calculate_tip(amount, tip_percentage):
#     return amount * (tip_percentage / 100)
#
#
#
# amount = float(input('how much was the bill?: '))
# tip_percentage = float(input('how much percent do you want to tip?: '))
#
# tip = calculate_tip(amount, tip_percentage)
# print(tip)


def tip_amount():
    total = float(input('how much was the total bill?: '))
    tip_perc = float(input('percent of tip?: '))
    tip = (tip_perc / 100) * total
    print(the amount of tip is:tip)

tip_amount()


# functions should be small, reusable, should only do one thing only.
# display_user() will result in error because it is not yet defined.
# customer_id = '123456'
#
#
# def display_user():  # function
#     print('*****')
#     print(f'my first name is {first_name}, my last name is {last_name}')
#     print(f'{customer_id}*****')


# display_user()  # there are print lines inside display_user no need for print() wrapping

def greet(name, age):  # name is local variable and only available inside the function
    print(f'hello {name}, you are {age} years old.')


greet('mary', 34)  # passing argument to the function
greet('alex', 60)
greet('jorge', 28)


# a good function is a function with NO arguments

# print(age)  # will cause error because age is only available inside the function.

def calculate_overdraft_fee(amount):
    return amount * 0.10
    print('not executed')


overdraft_fee = calculate_overdraft_fee(100)
if overdraft_fee > 20:
    print('lock account')


def add(no1, no2):
    return no1 + no2


result = add(2, 3)
print(result)


#  tuple (can return two values)

def airportNameAndCode():
    return ("intercontinental Airport", 'IAH')  # TUPLE!
    # return "IAH" (will not return because return is already executed above)


(airport_name, airport_code) = airportNameAndCode()


# Optional Arguments
def greet_with_optional_age(name, age=32):
    print(name)
    print(age)


greet_with_optional_age('jorge cuza')  # can ignore second argument, will assign 32 default

greet_with_optional_age('jorge', 28)




# Conditions

user_age = 18
citizen = 'US'

if user_age >= 18 and citizen == 'US':
    print('user is greater than 18')
    greet_with_optional_age('john doe', user_age)
elif user_age < 18 and citzen == 'AUS':
    print('under 18')
else:
    print('user is over/under 18 and not/is citizen from US')

number = 10

if number % 2 == 0:
    print('even')
else:
    print('odd')
# elif (number % 2) != 0:
#     print('odd')