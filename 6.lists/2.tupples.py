Cars = ("BMW", "Dodge", "Ford")


# Remember tuples cant be override like lists ex:- a = [1,2,3] and a[0] = 0 but like this you cant update in liosts
Cars[1]


name, age = 'Peter,24'.split(",")
print(name)
print(age)

# Create a function called rectangle_info() that takes the length and width of a rectangle as arguments. The function should then return the area and the perimeter of the rectangle. Call the function with arguments 2 and 10 to verify it worked correctly.
def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Call the function with 2 and 10
result = rectangle_info(2, 10)

print("Area:", result[0])
print("Perimeter:", result[1])


