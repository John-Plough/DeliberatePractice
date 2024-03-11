# def filter_list(l):
#     return [el for el in l if isinstance(el, int)]

# def sale_hotdogs(n):
#     return n * (100 if n < 5 else 95 if n < 10 else 90)
    
    # if n < 5:
    #     return 100
    # elif n < 10:
    #     return 95
    # else:
    #     return 90

# def powers_of_two(n):
#     return [2**num for num in range(0, n + 1)]
        
# def expanded_form(num): # 42
    #make str --> '42'
    #loop backwards 10 % int(str[-1])
    #   100 % int(str[-2])

# def expanded_form(num):
#     stringed = str(num)
#     result = ''

#     for digit in stringed:
#         result += f"{digit} + "
#     print(result[:-3])

# expanded_form(42)

# def expanded_form(num):
#     num = list(str(num))
#     return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

# def expanded_form(num):
#     num = list(str(num)) #num is a list of each digit as a str
#                          # --> ['7', '9', '2', '6']
#     return ' + '.join(x + '0' * (len(num) - 1 - y) for y,x in enumerate(num))


# print(isinstance((expanded_form(7926)), str))

# def expanded_form(num):
#     num = str(num)
#     return ' + '.join(idx + '0' * (len(num) - digit) for digit,idx in enumerate(num, 1) if idx != '0')

# print(expanded_form(5382))

# def expanded_form(num):
#     return ' + '.join(idx + '0' * (len(str(num)) - digit) for digit,idx in enumerate(str(num), 1) if idx != '0')

# print(expanded_form(98754321))

# def solution(string):
#     return string[::-1]

# def square(n):
#     return n**2

# def is_anagram(test, original):
#     test_dict = {}
#     orig_dict = {}
    
#     for char in test.lower():
#         if char in test_dict:
#             test_dict[char] += 1
#         else:
#             test_dict[char] = 1

#     for char in original.lower():
#         if char in orig_dict:
#             orig_dict[char] += 1
#         else:
#             orig_dict[char] = 1
            
#     return test_dict == orig_dict

# def is_anagram(test, original):
#     both = test + original
#     for char in both:
#         if test.lower().count(char) == original.lower().count(char):
#             continue
#         else:
#             return False
#     return True

# def is_anagram(test, original):
#     print(sorted(test.lower()) == sorted(original.lower()))

# is_anagram("foefet", "toffee")
# is_anagram("Buckethead", "DeathCubeK")
# is_anagram("beauty", "eauty")
# is_anagram("eauty", "beauty")
# is_anagram("Shops", "sHops")

# print(sorted('johnnyplough'))

# def fake_bin(x):
#     result = ''
#     for digit in x:  
#         result += '0' if int(digit) < 5 else '1'
#         print(result)
#         return result

# def fake_bin(x):
#     return ''.join('0' if digit < '5' else '1' for digit in x)

# print(fake_bin('3637'))

# li = ['1', '4', '0', '8', '7', '3', '2']
# print(li)
# print(sorted(li))
# print(li)
# print()
# print(li)
# li.sort()
# print(li)

# def wave(people):
#     result = []
#     enum = enumerate([*people]) 
#         # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
#     for idx, letter in enum:

#         result.append(people[:idx] + people[idx].upper() + people[idx+1:])
#     print(result)


# wave('hello')

# change 'hello' to 'heLlo'
# people[:idx] + people[idx].upper() + people[idx+1:]

def wave(people):
    # enum = enumerate([people]) 
        # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
    return [people[:idx] + people[idx].upper() + people[idx+1:] for idx, letter in enumerate(people) if letter != ' ']
    # return [people[:idx] + letter.upper() + people[idx+1:] for idx, letter in enumerate(people) if letter != ' ']
    

# print(wave('i do'))

# def wave(people):
#     return [people[:idx] + people[idx].upper() + people[idx+1:] for idx, letter in enumerate(people) if letter != ' ']

# def wave(str):
#     return [str[:i] + str[i:].capitalize() for i in range(len(str)) if str[i] != ' '] 
#     # return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i]!=" "]
# print(wave('i do too'))

# stuff = {
#     1: 'boat',
#     'two': 'car',
#     (3,'four','5'): 'plane'
# }

# print(1 in stuff)
# print('plane' in stuff)
# print(2 in stuff)
# print('2' in stuff)
# print(3 in stuff)
# print((3, 'four', '5') in stuff)