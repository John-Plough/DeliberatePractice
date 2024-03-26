# # # def is_anagram(str1, str2):
# # #     return sorted(str1.lower()) == sorted(str2.lower())


# # # def is_anagram(str1, str2):
# # #     if len(str1) != len(str2):
# # #         return False
    
# # #     str1 = str1.lower()
# # #     str2 = str2.lower()
# # #     str1_count, str2_count = {}, {}
    
# # #     for i in range(len(str1)):
# # #         str1_count[str1[i]] = 1 + str1_count.get(str1[i], 0)
# # #         str2_count[str2[i]] = 1 + str2_count.get(str2[i], 0)

# # #     for char in str1:
# # #         if str1_count[char] != str2_count.get(char, 0):
# # #             return False
        
# # #     return True

# # # # def remove_exclamation_marks(s):
# # # #     s.replace('!', '')

# # # # def remove_exclamation_marks(s):
# # # #     return ''.join(char for char in s if char != '!')

# # # # def remove_exclamation_marks(s):
# # # #     return s.replace('!', '')

# # # def remove_exclamation_marks(s):
# # #     return ''.join(char for char in s if char != '!')

# # # def remove_exclamation_marks(s):
# # #     return s.replace('!', '')


# # # def find_average(numbers):
# # #     return sum(numbers) / len(numbers)

# # # def find_average(numbers):
# # #     print(numbers)
# # #     return sum(numbers)/len(numbers)

# # # print(find_average([]))

# # def title_case(title, minor=''):
# #     title.title()
# #     arr = minor.lower().split(' ')
# #     for word in arr:
# #         if word in title.lower():
# #             title.replace(word, word.lower())

# #     return title


# # def title_case(title, minor=''):
# #     low_title = title.lower()
# #     low_minor = minor.lower()

# #     arr = low_minor.split(' ')
    
# #     for word in arr:
# #         if word not in low_title:
# #             low_title.replace(word, word.title())

# #     return title

# # def title_case(title, minor=''):
# #     title = title.lower().split()
# #     minor = minor.lower().split()

# #     for i in range(len(title)):
# #         if i == 0 or title[i] not in minor:
# #             title[i] = title[i].title()
    
# #     return ' '.join(title)

# # # print(title_case('THE WIND IN THE WILLOWS', 'The In'))

# # # [a clash of KINGS]    [a an the of]



# # def title_case(title, minor=''):

# #     title = title.lower().split()   # all words are lowercased and in list
# #     minor = minor.lower().split()   

# #     for i in range(len(title)): # loop over title words
# #         if i == 0 or title[i] not in minor: # if not first word or a minor word: capitalize
# #             title[i] = title[i].title()
    
# #     return ' '.join(title)  # return as string



# # def title_case(title, minor_words=''):
# #     title = title.capitalize().split()
# #     minor_words = minor_words.lower().split()
# #     return ' '.join([word if word in minor_words else word.capitalize() for word in title])

# # # print(title_case('THE WIND IN THE WILLOWS', 'the In'))
# # print(title_case('a clash of KINGS', 'a an the of'))

# # ' '.join(word if word in minor_words else word.capitalize() for word in title)
# # ' '.join([word if word in minor_words else word.capitalize() for word in title])


# def groupAnagrams(strs):
#     all_count = []

#     for word in strs:
#         all_count.append({})
#         j = 0
#         print(f"new word: {word}. j = {j}")

#         for i in range(len(word)):
#             all_count[j][word[i]] = 1 + all_count[j].get(word[i], 0)
#             print(all_count)

#         j += 1
    
#     return all_count

# def groupAnagrams(strs):
#     all_count = []
#     word_idx = 0

#     for word in strs:
#         all_count.append({})
#         for i in range(len(word)):
#             all_count[word_idx][word[i]] = 1 + all_count[word_idx].get(word[i], 0)

#         word_idx += 1
    
#     for i in range(len(all_count)):
#         for j in range(len(all_count[i])):
#             if all_count[i] != dicti

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#     [
    # {'e': 1, 'a': 1, 't': 1}, 
    # {'t': 1, 'e': 1, 'a': 1}, 
    # {'t': 1, 'a': 1, 'n': 1}, 
    # {'a': 1, 't': 1, 'e': 1}, 
    # {'n': 1, 'a': 1, 't': 1}, 
    # {'b': 1, 'a': 1, 't': 1}
    # ]

def to_dictionary(detects):
    result = {}

    for i, detect in enumerate(detects):
        result[detect] = i

    return result

# def to_dictionary(detects):
#     return{detect: i for i, detect in enumerate(detects)}

# print(to_dictionary(["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]))

def length_counts(countries):
    result = {}

    for country in countries:
        result[len(country)] = 1 + result.get(len(country), 0)

    return result

# def length_counts(countries):
#     return {len(country): countries.count(country) for country in set(countries)}
    
print(length_counts(["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]))