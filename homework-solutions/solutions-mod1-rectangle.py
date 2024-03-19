"""
This is the solution for the homeworks assigned in Mod 1.
In this assignment, you had to write a program that calculates the area and the perimeter
of a rectangle.
"""

# define the sides
a = 10
b = 14

# calculate perimeter and area
perimeter = a + b
area = (a * b) / 2

print("The perimeter of the given rectangle is: ")
print(perimeter)
print("The area of the given rectangle is: ")
print(area)

# solution using the input() ###########################################################
# asking the user to insert the sides value
a = int(input("Please insert the first side of a rectangle: "))
b = int(input("Please insert the second side of a rectangle: "))

# calculating perimeter and area
perimeter = a + b
area = (a * b) / 2

print("The perimeter of the given rectangle is: ")
print(perimeter)
print("The area of the given rectangle is: ")
print(area)
