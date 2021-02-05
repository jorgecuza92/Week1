# # Assignment 1
#
# first = input('What is your first name?: ')
# last = input('What is your last name?: ')
#
# print(f'Hello, my name is {first} {last}')
#
# # Assignment 2
#
# total = float(input('enter the total amount: '))
#
# tip = float(input('enter the tip percentage amount as a decimal: '))
#
# full_bill = (tip * total) + total
# print(f'Your total bill for the day is: {full_bill}')
#

# Assignment_1
def calc():
    number_1 = int(input('enter your first number: '))
    operator = input('enter the operand: ')
    number_2 = int(input('enter your second number: '))

    if operator == '+':
        print(number_1 + number_2)
    elif operator == '*':
        print(number_1 * number_2)
    elif operator == '/':
        print(number_1 / number_2)
    else:
        print(number_1 - number_2)
calc()

# Assignment_2
number = int(input('input a number: '))

if number % 2 == 0:
    print('this number is even')
else:
    print('this number is odd')

# Assignment 3
number = int(input('input a number: '))

if number % 3 == 0 and number % 5 == 0:
    print('Fizz Buzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print(f'{number} is not divisible by 3 or 5')
