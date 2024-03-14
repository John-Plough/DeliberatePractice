# def duplicate_count(text):

#     counter = {}

#     for char in text:
#         char = char.lower()
#         if char in counter:
#             counter[char] += 1
#         else:
#             counter[char] = 1

#     occurences = counter.values()
#     total = 0

#     for num in occurences:
#         if num > 1:
#             total += 1

#     return total

# def duplicate_count(s):
#   return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# def duplicate_count(s):
#     set(s.lower())

# print(duplicate_count("Indivisibilities"))

# if s.lower().count(char) > 1


# def duplicate_count(s):
#     return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
#     return len([c for c in set(s.lower()) if s.lower().count(c)>1])
#     return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# def duplicate_count(s):
#   return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# def duplicate_count(s):
#     return len([c for c in set(s.lower()) if s.lower().count(c) > 1])




# def duplicate_count(input_str):
#     s = input_str.lower()
#     return len([char for char in set(s) if s.count(char) > 1])

# def duplicate_count(input_str):
#     s = input_str.lower()
#     seen = set()
#     duplicates = set()

#     for char in s:
#         if char in seen:
#             duplicates.add(char)
#         seen.add(char)

#     return len(duplicates)

# def duplicate_count(input_str):
#     s = input_str.lower()
#     total = 0

#     for char in set(s):
#         if s.count(char) > 1:
#             total += 1

#     return total    

# print(duplicate_count("Indivisibilities"))

# def rain_amount(mm):
#     if mm < 40:
#         return f"You need to give your plant {40 - mm} mm of water"
#     else:
#         return "Your plant has had more than enough water for today!"
    
# print(rain_amount(35))

# def length_counts(list):

#     lengths = {}
    
#     for el in list:
#         if len(el) in lengths:
#             lengths[len(el)] += 1
#         else:
#             lengths[len(el)] = 1
            
#     return lengths


# def length_counts(list):

#     result = {}

#     for el in list:
#         length = len(el)
#         curr = result.get(length, 0)
#         result[length] = curr + 1
    
#     return result

# def length_counts(elements):
#     counts = {}

#     for el in elements:
#         curr = counts.get(len(el), 0)
#         counts[len(el)] = curr + 1

#     return counts

def delete_keys(dict, list):
    for str in list:
        if str in dict:
            del dict[str]
    
    return dict