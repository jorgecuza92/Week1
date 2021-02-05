#
# number = int(input('enter a number ot check if it is a prime number: '))
# def prime_or_not(number):
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 print(number, 'is not a prime number')
#                 break
#             else:
#                 print(number, 'is a prime number')
#                 break
#     else:
#         print(number, 'is not a prime number')
#
# prime_or_not(number)


# number = int(input('enter a number to see if it is prime or not: '))

# def prime(number):
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 print(number, 'is not a prime number')
#                 break
#             else:
#                 print(number, 'is a prime')
#                 break
#     else:
#         print(number, 'is not an integer')
#
# prime(number)


num = 7
def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print('NOT A PRIME NUMBER')
                return False
            else:
                print('PRIME NUMBER')
                return True
    else:
        print('this is not a prime number nor a positive integer')
prime(num)
