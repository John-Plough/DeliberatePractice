# def diamond(n):
    
#     if n % 2 == 0 or n < 1: #even or negative
#         return None
    
#     diamonds = ''
#     spaces = int((n-1) / 2)

#     for i in range(1, n+1, 2): #odd numbers from 1 up to n:
#         diamonds += spaces * ' ' + i * '*' + '\n'
#         spaces -= 1

#     spaces += 2
#     for j in range(n-2, 0, -2): #odd numbers from (n-2) down to 1:
#         diamonds += spaces * ' ' + j * '*' + '\n'
#         spaces += 1

#     return diamonds

# print(diamond(0))

# (int((n-1)/2) * '')


# "  *\n ***\n*****\n ***\n  *\n"





# print(diamond(5))



    # diamonds = ''
    # spaces = int((n-1) / 2)

    # for i in range(1, n+1, 2): #odd numbers from 1 up to n:
    #     diamonds += spaces * ' ' + i * '*' + '\n'
    #     spaces -= 1

    # spaces += 2
    # for j in range(n-2, 0, -2): #odd numbers from (n-2) down to 1:
    #     diamonds += spaces * ' ' + j * '*' + '\n'
    #     spaces += 1

    # return diamonds

def diamond(n):
    if n % 2 == 0 or n < 1:    #even or negative input
        return None
    
    the_diamond = (n * '*') + ('\n')    #middle row of diamond
    row_spaces = 1
    row_diamonds = n - 2
    
    while row_diamonds > 0:
        new_row = (row_spaces * ' ') + (row_diamonds * '*') + ('\n') 
        the_diamond = new_row + the_diamond + new_row    # add row above and below
        row_spaces += 1
        row_diamonds -= 2

    return the_diamond

# print(diamond(45))


# def name_shuffler(str_):
#     answer = ' '.join(str_.split(' ')[::-1])
#     print(str_)
#     return answer

def name_shuffler(str_):
    return ' '.join(reversed(str_.split()))


print(name_shuffler('John Plough'))