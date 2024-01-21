# 02-conditionals3.md

# Write a program that stores a customer's age and a movie's time in two separate variables. Then calculate the price of a movie ticket based on the following conditions:

# If the age is 12 years old or younger, the ticket price is $5.
# If the age is between 13 and 59 years old and the movie is before 6 PM, the ticket price is $7. After 6 PM, the ticket price is $10.
# If the customer is 60 years old or older, the ticket price is $7.

age = 62
time = 6

if age <= 12:
    price = 5
elif age <= 59:
    if time < 6:
        price = 7
    else:
        price = 10
else:
    price = 7

print(price)

# Write a program to store the type of book (regular, reference, or special collection) and the number of days its overdue. Then calculate the fine amount based on the following conditions:

# If the book is a regular book and overdue by up to 7 days, the fine is $1 per day.
# If the book is a regular book and overdue by more than 7 days, the fine is $2 per day.
# If the book is a reference book, there is no fine, regardless of the number of days overdue.
# If the book is a special collection book, the fine is $5 per day, regardless of the number of days overdue.

kind = 'googly'
days = 8

if kind == 'regular':
    if days <= 7:
        fine = days
    else:
        fine = 2 * days
elif kind == 'reference':
    fine = 0
else:
    fine = 5 * days
    
print(fine)

# Write a program that stores a person's order value and membership level (regular or premium). Then calculate a discount amount based on the following conditions:

# If the total order value is less than $50, there is no discount.
# If the total order value is between $50 and $100, the discount is 5% for regular customers and 10% for premium customers.
# If the total order value is greater than $100, the discount is 10% for regular customers and 15% for premium customers.

value = 200
level = 'premium'

if value < 50:
    discount = 0
elif value <= 100:
    if level == 'regular':
        discount = .05 * value
    else:
        discount = .10 * value
else:
    if level == 'regular':
        discount = .10 * value
    else:
        discount = .15 * value

print(discount)

# Write a Ruby program that stores the weight of a package and the destination (domestic or international). Then calculate the shipping fee based on the following conditions:

# If the destination is domestic:
# If the weight is less than or equal to 1 kg, the shipping fee is $5.
# If the weight is greater than 1 kg, the shipping fee is $10.
# If the destination is an international shipment:
# If the weight is less than or equal to 1 kg, the shipping fee is $15.
# If the weight is greater than 1 kg, the shipping fee is $25.

weight = 1.4
destination = 'domestic'

if destination == 'international':
    if weight <= 1:
        fee = 5
    else:
        fee = 10
else:
    if weight <= 1:
        fee = 15
    else:
        fee = 25

print(fee)