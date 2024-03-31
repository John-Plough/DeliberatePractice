# # def solution(s):
# #     return ''.join(' ' + char if char.isupper() else char for char in s)

# # def solution(s):
# #     result = ''

# #     for char in s:
# #         if char.isupper():
# #             result += ' '
# #         result += char
    
# #     return result


# # def solution(s):
# #     return ''.join(f" {char}" if char == char.upper() else char for char in [*s])

# # def solution(s):
# #     s = [*s]
# #     result = []

# #     for char in s:
# #         if char == char.upper():
# #             result.append(f" {char}")
# #         else:
# #             result.append(char)14

# #     return ''.join(result)





# def multiplication_table(size):
#     return [[i*j for j in range(1, size+1)] for i in range(1, size+1)]


# def multiplication_table(size):
#     result = []
    
#     for i in range(1, size+1):
#         row = []
#         for j in range(1, size+1):
#             row.append(i*j)
#         result.append(row)

#     return result


# def multiplication_table(size):
#     result = [[] * size for i in range(size)]
    
#     for i in range(size):
#         for j in range(size):
#             result[i].append((i+1) * (j+1))

#     return result

# print(multiplication_table(4))


toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")

pizza_and_prices = []
for i in range(len(toppings)):
  pizza_and_prices.append([prices[i], toppings[i]])

print(pizza_and_prices)