# def is_pangram(s):
#     # loop over string
#     # if alpha,
#         # check if in dict --> increment or create
#     # check length of dict == 26

#     count = {}

#     for char in s:
#         char = char.lower()
#         if char.isalpha():
#             if char in count:
#                 count[char] += 1
#             else:
#                 count[char] = 1
    
#     print(count)
#     print(len(count))

#     return len(count) == 26

# # is_pangram("The quick brown fox jumps over the lazy dog")

# def is_pangram(s):

#     counter = {}

#     for char in s:
#         char = char.lower()
#         if char.isalpha():
#             counter[char] = counter[char] + 1 if char in counter else 1

#     return len(counter) == 26


# def is_pangram(s):

#     s = s.lower()

#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         if char not in s:
#             return False
#     return True

# import string

# def is_pangram(s):

#     s = s.lower()

#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         if char not in s:
#             return False
#     return True


# def is_pangram(s):
#     return set(string.ascii_lowercase).issubset(s.lower())

# print(is_pangram("The quick brown fox jumps over the lazy dog"))

# def DNA_strand(dna):
#     comp = ''
#     for char in dna:
#         if char == 'A':
#             comp += 'T'
#         elif char == 'T':
#             comp += 'A'
#         elif char == 'C':
#             comp += 'G'
#         elif char == 'G':
#             comp += 'C'
    
#     return comp

# def DNA_strand(dna):

#     table = {
#         'A': 'T',
#         'T': 'A',
#         'C': 'G',
#         'G': 'C'
#     }

#     print(list(table[key] for key in dna))
#     return '-'.join(table[key] for key in dna)

# def DNA_strand(dna):
#     return dna.translate(str.maketrans("ATCG","TAGC"))

# def DNA_strand(dna):
#     return dna.translate(str.maketrans('ATCG', 'TAGC', 'XYZ'))

# print(DNA_strand('XATAYGTAZ'))

def merge_arrays(arr1, arr2):
    print(sorted(set(arr1 + arr2)))

merge_arrays([3,4], [1,2,3])
