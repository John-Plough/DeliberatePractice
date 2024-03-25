# # # def unique_in_order(sequence):
# # #     if not sequence:
# # #         return []
    
# # #     result = [sequence[0]]

# # #     for el in sequence:
# # #         if el != result[-1]:
# # #             result.append(el)

# # #     return result


# # # def unique_in_order(sequence):
# # #     res = []
# # #     prev = None

# # #     for el in sequence:
# # #         if el != prev:
# # #             res.append(el)
# # #             prev = el

# # #     return res


# # def tower_builder(n):
# #     tower = []
# #     space = ' '
# #     star = '*'
# #     stars = 1

# #     for i in range(n):
# #         tower.append(((n-1) * space) + (stars * star) + ((n-1) * space))
# #         n -= 1
# #         stars += 2

# #     return tower



# # def tower_builder(n):
# #     tower = []
# #     counter = 1

# #     for _ in range(n):
# #         spaces = ((n-1) * ' ')
# #         stars = (counter * '*')
# #         tower.append(spaces + stars + spaces)
# #         n -= 1
# #         counter += 2

# #     return tower


# # def tower_builder(n):
# #     tower = []

# #     for row in range(1, n+1):
# #         spaces = ' ' * (n-row)
# #         stars = '*' * (2 * row - 1)
# #         tower.append(spaces + stars + spaces)

# #     return tower

# # def tower_builder(n):
# #     tower = []

# #     for floor in range(1, n + 1):
# #         spaces = ' ' * (n - floor)
# #         stars = '*' * (2 * floor - 1)
# #         tower.append(spaces + stars + spaces)

# #     return tower



# # def tower_builder(n):
# #     return [ for floor in range(1, n+1)]


# # print(tower_builder(0))
# # print(tower_builder(1))
# # print(tower_builder(2))
# # print(tower_builder(6))



# # int(bin(5)[2:])

# # int(f'{5:b}')


# def isAnagram(s, t):
#         a = [*s].sort()
#         print(s)
#         b = [*t].sort()
#         print(t)
#         return a == b

# # print(isAnagram('rat', 'car'))


# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
    
#     countS, countT = {}, {}

#     for i in range(len(s)):
#         countS[s[i]] = 1 + countS.get(s[i], 0)
#         countT[t[i]] = 1 + countT.get(t[i], 0)

#     for key in countS:
#         if countS[key] != countT.get(key, 0):
#             return False

#     return True


# def ana(s, t):
#     if len(s) != len(t):
#         return False
    
#     scount, tcount = {}, {}

#     for i in range(len(s)):
#         scount[s[i]] = 1 + scount.get([s[i]], 0)
#         tcount[t[i]] = 1 + tcount.get([t[i]], 0)

#     for key in scount:
#         if scount[key] != tcount.get(key, 0):
#             return False
    
#     return True
        

# print(isAnagram('ratsi', 'ratis'))
    

    
def sort_array(arr):
    odds = []
    
    # find odds and add to odds list
    for i in range(len(arr)): 
        if arr[i] % 2 != 0:
            odds.append(arr[i])
            arr[i] = 1
    
    # sort odds list
    odds.sort()

    # loop thru arr again, adding back in odd nums
    odd_i = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = odds[odd_i]
            odd_i += 1

    return arr


def sort_array(arr):
    odds = sorted((num for num in arr if num % 2 != 0), reverse=True)
    return [num if num % 2 == 0 else odds.pop() for num in arr]
    
    # find odds and add to odds list
    for i in range(len(arr)): 
        if arr[i] % 2 != 0:
            odds.append(arr[i])
            arr[i] = 1
    
    # sort odds list
    odds.sort()

    # loop thru arr again, adding back in odd nums
    odd_i = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = odds[odd_i]
            odd_i += 1

    return arr

# print(sort_array([7, 1]))
# print(sort_array([5, 8, 6, 3, 4, 1, 1, 7]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))



def sort_array(arr):
    odds = sorted((num for num in arr if num % 2 != 0), reverse=True)
    return [num if num % 2 == 0 else odds.pop() for num in arr]


def sort_array(arr):
    odds = []
    
    # loop over input arr, and copy odds to odds list
    for i in range(len(arr)): 
        if arr[i] % 2 != 0:
            odds.append(arr[i])
    
    # sort the odds list
    odds.sort()

    # loop over arr again, adding odds back in
    odds_idx = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = odds[odds_idx]
            odds_idx += 1

    return arr






