# numbers = [1, 2, 3, 4, 5]
#
# for number in reversed(numbers):
#     print(number)


# range(start, stop, step)

# create a variable and set it equal to the reverse list of numbers using slicing
# reversed_numbers = numbers[::-1]
#
# for number in reversed_numbers:
#     print(number)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# for number in range(len(numbers) -1, -1, -1):
#     print(numbers[number])
#
# for number in range(len(numbers) - 1, -1, -1):  # Reversing array
#     print(numbers[number])

reversed_numbers = numbers[::-1]
print(reversed_numbers)
#
#
# for number in reversed_numbers:
#     print(number)

for number in range(len(numbers) - 1, -1,-1):
    print(numbers[number])
