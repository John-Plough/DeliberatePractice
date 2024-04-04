# # car = {
# #     'type': 'sedan',
# #     'color': 'blue',
# #     'mileage': 80000
# # }

# # car['year'] = 2003

# # del car['mileage']

# # print(car['color'])

# # print(len(car))

# # vehicle = {
# #     'car': {
# #         'type': 'sedan',
# #         'color': 'blue',
# #         'year': 2003

# #     },
# #     'truck': {
# #         'type': 'pickup',
# #         'color': 'red',
# #         'year': 1998
# #     }
# # }

# # car = [
# #         {'type': 'sedan'},
# #         {'color': 'blue'},
# #         {'year': 2003}
# # ]

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    10,
# }

# # half_numbers = []
# # for num in numbers.values():
# #     half_numbers.append(num // 2)
# # print(half_numbers)

# # half_numbers = [numbers[num] / 2 for num in numbers]
# half_numbers = [num // 2 for num in numbers.values()]
# print(half_numbers)

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    10,
# }

# for k, v in numbers.items():
#     print(f"A {k} number is {v}.")

# import random

# def predict_weather():
#     sunshine = random.choice(['True', 'False'])

#     if sunshine:
#         print("Today's weather will be sunny!")
#     else:
#         print("Today's weather will be cloudy!")

# predict_weather()

# def multiply_by_five(n):
#     return n * 5

# print("Hello! Which number would you like to multiply by 5?")
# number = int(input())

# print(f"The result is {multiply_by_five(number)}!")

# multiply_by_five

# pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# # pets['dog'] = 'bowser'
# pets['dog'].append('bowser')

# print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# def get_quote(person):
#     if person == 'Yoda':
#         return 'Do. Or do not. There is no try.'
#     if person == 'Confucius':
#         return 'I hear and I forget. I see and I remember. I do and I understand.'
#     if person == 'Einstein':
#         return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

# print('Confucius says:')
# print('"' + get_quote('Confucius') + '"')
# print(f'"{get_quote("Confucius")}"')

# numbers = []

# for i in range(5):
#     numbers.append(i)

# print(numbers)

# info = {'name': 'Srdjan', 'age': 38}

# print(info.get('city', 'unknown'))

# sub_list = ["-", "-", "-"]
# matrix = []

# for _ in range(3):
#     matrix.append(sub_list.copy())

# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     max_number = float('-inf')
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     return max_number

# print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
# print(find_maximum([-1, 0, 5, 3]))         # Expected 5
# print(find_maximum([-10, -3, -20, -2]))   # Expected -2

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0