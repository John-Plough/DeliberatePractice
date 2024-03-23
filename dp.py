# # def unique_in_order(seq):
# #     if not seq:
# #         return []
    
# #     result = [seq[0]]

# #     for el in seq:
# #         if el != result[-1]:
# #             result.append(el)

# #     return result

# # def unique_in_order(iterable):
# #     result = []
# #     prev = None
# #     for char in iterable:
# #         if char != prev:
# #             result.append(char)
# #             prev = char
# #     return result

# # def unique_in_order(seq):
# #     result = []

# #     for el in seq:
# #         if not len(result) or el != result[-1]:
# #             result.append(el)

# #     return result

# # print(unique_in_order('A'))
# # print(unique_in_order([[1],[2],[3]]))

# # def check_exam(arr1, arr2):
# #     score = 0

# #     for i in range(len(arr1)):
# #         if arr1[i] == arr2[i]:
# #             score += 4
# #         elif arr1[i] != arr2[i] and arr2[i] != '':
# #             score -= 1

# #     return score if score > 0 else 0
        

# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]

# def sum_two_smallest_numbers(numbers):
#     ordered = sorted(numbers)
#     return ordered[0] + ordered[1]

# def sum_two_smallest_numbers(numbers):
#     lowest = float('inf')
#     low = float('inf')

#     for num in numbers:
#         if num < lowest:
#             low = lowest
#             lowest = num
#         elif num < low:
#             low = num
#         print(f"lowest: {lowest}, low: {low}")
#     return lowest + low

# def sum_two_smallest_numbers(numbers):
#     numbers1 = numbers[::]
#     a = min(numbers1)
#     numbers1.remove(a)
#     b = min(numbers1)
#     return a + b

# # print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
# # print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
# print(sum_two_smallest_numbers([25, 12, 10, 8, 18, 22]))


# def solution(text, ending):
#     return text.endswith(ending)



# def rot13(message):
#     encrypted_message = ''

#     for char in message:
#         int_rep = ord(char)
#         offset = int_rep + 13
#         encrypted_char = chr(offset)

#         if 65 <= int_rep <= 90: #uppercase 
#             if offset > 90:
#                 offset -= 26
#             encrypted_message += encrypted_char

#         elif 97 <= int_rep <= 122: #lowercase
#             if offset > 122:
#                 offset -= 26
#             encrypted_message += encrypted_char

#         else:
#             encrypted_message += char

#     return encrypted_message

# print(rot13('John'))

# # def rot13b(message):
    
# #     encryption = ''

# #     for char in message:
# #         if (ord(char) > 64 and ord(char) < 91) or (ord(char) > 96 and ord(char) < 123):
# #             cipher = ord(char) + 13
# #             if (ord(char) < 91 and cipher > 90) or (ord(char) > 96 and cipher > 122):
# #                 cipher -=26
# #             encryption += chr(cipher)
# #         else:
# #             encryption += char

# #     return encryption


def findMaxAverage(nums, k):
    
    largest_avg = float('-inf')

    for i in range(len(nums) - (k-1)):
        total = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
        avg = total / k
        if avg > largest_avg:
            largest_avg = avg 
    return largest_avg

# print(findMaxAverage([1,12,-5,-6,50,3], 4))
# [1,12,-5,-6,50,3], k = 4
#  0  1  2  3  4 5

def findMaxAverage(nums, k):
    
    max_avg = float('-inf')

    for i in range(len(nums) - (k-1)):
        total = sum(nums[i:i+k])
        avg = total / k
        if avg > max_avg:
            max_avg = avg
    
    return max_avg

# print(findMaxAverage([1,12,-5,-6,50,3], 4))
# print(findMaxAverage([5], 1))


def findMaxAverage(nums, k):
    
    curr_sum = max_sum = sum(nums[:4])

    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)

    return max_sum / k

# print(findMaxAverage([1,12,-5,-6,50,3], 4))
# print(findMaxAverage([5], 1))


# def findMaxAverage(nums, k):
    
#     max_avg = float('-inf')
#     curr_sum = sum(nums[:k])

#     for i in range(len(nums) - k + 1):
#         curr_sum += nums[k + i - 1] 
#         curr_sum -= nums[i - 1]
#         avg = curr_sum / k
#         if avg > max_avg:
#             max_avg = avg
    
#     return max_avg

# print(findMaxAverage([1,12,-5,-6,50,3], 4))

def findMaxAverage(nums, k):
    
    max_avg = float('-inf')
    window_sum = 0

    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= k - 1:
            max_avg = max(max_avg, window_sum / k)
            window_sum -= nums[i - k + 1]
    return max_avg

print(findMaxAverage([1,12,-5,-6,50,3], 4))
print(findMaxAverage([5], 1))




