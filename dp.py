# def no_space(x):
#     return x.replace(' ', '')
    # return ''.join(x.split())

# def basic_op(operator, value1, value2):
#     pass

# def basic_op(operator, value1, value2):
#     operations = {
#         '+': value1 + value2,
#         '-': value1 - value2,
#         '*': value1 * value2,
#         '/': value1 / value2
#     }
#     return operations[operator]

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:


# def count_sheeps(sheep):
#     return sheep.count(True)

# def count_sheeps(sheep):
#     total = 0

#     for i in sheep:
#         if i == True:
#             total += 1

#     return total

# def century(year):
#     return year // 100 if year % 100 == 0 else (year // 100) + 1

# def abbrev_name(name):
#     return '.'.join(item[0] for item in name.upper().split())

# def digitize(n): 
#     return [int(char) for char in str(n)[::-1]]

# def greet(name):
#     return f"Hello, {name} how are you doing today?"

# def summation(num):


# def summation(num):
#     return (num * num + num) / 2

    # return (1 + num) * num / 2

    # return sum(range(1, num+1))

# def move_zeros(lst):
#     zeros = []
#     others = []

#     for idx, num in enumerate(lst):
#         if num == 0:
#             zeros.append(lst[idx])
#         else:
#             others.append(lst[idx])
            
#     return others + zeros

# def move_zeros(lst):
#     for num is lst:
#         if num == 0:
#             lst.remove(num)
#             lst.append(num)
#     return lst



# class Solution:
#     def intToRoman(self, num: int) -> str:

#         converter = [   #holds tuples of (roman numeral, integer)
#         ('M', 1000),
#         ('CM', 900),
#         ('D', 500),
#         ('CD', 400),
#         ('C', 100),
#         ('XC', 90),
#         ('L', 50),
#         ('XL', 40),
#         ('X', 10),
#         ('IX', 9),
#         ('V', 5),
#         ('IV', 4),
#         ('I', 1)
#         ]

#         roman_num = ''  #building up this string over our for-loop

#         for pair in converter:  #looping over each tuple in our converter list
#             roman = pair[0]
#             integer = pair[1]
#             dividend = num // integer

#             if dividend > 0:
#                 roman_num += roman * dividend   #adding current numeral this many times
#                 num -= integer * dividend       #decrementing by integer value this many times

#         return roman_num


# def cakes(recipe, available):
#     total = float('inf')
#     for ingredient in recipe:
#         if ingredient in available:
#             max = available[ingredient] // recipe[ingredient]
#             if max < total:
#                 total = max
#         else:
#             return 0
    
#     return int(total)

# def cakes(recipe, available):
#     return min(available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe)

# print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))


# def guess_gifts(wishlist, presents): 

#     #loop over wishlist arr
#         #for each item, compare vals to vals of pres
    
    
# wishlist =      [
#                     {'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
#                     {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
#                     {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}
#                 ]

# presents =      [
#                     {'size': "medium", 'clatters': "a bit", 'weight': "medium"},
#                     {'size': "small", 'clatters': "yes", 'weight': "light"}
#                 ]

# gifts = []
# loop over enumerate(presents:)
#     for each item:
#         for each item in wishlist
#             if size, clat, weight in wishlist.values == 0:
#                 gifts.append wishlist[name]
# return gifts

# def guess_gifts(wishlist, presents): 
#     gifts = []
#     for i, item1 in enumerate(presents):
#         for j, item2 in enumerate(wishlist):
#             if item1['size'] == item2['size'] and item1['clatters'] == item2['clatters'] and item1['weight'] == item2['weight']:
#                 gifts.append(wishlist['name'])
#     return gifts

# wishlist = [{'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
#             {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
#             {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}]
# presents = [{'size': "medium", 'clatters': "a bit", 'weight': "medium"},
#             {'size': "small", 'clatters': "yes", 'weight': "light"}]

# def guess_gifts(wishlist, presents): 
#     gifts = []
#     for present in presents:
#         print(f"present is --> {present}")
#         for wish in wishlist:
#             print(f"   wish is --> {wish}")
#             if present['size'] == wish['size'] and present['clatters'] == wish['clatters'] and present['weight'] == wish['weight'] and wish['name'] not in gifts:
#                 gifts.append(wish['name'])
#     return gifts

# def guess_gifts(wishlist, presents): 
#     gifts = []

#     for present in presents:
#         for wish in wishlist:
#             if (present['size'] == wish['size'] and 
#                 present['clatters'] == wish['clatters'] and 
#                 present['weight'] == wish['weight']:
#                 gifts.append(wish['name'])
#     return set(gifts)

# print(guess_gifts(wishlist, presents))

# wishlist =      [
#                     {'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
#                     {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
#                     {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}
#                 ]

# presents =      [
#                     {'size': "medium", 'clatters': "a bit", 'weight': "medium"},
#                     {'size': "small", 'clatters': "yes", 'weight': "light"}
#                 ]

# def find_needle(haystack):
#     return f"found the needle at position {haystack.index('needle')}"



# def spin_words(sentence):

#     return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())


        

def likes(names):
    match len(names):
        case 0: return 'no one likes this'
        case 1: return f"{names[0]} likes this"
        case 2: return f"{names[0]} and {names[1]} like this"
        case 3: return f"{names[0]}, {names[1]} and {names[2]} like this"
        case _: return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

# def likes(names):    
#     if len(names) == 0:
#         return 'no one likes this'
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     elif len(names) > 3:
#         return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

print(likes([]))
print(likes(['John', 'Tim', 'Derek', 'Sal', 'Kiber']))