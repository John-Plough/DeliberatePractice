# # def duplicate_count(text):
# #     text = text.lower()
# #     counter = {}
# #     total = 0

# #     for char in text:
# #         if char in counter and counter[char] == 1:
# #             total += 1
# #         counter[char] = counter.get(char, 0) + 1

# #     return total



# def duplicate_count(text):
#     text = text.lower()
#     counter = {}
#     total = 0

#     for char in text:
#         counter[char] = counter.get(char, 0) + 1
#         if counter[char] == 2:
#             total += 1

#     return total


# # def duplicate_count(text): 
# #     text = text.lower()
# #     total = 

# #     for char in set(text):
# #         if text.count(char) > 1:
# #             total += 1

# #     return total

# # def duplicate_count(text): 
# #     return len([char for char in set(text.lower()) if text.lower().count(char) > 1])

# print(duplicate_count("Indivisibilities"))

# # def duplicate_count(s):
# #   return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     elif len(names) > 3:
#         return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

# def goose_filter(birds):
#     return [bird for bird in birds if bird not in geese]

# def solve(s):
#     upper = 0
#     lower = 0

#     for char in s:
#         if char.isupper():
#             upper += 1
#         else:
#             lower += 1

#     return s.lower() if lower >= upper else s.upper()


# def sort_my_string(s):
#     evens = []
#     odds = []
    
#     for i, char in enumerate(s):
#         if i % 2 == 0:
#             evens.append(char)
#         else:
#             odds.append(char)
            
#     return f"{''.join(evens)} {''.join(odds)}"








# def sort_my_string(s):
#     return f"{s[::2]} {s[1::2]}"


# def sort_my_string(s):
#     evens = ''
#     odds = ''
    
#     for i in range(len(s)):
#         if i % 2 == 0:
#             evens += s[i]
#         else:
#             odds += s[i]
            
#     return f"{evens} {odds}"


# def sort_my_string(s):
#     evens = []
#     odds = []
    
#     for i in range(len(s)):
#         if i % 2 == 0:
#             evens.append(s[i])
#         else:
#             odds.append(s[i])
            
#     return f"{''.join(evens)} {''.join(odds)}"


def pushDominoes(dominoes):
    result = ''
    pairs = [(-1, 'L')]                 # pre-populate with a left boundary

    for i, direction in enumerate(dominoes):
        if direction == 'R' or direction == 'L':
            pairs.append((i, direction))
    pairs.append((len(dominoes), 'R'))    # populate with a right boundary

    for i in range(len(pairs) - 1):     # iterate to compare directions in neighbor tuples      5
        a = pairs[i][1]
        b = pairs[i+1][1]
        ai = pairs[i][0]
        bi = pairs[i+1][0]

        if a == 'L' and b == 'L':        
            result += 'L' * (bi - ai)

        elif a == 'L' and b == 'R':
            result += '.' * (bi - ai - 1) + 'R'

        elif a == 'R' and b == 'R':
            result += 'R' * (bi - ai)

        elif a == 'R' and b == 'L':
            if (bi - ai) % 2 == 0:      # '.' in middle
                result += 'R' * ((bi - ai) // 2 - 1) + '.' + 'L' * ((bi - ai) // 2)
            else:                       # no '.' in middle
                result += 'R' * ((bi - ai) // 2) + 'L' * ((bi - ai) // 2 + 1)

    return result[:-1]

#   .L.R...LR..L..    [(-1, 'L'), (1, 'L'), (3, 'R'), (7, 'L'), (8, 'R'), (11, 'L'), (14, 'R')]
#   LL.RR.LLRRLL..
# print(pushDominoes('.L.R...LR..L..'))
#   012345678
#   .LL.R..R.L.
#   LLL.RRRR.L.
# print(pushDominoes(".L.R...LR...L.."))
#                  "LL.RR.LLRRLL.."
#                  "LL.RR.LLRL.."
# R..L -> R(RLL)
# 0123 -> 1R, 2L

#   L       012345678
        #   ..L..R.RL

#   L       012345678
        #   ..R..L.RL

#   L       012345678
        #   ..R..LRL  --> add 1/2 - 1 Rs, add 1/2 Ls
#             R-.-L


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = ''
        pairs = [(-1, 'L')]                     # pre-populate with a left boundary

        for i, direction in enumerate(dominoes):
            if direction == 'R' or direction == 'L':
                pairs.append((i, direction))
        pairs.append((len(dominoes), 'R'))      # populate with a right boundary

        for i in range(len(pairs) - 1):         # loop & compare directions in neighbor tuples
            a, b, ai, bi = pairs[i][1], pairs[i+1][1], pairs[i][0], pairs[i+1][0]

            if a == 'L' and b == 'L':        
                result += 'L' * (bi - ai)

            elif a == 'L' and b == 'R':
                result += '.' * (bi - ai - 1) + 'R'

            elif a == 'R' and b == 'R':
                result += 'R' * (bi - ai)

            elif a == 'R' and b == 'L':
                if (bi - ai) % 2 == 0:          # even diff (needs '.' in middle)
                    result += 'R' * ((bi - ai) // 2 - 1) + '.' + 'L' * ((bi - ai) // 2)
                else:                           # odd diff
                    result += 'R' * ((bi - ai) // 2) + 'L' * ((bi - ai) // 2 + 1)

        return result[:-1]                      # remove fake right boundary
    



    class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = ''
        pairs = [(-1, 'L')]                     # pre-populate with a left boundary

        for i, direction in enumerate(dominoes):
            if direction == 'R' or direction == 'L':
                pairs.append((i, direction))
        pairs.append((len(dominoes), 'R'))      # populate with a right boundary

        for i in range(len(pairs) - 1):         # loop & compare directions in neighbor tuples
            a, b, ai, bi = pairs[i][1], pairs[i+1][1], pairs[i][0], pairs[i+1][0]

            if a == 'L' and b == 'L':        
                result += 'L' * (bi - ai)

            elif a == 'L' and b == 'R':
                result += '.' * (bi - ai - 1) + 'R'

            elif a == 'R' and b == 'R':
                result += 'R' * (bi - ai)

            elif a == 'R' and b == 'L':
                if (bi - ai) % 2 == 0:          # even diff (needs '.' in middle)
                    result += 'R' * ((bi - ai) // 2 - 1) + '.' + 'L' * ((bi - ai) // 2)
                else:                           # odd diff
                    result += 'R' * ((bi - ai) // 2) + 'L' * ((bi - ai) // 2 + 1)

        return result[:-1]                      # remove fake right boundary