from itertools import chain
# 03-loops2.md

# Start with an array of numbers and create a new array with each number times 3.
# For example, [1, 2, 3] becomes [3, 6, 9].

# arr = [1,2,3,4]

# new_arr = []
# for num in arr:
#     new_arr.append(num * 3)

# tripled = [num * 3 for num in arr]

# print(new_arr)
# print(tripled)

# Start with an array of strings and create a new array with each string upcased.
# For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

# animals = ['panda', 'koala', 'otter']

# shouting_animals = [animal.upper() for animal in animals]
# print(shouting_animals)

# Start with an array of hashes and create a new array of string values from each hash's :name key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].

# animals = [
#     {'name': 'ned', 'animal': 'panda'},
#     {'name': 'frank', 'animal': 'koala'},
#     {'name': 'kevin', 'animal': 'otter'},
# ]

# names = [animal['name'] for animal in animals]
# print(names)

# Start with an array of numbers and create a new array with each number plus 7.
# For example, [1, 2, 3] becomes [8, 9, 10].

# arr = [1,2,3,4]
# sevened = [num + 7 for num in arr]
# print(sevened)

# Start with an array of strings and create a new array with each string's length.
# For example, ["hello", "goodbye"] becomes [5, 7].

# animals = ['panda', 'koala', 'otter']
# length = [len(animal) for animal in animals]
# print(length)

# Start with an array of hashes and create a new array of number values from each hash's :age key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].

# animals = [
#     {'name': 'ned', 'animal': 'panda', 'age': 7},
#     {'name': 'frank', 'animal': 'koala', 'age': 4},
#     {'name': 'kevin', 'animal': 'otter', 'age': 9},
# ]

# ages = [animal['age'] for animal in animals]
# print(ages)

# Start with an array of numbers and create a new array with each number divided by 2.
# For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].

# arr = [1,2,3,4]
# halved = [num / 2 for num in arr]
# print(halved)

# Start with an array of strings and create a new array with each string's first letter only.
# For example, ["hello", "goodbye"] becomes ["h", "g"].

# animals = ['panda', 'koala', 'otter']
# first_only = [animal[0] for animal in animals]
# print(first_only)

# Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].

# animals = [
#     {'name': 'ned', 'animal': 'panda', 'age': 7},
#     {'name': 'frank', 'animal': 'koala', 'age': 4},
#     {'name': 'kevin', 'animal': 'otter', 'age': 9},
# ]
    
# age_doubled = [animal['age'] * 2 for animal in animals]
# print(age_doubled)

# Start with an array of numbers and create a new array with each number converted into a string.
# For example, [1, 2, 3] becomes ["1", "2", "3"].

# arr = [1,2,3,4]
# str_of_num = [str(num) for num in arr]
# print(str_of_num)

# animals = [
#     {'name': 'ned', 'animal': 'panda', 'age': 7},
#     {'name': 'frank', 'animal': 'koala', 'age': 4},
#     {'name': 'kevin', 'animal': 'otter', 'age': 9},
# ]

# for animal in animals:
#     for value in animal.values():
#         print(value)

# frank = {'name': 'frank', 'animal': 'koala', 'age': 4}

# for val in frank.values():
#     print(val)

# for item in frank.items():
#     print(item)

# for k, v in frank.items():
    # print(f"key is: {k} | value is: {v}")

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
for v in donations.values():
    total_donations += v

# print(total_donations)

# print('sam' in donations)
# print('chuck' in donations)
# print('li' in donations)
# print(25 in donations.values())
# print(13 in donations.values())
# print(400 in donations.values())

# print(donations)
# donations.clear()
# print(donations)
    
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 
    
# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state

initial_game_state = dict.fromkeys(game_properties, 0)

# print(initial_game_state)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"

stock_list['cookie'] = 18

# remove 'cake' from stock_list USE A DICTIONARY METHOD

# stock_list.pop('cake')
# # print(stock_list)

# list1[i], list2[i] for i in range(0, len(list1))

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]: list2[i] for i in range(0, len(list1))}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
# answer = {item[0]: item[1] for item in person}
# answer = {k:v for k,v in person}
# # print(answer)

# dicti = dict(person)
# print(dicti)

# answer = {row[0]: row[1] for row in person}
# answer = {k:v for k,v in person}
answer = dict(person)
# print(answer)

# make sure your solution is assigned to the answer variable so the tests can work!
vowels = ['a', 'e', 'i', 'o', 'u']

# answer = dict.fromkeys(vowels, 0)
# answer = {char:0 for char in vowels}

answer = {char:0 for char in 'aeiou'}
# answer = dict.fromkeys('aeiou', 0)

# print(answer)

# make sure your solution is assigned to the answer variable so the tests can work!

# vowels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nums = range(65, 91)

# answer = {nums[i]: vowels[i] for i in range(0, len(vowels))}
# print(answer)


# vowels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nums = range(65, 91)

answer = {range(65, 91)[i]: chr(range(65, 91)[i]) for i in range(0, len(range(65, 91)))}
# print(answer)

answer = {count: chr(count) for count in range(65,91)} 

answer = {num: chr(num) for num in range(65,91)}
# print(answer)

smalls = {num: chr(num) for num in range(97,123)}
# print(smalls)

# answer.update(smalls)
all = dict(chain(answer.items(), smalls.items()))
print(all)