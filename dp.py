# def longest_consec(list_of_strings, integer):
#     long = 0
#     start = 0
#     longest_string = ''

#     for my_str in list_of_strings:
#         length = 0
#         this_string = ''

#         # print('---loop of strings---')
#         # print(start + integer)
#         if start + integer > len(list_of_strings):
#             # integer = len(list_of_strings) - start
#             # print(f"END -- The longest string: {longest_string}")
#             return longest_string

#         for idx in range(start, start + integer):
#             length += len(list_of_strings[idx])
#             this_string += list_of_strings[idx]
#             # print(f"this_string:  {this_string}")
#             # print(f"length: {length}")
#             # print(f"long: {long}")
#         if length > long:
#             long = length
#             longest_string = this_string
#             # print(f"***updated long: {long}")
#         start += 1
#         # print(f"  Current longest string: {longest_string}")

#     # return long_string
#                                         #3
# longest_consec(["tr", "fol", "tras", "bluey", "abcdef", "uvwxyza"], 3)
# # longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2) 



# def longest_consec(list_of_strings, integer):
#     long = 0
#     start = 0
#     longest_string = ''

#     for my_str in list_of_strings:
#         length = 0
#         this_string = ''

#         if start + integer > len(list_of_strings):
#             return longest_string

#         for idx in range(start, start + integer):
#             length += len(list_of_strings[idx])
#             this_string += list_of_strings[idx]
#         if length > long:
#             long = length
#             longest_string = this_string
#         start += 1


# # longest_consec(["tr", "fol", "tras", "bluey", "abcdef", "uvwxyza"], 3)

# # strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

# # def longest_consec(list_of_strings, integer):  
# #     long = 0
# #     lengths = []
# #     for str in list_of_strings:
# #         lengths.append(len(str))
# #     print(lengths)

# #     for num in lengths:
# #         start = 0
# #         for idx in range(start, integer):
# #                 long += lengths[idx]
# #                 start += 1
# #                 # integer -= 1
# #                 print(long)

# #     print(long)


def spacey(array):
    result = []
    my_string = ''
    
    for word in array:
        my_string += word   
        result.append(my_string)    
        print(result)
    
    return result

def spacey(array):
    my_string = ''
    return [my_string := my_string + word for word in array]

def spacey(array):
    strr = ''
    out = []
    for el in array:
        strr += el
        out.append(strr)
    return out

from itertools import accumulate

def spacey(a):
    return list(accumulate(a))

def spacey(array):
    return [''.join(array[:i+1]) for i in range(len(array))]

def spacey(array):
    return [''.join(array[:1+i]) for i in range(len(array))]

print(spacey(['i', 'have','no','space']))