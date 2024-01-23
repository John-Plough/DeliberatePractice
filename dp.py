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