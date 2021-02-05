# REVIEW

# PALINDROME
word = 'stop'
# for index in range(0, len(word)):
#     print(word[index])

# reverse order
reversed_word = ''
for index in range(len(word) -1, -1):
    reversed_word = reversed_word + word[index]
    print(reversed_word)


# for index in range(0, len(word)):   # loops through word (string) characters
#     print(word[index])

# reverse word?
# reversed_word = ''
# for index in range(len(word) -1, -1, -1):
#     # reversed_word = reversed_word + word[index]
#     reversed_word += word[index]
#
# if word == reversed_word:
#     print('PALINDROME')
# else:
#     print('NOT A PALINDROME')



# def is_palindrome(word):
#     for index in range(len(word)-1, -1, -1):
#         reversed_word += word[index]
#     return word == reversed_word # result will be True or False
    # if word == reversed_word:
    #     return True
    #
    # return False

# word = input('enter a word: ')
#
# if is_palindrome(word) == True: # is_palindrome called here
#     print('Palindrome')
# else:
#     print('Not a Palindrome')


# FACTORIAL
result = 1
number = int(input(' enter a number: '))
for index in range(1, number + 1):  # add +1 because end stop in range fx is excluded
    result = result * index
print(result)
print()
print()
