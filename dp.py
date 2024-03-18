# #func that takes list of ints and a target num
# #find two different items in list that added together give target num
# #return indices of those two items in a tuple

# # def two_sum(numbers, target):
# #     #loop thru list
# #         #loop thru list again
# #             #compare el and outer loop el added with target
# #     pass
    
# # def two_sum(numbers, target):
# #     #loop thru list
# #         #if target - num in list
# #             # index of target - num, and num
# #     pass

# # def two_sum(numbers, target):
# #     if target % 2 != 0:
# #         for num in numbers:
# #             if target - num in numbers:
# #                 return (numbers.index(target - num), numbers.index(num))
# #     else:
# #         if target / 2 in numbers and numbers.lindex(target / 2) != numbers.rindex(target / 2):
# #             return (numbers.lindex(target / 2), numbers.rindex(target / 2))
# #         else: 



# # def two_sum(numbers, target):
# #     if target / 2 in numbers and numbers.index(target / 2) != numbers[::-1].index(target / 2):
# #         return (numbers.index(target / 2), numbers[::-1].index(target / 2))
# #     else:
# #         for num in numbers:
# #             if target - num in numbers:
# #                 return (numbers.index(target - num), numbers.index(num))
            


# # def two_sum(numbers, target):
# #     half = target / 2

# #     #even target
# #     if half in numbers and numbers.index(half) != numbers[::-1].index(half):
# #         return (numbers.index(half), numbers[::-1].index(half))
# #     else:
# #         for num in numbers:
# #             if target - num in numbers:
# #                 return (numbers.index(target - num), numbers.index(num))


# def two_sum(numbers, target):
    
#     #odd
#     if target % 2 != 0:
#         for num in numbers:
#             if target - num in numbers:
#                 return (numbers.index(target - num), numbers.index(num))
    
#     #even    
#     else:
#         # two occurences of half target (ex. [1,2,2], 4)
#         half = target / 2
#         if half in numbers and numbers.count(half) > 1:
#             first = numbers.index(half)
#             print(first)
#             second = numbers[first + 1:].index(half) + 1 + first
#             print(second)
#             print(first, second)
#             return (first, second)
#         # two different nums
#         else:
#             for num in numbers:
#                 if target - num in numbers:
#                     return (numbers.index(target - num), numbers.index(num))
            
# # print(two_sum([2,2,3], 4))

# #     '1 3 82 44'

# #     [1 ,2, 3]             4          ((0,2), (2,0))
# #     [1234,5678,9012]      14690      ((1,2), (2,1))
# #     [2, 2,] 3]             4          ((0,1), (1,0))



# # [1,1,8], 
# # [1,1,8], 
# # [1,2,8]

# # ex = [1,2,4,6,8,9], 8
# # ex = [1,2,4,4,9], 8
# # ex = [1,2,3,6,9], 9
# # ex = [1,2,4,5,6], 9
# # print(two_sum([1, 2, 3], 4)) # returns (0, 2) or (2, 0)
# # print(two_sum([3, 2, 4], 6)) # returns (1, 2) or (2, 1))
                

# def two_sum(numbers, target):

#     for num in numbers:
#             if target - num in numbers and numbers.index(target - num) != numbers.index(num):
#                 return (numbers.index(target - num), numbers.index(num))
#             else:
#                 first = numbers.index(target / 2)
#                 second = numbers[first + 1:].index(half) + first + 1
#                 return first, second
    
#     #even    
#     else:
#         # two occurences of half target (ex. [1,2,2], 4)
#         half = target / 2
#         if half in numbers and numbers.count(half) > 1:
#             first = numbers.index(half)
#             print(first)
#             second = numbers[first + 1:].index(half) + 1 + first
#             print(second)
#             print(first, second)
#             return (first, second)
#         # two different nums
#         else:
#             for num in numbers:
#                 if target - num in numbers:
#                     return (numbers.index(target - num), numbers.index(num))
            
# # print(two_sum([2,2,3], 4))
                

# def two_sum(numbers, target):

#     for num in numbers:
#         if target - num in numbers and numbers.index(target - num) != numbers.index(num):
#             return numbers.index(num), numbers.index(target - num)

#     first = numbers.index(target / 2)
#     second = numbers[first + 1:].index(target / 2) + first + 1
#     return first, second
                            



# def two_sum(numbers, target):
#     other = target - num
#     for num in numbers:
#         if other in numbers and numbers.index(other) != numbers.index(num):
#             return numbers.index(num), numbers.index(other)

#     first = numbers.index(target / 2)
#     second = numbers[first + 1:].index(target / 2) + first + 1
#     return first, second


# def two_sum(numbers, target):
    
#     for num1 in numbers:
#         num2 = target - num1
#         if num2 in numbers and num1 != num2:
#             return numbers.index(num1), numbers.index(num2)

#     # both addends are same value 
#     half = target / 2
#     slice_index = num1 + 1
#     num1 = numbers.index(half)
#     num2 = numbers[slice_index:].index(half) + slice_index
#     return num1, num2

# print(two_sum([1234,5678,9012], 14690))

# def two_sum(numbers, target):

#     # addends are different values
#     for num1 in numbers:
#         num2 = target - num1
#         if num2 in numbers and numbers.index(num1) != numbers.index(num2):
#             return numbers.index(num1), numbers.index(num2)

#     # addends are same value
#     num1 = numbers.index(target / 2)
#     num2 = numbers[num1 + 1:].index(target / 2) + num1 + 1
#     return num1, num2


def two_sum(numbers, target):
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers[i+1:], i+1):
            if num1 + num2 == target:
                return i,j


def two_sum(numbers, target):
    other = {}

    for idx, num in enumerate(numbers):
        if target - num in other:
            return other[target - num], idx
        
        other[num] = idx

print(two_sum([1234,5678,9012], 14690))

arr = [1,3,6,15]
