numbers = [1,2,3,4,5,6,7,8,9]
numbers

# [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_numbers = []
for n in numbers:
    new_numbers.append(n * 2)
print(new_numbers)

# [2, 4, 6, 8, 10, 12, 14, 16, 18]

# Alternate for above
new_numbers = [n * 1 for n in numbers]
print(new_numbers)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(2):
    for j in range(5):
        print(i + j, end = " ")

# 0 1 2 3 4 1 2 3 4 5 

# Alternate above
computed_num = [i+j for i in range(2) for j in range(5)]
computed_num

# [0, 1, 2, 3, 4, 1, 2, 3, 4, 5]

type(computed_num)

# list

# multi dimension
new_computed_multi = [ [i+j for i in range(2)] for j in range(5) ]
print(new_computed_multi)

# [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]

# The following code cell will execute a nested loop that will deliver all possible combinations of the elements from the products_on_sale, sale_prices and quantities lists:

# for chair_type in products_on_sale:
#     for price in sale_prices:
#         for quantity in quantities:
#             print ([chair_type, price*quantity])
# Use a list comprehension to obtain the same output. Store it in a variable called sales_revenue.



# If your solution is correct, the contents of the sales_revenue variable will appear in the User Logs.

products_on_sale = ['Chair_Type_1', 'Chair_Type_2', 'Chair_Type_3', 'Chair_Type_4']
sale_prices = [100, 120, 135, 150]
quantities = [1000, 1500, 1300]
sales_revenue = []

for chair_type in products_on_sale:
    for price in sale_prices:
        for quantity in quantities:
            sales_revenue.append([chair_type, price*quantity])

sales_revenue

# Use a list comprehension to return a list with all even numbers between 1 and 10 inclusive, multiplied by 10.

# Please remember to use the print() function to print out the desired output.

# pythonic way
print([ n * 10 for n in range(1,11) if n % 2 == 0 ])

# non pythonic way
even = []
for n in range(1,11):
    if n % 2 == 0:
        even.append(n * 10)
print(even)

# Using list comprehension, return a list that contains the element from range(1, 11) multiplied by 10 if the number is even, and "None" if that number is odd.

# Please use num as an iteration variable name in the required list comprehension.

# pythonic way
print([ num * 10 if num % 2 == 0 else 'None' for num in range(1,11) ])