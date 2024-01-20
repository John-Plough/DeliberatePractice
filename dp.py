# 02-conditionals1.md

# # Use a variable to store a number, then write a condition that prints 0 if the number is equal to 10, and prints -1 otherwise.

# num = 8
# if num == 10:
#     print(0)
# else:
#     print(-1)

# # Use a variable to store a number, then write a condition that prints -1 if the number is less than 10, prints 1 if the number is greater than 10, and prints 0 if the number is equal to 10.
    
# num = 4
# if num < 10:
#     print(-1)
# elif num > 10:
#     print(1)
# else:
#     print(0)

# # Use variables to store two numbers, then write a condition that prints 1 if the numbers are both less than 10, and prints 0 otherwise.

# num1 = 5
# num2 = 8
# if num1 < 10 and num2 < 10:
#     print(1)
# else:
#     print(0)

# # Use a variable to store a number, then write a condition that prints 1 if the number is over 9000, and prints -1 otherwise.

# num = 100
# if num > 9000:
#     print(1)
# else:
#     print(-1)

# # Use a variable to store a number, then write a condition that prints 9 if the number is less than 10, prints 19 if the number is less than 20, prints 29 if the number is less than 30, and prints -1 otherwise (only one print statement should occur).

# num = 15
# if num < 10:
#     print(9)
# elif num < 20:
#     print(19)
# elif num < 30:
#     print(29)
# else:
#     print(-1)

# Use variables to store two numbers, then write a condition that prints 100 if either number is greater than 10, and prints -100 otherwise.

num1 = 12
num2 = 8
if num1 > 10 or num2 > 10:
    print(100)
else:
    print(-100)

# Use a variable to store a number, then write a condition that prints 1776 if the number is less than 0, and prints 1979 otherwise.

num = 1500
if num < 0:
    print(1776)
else:
    print(1979)

# Use a variable to store a number, then write a condition that prints 100 if the number equals 100, prints 99 if the number is equal to 99, and prints 0 otherwise.

num = 100
if num == 100:
    print(100)
elif num == 99:
    print(99)
else:
    print(0)

# Use variables to store two numbers, then write a condition that prints 1 if the first number is less than zero and the second number is greater than 0, and prints 0 otherwise.

num1 = -4
num2 = 4
if num1 < 0 and num2 > 0:
    print(1)
else:
    print(0)

# Use a variable to store a number, then write a condition that prints 5 if the number is greater than 80, prints 4 if the number is greater than 60, prints 3 if the number is greater than 40, prints 2 if the number is greater than 20, and prints 1 otherwise (only one print statement should occur).

num = 65
if num > 80:
    print(5)
elif num > 60:
    print(4)
elif num > 40:
    print(3)
elif num > 20:
    print(2)
else:
    print(1)


# def in_list(strings, str):
#     print('John')
#     # if str in strings:
#     #     return strings.index(str)
#     for index, word in enumerate(strings):
#         if word == str:    
#             return index
#     return -1
    
# print(in_list(['hi', 'bye'], 'bye'))

# print(type(list(range(3))))

# for idx, color in ["red", "green", "blue"]:
#   print(color, idx)