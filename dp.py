# # # def solution(n):
# #     # build ordered container for pairs, starting with largest
    
# #     # create empty output str
    
# #     # loop over container
# #         # if n > val
# #             # divide n by val
# #             # add that many symbols to output str
# #             # decrement n

# #     # return output str

# # # def solution(n):
    
# # #     pairs = [
# # #         ('M', 1000),
# # #         ('CM', 900),
# # #         ('D', 500),
# # #         ('CD', 400),
# # #         ('C', 100),
# # #         ('XC', 90),
# # #         ('L', 50),
# # #         ('XL', 40),
# # #         ('X', 10),
# # #         ('IX', 9),
# # #         ('V', 5),
# # #         ('IV', 4),
# # #         ('I', 1),
# # #     ]

# # #     roman_numeral = ''

# # #     for pair in pairs:
# # #         symbol = pair[0]
# # #         value = pair[1]
# # #         print(f"n: {n}, val: {value}, {n > value}")
# # #         if n >= value:
# # #             print(f"romannum: {roman_numeral}")
# # #             roman_numeral += (n // value) * symbol
# # #             print(f"        romannum: {roman_numeral}")
# # #             n -= (n // value) * value

    
# # #     return roman_numeral





# # # for num, rep in table:
# # #         if x >= num:
# # #             return rep + solution(x-num)
# # #     return str()


# # def solution(x):
# #     table = [
# #         (1000,"M"),
# #         (900,"CM"),
# #         (500,"D"),
# #         (400,"CD"),
# #         (100,"C"),
# #         (90,"XC"),
# #         (50,"L"),
# #         (40,"XL"),
# #         (10,"X"),
# #         (9,"IX"),
# #         (5,"V"),
# #         (4,"IV"),
# #         (1,"I")
# #     ]

# #     roman_numeral = ''

# #     for num, rep in table:
# #         if x >= num:
# #             roman_numeral += (x // num) * rep
# #             x -= (x // num) * num
    
# #     return roman_numeral

# # print(solution(14))


# def is_square(n):  

# # determine if sq root of n is an int



# def is_square(n): 
#     return n >= 0 and (n ** 0.5) % 1 == 0

# # return False if n < 0 else pow(n, 0.5) % 1 == 0


# def number(bus_stops):
    # input - list of pairs [[10,0],[3,5],[5,8]]
    # first is people that get on
    # second is people that get off
    # output people still on bus after last pair

    # create total
    #loop over bus_stops
        # add first to total
        # subtract second to total
    #return total

#     total = 0

#     for stop in bus_stops:
#         total += stop[0]
#         total -= stop[1]

#     return total

# def number(bus_stops):

#     total = 0

#     for stop in bus_stops:
#         total += stop[0]
#         total -= stop[1]

#     return total

# print(number([[10,0],[3,5],[5,8]]))



# def number(bus_stops):
#     return sum(get_on - get_off for get_on, get_off in bus_stops)

# # def number(bus_stops):
# #     return sum(stop[0] - stop[1] for stop in bus_stops)

# # def number(bus_stops):

# #     total = 0

# #     for stop in bus_stops:
# #         total += stop[0]
# #         total -= stop[1]

# #     return total

# print(number([[10,0],[3,5],[5,8]]))


def moveZeroes(nums):
    i = 0
    
    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1

    while i < len(nums):
        nums[i] = 0
        i += 1

    return nums

# print(moveZeroes([0,1,0,3,12]))
#     # ---> [1,3,12,0,0]

def moveZeroes1(nums):
    i = 0

    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1

    while i < len(nums):
        nums[i] = 0
        i += 1

    return nums

# print(moveZeroes([0,1,0,3,12]))
    # ---> [1,3,12,0,0]

def moveZeroes2(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums
                    # [1,3,12,0,0] 
# print(moveZeroes([0,1,0,3,12]))
    # ---> [1,3,12,0,0]

def moveZeroes2(nums):
    left_index = 0

    for right_index in range(len(nums)):
        a = nums[left_index]
        b = nums[right_index]

        if b:  #if element is not a zero...
            a, b = b, a
            left_index += 1

    return nums
                    # [1,3,12,0,0] 
print(moveZeroes([0,1,0,3,12]))