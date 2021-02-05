# def check_palindrome_1(string):
#     reversed_string = string[::-1]
#     return True
#     if string!=reversed_string:
#         return False
#
#
# string = input("Enter the string: ")
# status= check_palindrome_1(string)
# if True:
#     print("It is a palindrome ")
# else:
#     print("Sorry! Try again")


string = input('enter a word: ')

if string == string[::-1]:
    print(string, 'is a palindrome')
else:
    print(string, 'is not a palindrome')
