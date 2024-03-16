# def divisors(n): 
#     total = 0
    
#     for num in range(1, n + 1):
#         if n % num == 0:
#             total += 1

#     return total

# def divisors(n): 
#     sum(1 for num in range(1, n+1) if n % num == 0)

# def divisors(n): 
#     total = 0

#     for num in range(1, n/2 + 1):
#         if n % num == 0:
#             total += 1
    
#     return total + 1

# def duty_free(price, discount, holiday_cost):
#     return int(holiday_cost / (price * (.01 * discount)))

# def duty_free(price, discount, holiday_cost):
#     savings = price * discount / 100
#     return holiday_cost // savings

# def duty_free(price, discount, holiday_cost):
#     return holiday_cost // (price * discount / 100)

# def duty_free(price, discount, holiday_cost):
#     if discount == 0:
#         return 
#     return holiday_cost // (price * discount / 100)

# def flatten_and_sort(array):
#     flat = []
#     for row in array:
#         for num in row:
#             flat.append(num)

#     flat.sort()
#     return flat

# def flatten_and_sort(array):
#     flat = []
#     for row in array:
#         flat.extend(row)
#     return sorted(flat)

# print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))


# def check_exam(arr1,arr2):
#     score = 0

#     for idx, answer in enumerate(arr1):
#         if arr2[idx]:
#             if arr1[idx] == arr2[idx]:
#                 score += 4
#             elif arr1[idx] != arr2[idx]:
#                 score -= 1

#     return score if score >= 0 else 0

# def check_exam(arr1,arr2):
#     score = 0

#     for idx in range(0, len(arr1)):
#         if arr2[idx]:
#             if arr1[idx] == arr2[idx]:
#                 score += 4
#             else:
#                 score -= 1

#     return score if score >= 0 else 0


# def check_exam(arr1, arr2):
#     return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))

# def check_exam(arr1, arr2):
#     score = sum(4 if first == second else -1 for first, second in zip(arr1, arr2) if second)
#     return score if score >= 0 else 0

# def check_exam(arr1, arr2):
#     # one liner
#     return max(0, sum(4 if first == second else -1 for first, second in zip(arr1, arr2) if second))

# def check_exam(arr1, arr2):
#     #readable
#     score = 0

#     for teacher, student in zip(arr1, arr2):
#         if student:
#             if teacher == student:
#                 score += 4
#             else:
#                 score -= 1

#     return score if score >= 0 else 0



# def check_exam(arr1,arr2):
#     score = 0

#     for idx in range(0, len(arr1)):
#         if arr2[idx]:
#             if arr1[idx] == arr2[idx]:
#                 score += 4
#             else:
#                 score -= 1

#     return score if score >= 0 else 0

# print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))



# def gimme(input_array):
    # return input_array.index(sorted(input_array)[1])



# def delete_nth(my_list, limit):
#     result = []
#     count = {}

#     for idx, num in enumerate(my_list):
#         if num in count:
#             count[num] += 1
#             if count[num] <= limit:
#                 result.append(num)
#         else:
#             count[num] = 1
#             result.append(num)    

#     return result

# {20: 2, 37: 1}
# [20, 37]
# [20,37,20,21], 1 ---> [20,37,21]

# def delete_nth(my_list, limit):
#     result = []
#     count = {}

#     for num in my_list:
#         if num in count:
#             count[num] += 1
#             if count[num] <= limit:
#                 result.append(num)
#         else:
#             count[num] = 1
#             result.append(num)    

#     return result


# def delete_nth(my_list, limit):
#     counter = {}
#     result = []

#     for item in my_list:
#         occurences = counter.get(item, 0)
#         if occurences < limit:
#             result.append(item)
#             counter[item] = occurences + 1

#     return result

# def delete_nth(my_list, limit):
#     result = []

#     for num in my_list:
#         if result.count(num) < limit: result.append(num)

#     return result

# print(delete_nth([20,37,20,21], 1))


def find_multiples(integer, limit):     # 5, 25
    multiples = []
    
    n = 1
    multiple = integer * n

    while multiple <= limit:
        multiples.append(multiple)
        n += 1

    return multiples

def find_multiples(integer, limit):
    
    result = []
    i = 1
    while integer * i <= limit:
        result.append(integer * i)
        i += 1

    return result

def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))