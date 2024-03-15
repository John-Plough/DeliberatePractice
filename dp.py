# dic = {
#     'chocolate': 4,
#     'milk': 3,
#     'eggs': 2
# }

# for item, price in dic.items():
#     print(f"{item} costs ${price}.")

# def invert(in_dict):
#     new_dict = {}
    
#     for k, v in in_dict.items():
#         new_dict[v] = k
        
#     return new_dict

# def invert(in_dict):
#     return {v: k for k, v in dict.items()}

# def count_of_value(my_dict, num):
#     count = 0
    
#     for _, v in my_dict.items():
#         if v == num:
#             count += 1

#     return count


# def count_of_value(dictionary, integer):
#     count = 0
    
#     for key in dictionary:
#         if dictionary[key] == integer:
#             count += 1
            
#     return count

# def sum_of_values(my_dict, list_of_strings):
#     total = 0
    
#     for string in list_of_strings:
#         if string in my_dict:
#             total += my_dict[string]

#     return total

# def sum_of_values(my_dict, list_of_strings):
#     total = 0

#     for k, v in my_dict.items():
#         if k in list_of_strings:
#             total += v

#     return total


# def common_elements(my_dict):
#     common = []
    
#     for value in my_dict.values():
#         if value in my_dict:
#             common.append(value)
    
#     return common

# def common_elements(my_dict):
#     return [val for val in my_dict.values() if val in my_dict]

# def common_elements(my_dict):
#     return [key for key in my_dict if key in my_dict.values()]
