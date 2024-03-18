# def sum_str(a, b):
#     if a == '':
#         a = '0'
#     if b == '':
#         b = '0'
#     return str(int(a) + int(b))


# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))

# def multiple_of_index(arr):
#     return [num for idx, num in enumerate(arr) if num % idx == 0 and idx > 0]

# def multiple_of_index(arr):
#     result = []

#     for idx, num in enumerate(arr):
#         if idx == 0:
#             if num == 0:
#                 result.append(num)
#             else:
#                 continue
#         elif num % idx == 0:
#             result.append(num)

#     return result


# def multiple_of_index(arr):
#     return [num for idx, num in enumerate(arr) if num == 0 or (idx != 0 and num % idx == 0)]

# # def multiple_of_index(arr):
# #     return [x for i,x in enumerate(arr) if x==0 or (i!=0 and x%i == 0)]

# print(multiple_of_index([0,0,2]))


# def is_isogram(string):
#     my_string = sorted(string.lower())

#     i = 0
#     while i < len(my_string) - 1:
#         if my_string[i] == my_string[i+1]:
#             return False
#         i += 1
#     return True  

# def is_isogram(string):
#     lower = string.lower()
#     for char in lower:
#         if lower.count(char) != 1:
#             return False
        
#     return True

# def is_isogram(string):
#     lower = string.lower()
#     for char in string.lower():
#         if string.lower().count(char) != 1:
#             return False
        
#     return True

# is_isogram('bep')

# def is_isogram(string):
#     return len(string) == len(set(string.lower()))

# def is_isogram(string):
#     lower = string.lower()
#     for char in string.lower():
#         if string.lower().count(char) != 1:
#             return False
        
#     return True


# def persistence(n):
#     if len([*str(n)]) == 1:
#         return 0
    
#     times = 0
#     while True:
#         product = 1
#         for num in [*str(n)]:
#             product *= int(num)

#         times += 1

#         if product < 10:
#             break

#         n = product
#     return times



# def persistence(n):
#     n = str(n)
#     count = 0

#     while len(n) > 1:
#         product = 1
#         for digit in n:
#             product *= int(digit)
#         n = str(product)
#         count += 1

#     return count


# import operator
# from functools import reduce
# def persistence(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i


# import operator
# from functools import reduce
# def persistence(num):
#     count = 0
#     while num > 9:
#         num = reduce(operator.mul, [int(digit) for digit in str(num)], 1)
#         count += 1
#     return count


# import operator
# from functools import reduce
# def persistence(num):
#     count = 0

#     while num > 9:
#         num = reduce(operator.mul, [int(digit) for digit in str(num)], 1)
#         count += 1

#     return count

# print(persistence(999))

# def tower_builder(n):
#     tower = []
#     i = 1
#     stars = 1

#     for row in range(1, n+1):
#         spaces = n - i

#         tower.append((spaces * ' ') + (stars * '*') + (spaces * ' '))
#         i += 1
#         stars += 2

#     return tower

# def tower_builder(n):
#     result = []
    
#     i = 2 * n - 1 
#     j = 1
#     spaces = i * ' ' 
#     stars = j * '*'

#     for row in range(1, n+1):
#         result.append((spaces * ' ') + (stars * '*') + (spaces * ' '))
#         spaces -= 2
#         stars += 2

#     print(result)
#     return result

# tower_builder(6)


# def tower_builder(n):
#     tower = []
#     stars = 1
#     spaces = n - 1

#     for _ in range(0, n):
#         tower.append((spaces * ' ') + (stars * '*') + (spaces * ' '))
#         stars += 2
#         spaces -= 1

#     return tower



# def tower_builder(floors):
#     result = []

#     for floor in range(1, floors+1):
#         stars = '*' * (2 * floor - 1)
#         space = ' ' * (floors - floor)
#         result.append(space + stars + space)
    
#     return result



# def tower_builder(floors):
#     return [('*' * (2 * floor - 1)).center(floors * 2 - 1) for floor in range(1, floors + 1)]

# # def tower_builder(floors):
# #     result = []

# #     for floor in range(1, floors+1):
# #         stars = '*' * (2 * floor - 1)
# #         space = ' ' * (floors - floor)
# #         result.append(space + stars + space)
    
# #     return result

# print(tower_builder(4))


# def multi_table(number):
#     result = ''
    
#     for row in range(1, 11):
#         result += f"{row} * {number} = {row * number}\n"

#     return result.rstrip()


# def multi_table(number):
#     return '\n'.join(f"{row} * {number} = {row * number}" for row in range(1, 11))

# print(multi_table(0))


# def human_years_cat_years_dog_years(human_years):
#     cat = 0
#     dog = 0
    
#     if human_years > 0:
#         cat += 15
#         dog += 15
    
#     if human_years > 1:
#         cat += 9
#         dog += 9

#     if human_years > 2:
#         cat += (human_years - 2) * 4
#         dog += (human_years - 2) * 5

#     return[human_years, cat, dog]

# def human_years_cat_years_dog_years(human):
#     cat = 15 * (human > 0) + 9 * (human > 1) + 4 * (human - 2) * (human > 2)
#     dog = 15 * (human > 0) + 9 * (human > 1) + 5 * (human - 2) * (human > 2)
#     return[human, cat, dog]




def count_sheep(n):
    return ''.join(f"{sheep_number} sheep..." for sheep_number in range(1, n+1))


def count_sheep(n):
    murmur = ''
    for sheep in range(1, n + 1):
        murmur += f"{sheep} sheep..."

    return murmur