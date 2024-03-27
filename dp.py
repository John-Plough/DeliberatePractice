# # # def persistence(num): # 999
# # #     # if num < 10:
# # #     #     return 0
    
# # #     iter = str(num)    # '999'
# # #     result = 0

# # #     while len(iter) > 1:
# # #         product = 1
# # #         for digit in iter:
# # #             product *= int(digit) # 729
# # #         iter = str(product)
# # #         result += 1
    
# # #     return result

# # def diamond(n):
# #     if n < 1 or n % 2 == 0:
# #         return None
    
# #     ring = ''
# #     spaces = n // 2
# #     diamonds = 1

# #     for i in range(n//2 + 1):
# #         ring += (spaces * ' ') + (diamonds * '*') + '\n'
# #         spaces -= 1
# #         diamonds += 2

# #     spaces += 2
# #     diamonds -= 4

# #     for j in range(n//2):
# #         ring += (spaces * ' ') + (diamonds * '*') + '\n'
# #         spaces += 1
# #         diamonds -= 2

# #     return ring


# # def diamond(n):
# #     if n < 1 or n % 2 == 0:
# #         return None
    
# #     spaces = 0
# #     diamonds = n
# #     ring = (n * '*') + '\n'

# #     while diamonds > 1:
# #         spaces += 1
# #         diamonds -= 2
# #         row = (spaces * ' ') + (diamonds * '*') + '\n'
# #         ring = row + ring + row

# #     return ring


# # def diamond(n):
# #     if n % 2 == 0 or n < 1:         #even or negative input
# #         return None
    
# #     ring = (n * '*') + ('\n')       # create middle row of diamond
# #     spaces = 1
# #     diamonds = n - 2
    
# #     while diamonds > 0:
# #         row = (spaces * ' ') + (diamonds * '*') + ('\n') 
# #         ring = row + ring + row     # add row above and below
# #         spaces += 1
# #         diamonds -= 2

# #     return ring



# # # print(diamond(1))
# # print(diamond(11))
# # # "  *\n ***\n*****\n'

# # def sum_of_minimums(numbers):
# #     total = 0
# #     for list in numbers:
# #         total += min(list)

# #     return total

# #     return sum(min(row) for row in numbers)


# # def add_length(str_):
# #     arr = str_.split()

# #     for i in range(len(arr)):
# #         arr[i] = arr[i] + ' ' + str(len(arr[i]))

# #     return arr


# def add_length(str_):
#     arr = str_.split()
#     return [f"{arr[i]} {str(len(arr[i]))}" for i in range(len(arr))]



#     arr = str_.split()
#     return [f"{arr[i]} {str(len(arr[i]))}" for i in range(len(arr))]
    

# # def add_length(str_):
# #     return [f"{str_.split()[i]} {str(len(str_.split()[i]))}" for i in range(len(str_.split()))]

# def add_length(str_):
#     return [f"{word} {len(word)}" for word in str_.split()]

# # "apple ban" --> ["apple 5", "ban 3"]
# print(add_length('apple ban'))


def sum_dig_pow(a, b):
    result = []

    for i in range(a, b+1):

        num_of_digits = len(str(i))
        # print(num_of_digits)
        total = 0
        j = 1

        for digit in str(i):    # '8'
            # print(str(i), digit)
            # print(f"j: {j}")
            total += int(digit) ** j
            print(f"total: {total}")
            j += 1

        if total == i:
            # print(f"i: {i}, Total: {total}")
            result.append(i)

        # print(total)    

    return result

print(sum_dig_pow(88, 141))
# 89, 135

def sum_dig_pow(a, b):
    result = []

    for i in range(a, b+1):
        total = 0
        j = 1

        for digit in str(i):    
            total += int(digit) ** j
            j += 1

        if total == i:
            result.append(i)

    return result

# print(sum_dig_pow(5, 141))



def sum_dig_pow(a, b):
    result = []

    for num in range(a, b+1):
        total = 0
        exponent = 1

        for digit in str(num):    
            total += int(digit) ** exponent
            exponent += 1

        if num == total:
            result.append(num)

    return result


def sum_dig_pow(a, b):
    return [num for num in range(a, b+1) if sum(int(d) ** i for i, d in enumerate(str(num), 1)) == num]

                            #   (1, '1'), (2, '3'), (3, '5') for 135    1+9+125


def sum_dig_pow(a, b):
    return [num for num in range(a, b+1) if sum(int(digit) ** idx for idx, digit in enumerate(str(num), 1)) == num]

def sum_dig_pow(a, b):
    result = []

    for num in range(a, b+1):
        total = 0

        for idx, digit in enumerate(str(num), 1):
            total += int(digit) ** idx

        if total == num:
            result.append(num)

    return result

# one-liner:
# def sum_dig_pow(a, b):
#     return [num for num in range(a, b+1) if sum(int(digit) ** idx for idx, digit in enumerate(str(num), 1)) == num]

print(sum_dig_pow(5, 145))
    


