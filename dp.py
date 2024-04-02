# def chromosome_check(chromosome):
#     sex = 'son' if 'Y' in chromosome else 'daughter'
#     return f"Congratulations! You're going to have a {sex}." 

# for num in range(1, 100):
#     print(num * 2)

# lst = [1, 3, 7, 15]
# index = 0

# i = 0
# while i < len(lst):
#     print(lst[i])
#     i += 1

# friends = ['Sarah', 'John', 'Hannah', 'Dave']

# for friend in friends:
#     print(f"Hi, {friend}")

# cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
#           'Vienna', None, 'London', 'Beijing', None]

# for city in cities:
#     if not city:
#         continue
#     print(len(city))

# while True:
#     print("and on")
#     break

# fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

# for fish in fish_list:
#     print(fish)
#     if fish == 'Nemo':
#         break

# while True:
#     print('Should I stop looping?')
#     answer = input()
#     if answer == 'Yes':
#         break

# def factorial(n):
#     result = 1

#     while n > 1:
#         result *= n
#         n -= 1

#     return result


# def factorial(n):
#     result = 1

#     for i in range(1, n+1):
#         result *= i

#     return result

# print(factorial(5))

# def whatday(num):
#     match num:
#         case 1:
#             return 'Sunday'
#         case 2:
#             return 'Monday'
#         case 3:
#             return 'Tuesday'
#         case 4:
#             return 'Wednesday'
#         case 5:
#             return 'Thursday'
#         case 6:
#             return 'Friday'
#         case 7:
#             return 'Saturday'
#         case default:
#             "Wrong, please enter a number between 1 and 7"

# print(whatday(8))

# False 
# None
# 0 
# ''
# []
# {}
# ()
# set()
# range(0)

# import random
# random_number = random.randint(0, 1)

# print('Yes' if random_number else 'No')

# if random_number:
#     print('Yes')
# else:
#     print('No')


# weather = 'sunny'

# match weather:
#     case 'sunny':
#         print('Sunny')
#     case 'rainy':
#         print('rain')
#     case _:
#         print('stay inside')

# elif weather == 'rainy':
#     print('RAin!')
# else:
#     print('stay inside')

# def multiply(int1, int2):
#     return int1 * int2

# def bruce_eckel_quote():
#     print('Python is executable pseudocode.')

# def cite(author, quote):
#     print(f"{author} said: {quote}")

# def square(num):
#     return num ** 2

# def compare_lengths(str1, str2):
#     if len(str1) < len(str2):
#         return -1
#     elif len(str1) > len(str2):
#         return 1
#     else:
#         return 0
    
# name = 'Captain Ruby'
# name2 = name[:8] + 'Python'

# def greet(code):
#     match code:
#         case 'en':
#             return 'Hi!'
#         case 'fr':
#             return 'Salut' 
        
# def extract_region(locale):
#     return locale.split('_')[1][:2]

# def extract_region(locale):
#     return locale.split('.')[0].split('_')[1]

# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

# def greet(language_code):
#     match language_code:
#         case 'US':
#             return 'Hey!'
#         case 'GB':
#             return 'Hello!'
#         case 'AU':
#             return 'Howdy!'
#         case 'FR':
#             return 'Salut!'
#         case 'CA':
#             return 'Salut!'
#         case 'MA':
#             return 'Salut!'
        
# def local_greet(locale):
#     return greet(locale.split('_')[1].split('.')[0])

# print(local_greet('en_US.UTF-8'))       # Hey!
# print(local_greet('en_GB.UTF-8'))       # Hello!
# print(local_greet('en_AU.UTF-8'))       # Howdy!
# print(local_greet('fr_FR.UTF-8'))       # Salut!
# print(local_greet('fr_CA.UTF-8'))       # Salut!
# print(local_greet('fr_MA.UTF-8'))       # Salut!

# x = 10

# def my_function():
#     x = x + 5
#     print(x)

# my_function()

# name = 'Roger' 
# print(name.lower() == 'RoGeR'.lower())
# print(name.lower() == 'DAVE'.lower())

# var = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'

# print(var)

# def is_empty(stri):
#     return not stri

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True

# def is_empty_or_blank(my_str):
#     return not my_str.strip()

# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True

# 'launch school tech & talk'.title()

# def starts_with(s, beg):
#     return s.startswith(beg)

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

# def count_substrings(s, sub):
#     return s.count(sub)

# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0

# def last(arr):
#     if arr:
#         return arr[-1]
#     else:
#         return None
    
# energy.pop()
# energy.append('geothermal')

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# list(alphabet)

# scores = [96, 47, 113, 89, 100, 102]

# total = 0
# for score in scores:
#     if score >= 100:
#         total += 1

# [num for num in scores if num >= 100]

# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for row in vocabulary:
#     for word in row:
#         print(word)

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# # etc...

# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'


# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']

# # def contains(city, arr):
# #     return destinations.count(city) > 0

# def contains(city, arr):
#     for dest in arr:
#         if dest == city:
#             return True
#     return False

# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False

# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# new = ''
# for i in range(len(passcode)):
#     if i > 0:
#         new += '-'
#     new += passcode[i]

# new


# full = ''
# for part in passcode:
#     full += part + '-'

# full[:-1]

# '-'.join(passcode)

# Write some code here.
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

def buy(arr):
    while grocery_list:
        bought = grocery_list.pop(0)
        print(bought)

buy(grocery_list)

print(grocery_list)