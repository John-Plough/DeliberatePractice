# def alphabet_position(text):
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     mapped = {letter: idx + 1 for idx, letter in enumerate(alpha)}
#     result = ''

#     for char in text.lower():
#         if char in mapped:
#             result += str(mapped[char]) + ' '

#     return result.strip()


# def alphabet_position(text):

#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# # print(alphabet_position("The sunset sets at twelve o' clock."))



# def alphabet_position(text):

#     result = ''

#     for char in text.lower():
#         if char.isalpha():
#             result += str(ord(char) - 96) + ' '
    
#     return result.strip()

# # print(alphabet_position("The sunset sets at twelve o' clock."))

# def alphabet_position(text):
#     print(str(ord(char) - ord('a') + 1) for char in text.lower() if char.isalpha())
#     return ' '.join(str(ord(char) - ord('a') + 1) for char in text.lower() if char.isalpha())

# print(alphabet_position("The sunset sets at twelve o' clock."))

# # return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())

# # return ' '.join(str(ord(c)-ord('a')+1) for c in s.lower() if c.isalpha())

def calculate_age(year_of_birth, current_year):
    
    if year_of_birth < current_year:
        if current_year - year_of_birth == 1:
            return "You are 1 year old."
        else:
            return f"You are {current_year - year_of_birth} years old."
    elif year_of_birth > current_year:
        if year_of_birth - current_year == 1:
            return "You will be born in 1 year."
        else:
            return f"You will be born in {year_of_birth - current_year} years."
    else:
        return "You were born this very year!"
    
def calculate_age(year_of_birth, current_year):
    diff = year_of_birth - current_year

    if diff > 1:
        return f"You will be born in {diff} years."
    elif diff == 1:
        return "You will be born in 1 year."
    elif diff == 0:
        return 'You were born this very year!'
    elif diff == -1:
        return "You are 1 year old."
    else:
        return f"You are {abs(diff)} years old."

def calculate_age(year_of_birth, current_year):
    diff = abs(year_of_birth - current_year)
    plural = '' if diff == 1 else 's'

    if year_of_birth > current_year:
        return f"You will be born in {diff} year{plural}."
    elif year_of_birth < current_year:
        return f"You are {diff} year{plural} old."
    else:
        return 'You were born this very year!'
    
