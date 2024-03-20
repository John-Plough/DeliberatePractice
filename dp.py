# # # def pipe_fix(nums):
# # #     return [num for num in range(min(nums), max(nums) + 1)]
    
# # # def pipe_fix(nums):
# # #     return list(range(min(nums), max(nums) + 1))

# # # def pipe_fix(nums):
# # #     return list(range(min(nums), max(nums) + 1))

# # # def pipe_fix(nums):
# # #     return list(range(nums[0], nums[-1] + 1))
# # #     return list(range(nums[0], nums[-1] + 1))

# # # print(pipe_fix([1,3,5,6,7,8]))

# # # def switch_it_up(number):
# # #     if number == 0:
# # #         return 'Zero'
# # #     elif number == 1:
# # #         return 'One'
# # #     elif number == 2:
# # #         return 'Two'
# # #     elif number == 3:
# # #         return 'Three'
# # #     elif number == 4:
# # #         return 'Four'
# # #     elif number == 5:
# # #         return 'Five'
# # #     elif number == 6:
# # #         return 'Six'
# # #     elif number == 7:
# # #         return 'Seven'
# # #     elif number == 8:
# # #         return 'Eight'
# # #     else:
# # #         return 'Nine'
    
# # #     if number == 9:


# # # def reverse_words(text):
# #     #split text into words array    ['This', 'is', 'an', 'example']
# #     #loop over words array
# #         # add reversed word to array
# #         # join els on ' '
    
# # def reverse_words(text):
# #     return ' '.join([word[::-1] for word in text.split(' ')])

# # # def reverse_words(text):
# # #     return ' '.join(i[::-1] for i in text.split(' '))

# # print(type(reverse_words('double  spaced  words')))

# # # "This is an example!" ==> "sihT si na !elpmaxe"

# # 'elbuod decaps sdrow'
# # 'elbuod  decaps  sdrow'


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for num in nums:
#             if nums.count(num) > 1:
#                 return True
#         return False
    
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         my_dict = {}
        
#         for num in nums:
#             if num in my_dict:
#                 return True
#             my_dict[num] = True

#         return False
    
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) != len(nums)
    
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums_set = set()
        
#         for num in nums:
#             if num in nums_set:
#                 return True
#             nums_set.add(num)

#         return False


# class Solution:
# def mergeAlternately(self, word1: str, word2: str) -> str:
#     merged_str = ''
#     long = []
#     short = []

#     if len(word1) > len(word2):
#         long = word1
#         short = word2
#     else:
#         long = word2
#         short = word1

#     for idx in range(0, len(short)):
#         merged_str += word1[idx]
#         merged_str += word2[idx]
#         print(merged_str)

#     merged_str += long[len(short):]

#     return merged_str
        
# 
        
        
#         # loop for enum of word1
#         # add char1, add char2
    
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         merged_str = ''
#         if len(word1) > len(word2):

#             for idx in range(0, len(word2)):
#                 merged_str += word1[idx]
#                 merged_str += word2[idx]

#             merged_str += word1[len(word2):]

#         else:

#             for idx in range(0, len(word1)):
#                 merged_str += word1[idx]
#                 merged_str += word2[idx]

#             merged_str += word2[len(word1):]

#         return merged_str
    
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ''
        long = []
        short = []

        if len(word1) > len(word2):
            long = word1
            short = word2
        else:
            long = word2
            short = word1

        for idx in range(0, len(short)):
            merged_str += word1[idx]
            merged_str += word2[idx]

        merged_str += long[len(short):]

        return merged_str
    

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_list = []

        for i in range(min(len(word1), len(word2))):
            merge_list.append(word1[i])
            merge_list.append(word2[i])

        if len(word1) > len(word2):
            merge_list.append(word1[len(word2):])
        else:
            merge_list.append(word2[len(word1):])
        
        return ''.join(merge_list)



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_str = ''

        for i in range(min(len(word1), len(word2))):
            merge_str += word1[i] + word2[i]
        
        return merge_str + word1[i+1:] + word2[i+1:]
    

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_list = []

        for i in range(min(len(word1), len(word2))):
            merge_list.append(word1[i])
            merge_list.append(word2[i])
        
        return ''.join(merge_list) + word1[i+1:] + word2[i+1:]
    


def mergeAlternately(word1, word2):
    merge_list = []

    for i in range(min(len(word1), len(word2))):
        merge_list.append(word1[i])
        merge_list.append(word2[i])
        
    return ''.join(merge_list) + word1[i+1:] + word2[i+1:]

print(mergeAlternately('abcd', 'pq'))