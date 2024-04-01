# def chromosome_check(chromosome):
#     sex = 'son' if 'Y' in chromosome else 'daughter'
#     return f"Congratulations! You're going to have a {sex}." 

# for num in range(1, 100):
#     print(num * 2)

# lst = [1, 3, 7, 15]
# index = 0

# i = 0
# while i < len(lst):
#     print(lst[i])
#     i += 1

# friends = ['Sarah', 'John', 'Hannah', 'Dave']

# for friend in friends:
#     print(f"Hi, {friend}")

# cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
#           'Vienna', None, 'London', 'Beijing', None]

# for city in cities:
#     if not city:
#         continue
#     print(len(city))

# while True:
#     print("and on")
#     break

# fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

# for fish in fish_list:
#     print(fish)
#     if fish == 'Nemo':
#         break

# while True:
#     print('Should I stop looping?')
#     answer = input()
#     if answer == 'Yes':
#         break

# def factorial(n):
#     result = 1

#     while n > 1:
#         result *= n
#         n -= 1

#     return result


# def factorial(n):
#     result = 1

#     for i in range(1, n+1):
#         result *= i

#     return result

# print(factorial(5))

def whatday(num):
    match num:
        case 1:
            return 'Sunday'
        case 2:
            return 'Monday'
        case 3:
            return 'Tuesday'
        case 4:
            return 'Wednesday'
        case 5:
            return 'Thursday'
        case 6:
            return 'Friday'
        case 7:
            return 'Saturday'
        case default:
            "Wrong, please enter a number between 1 and 7"

print(whatday(8))