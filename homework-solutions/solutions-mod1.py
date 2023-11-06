"""
This is the solution for the homeworks assigned in Mod 1.
In this assignment, you had to write a program that calculates the area and the perimeter
of a triangle. Ignore having to check if the sides are form a valid triangle.
"""

import math

# this program calculates the perimeter and area of a valid triangle
a = 15
b = 14
c = 13

perimeter = a + b + c
sp = perimeter / 2
# calculate A with Heron's formula A = sqrt(sp - (sp - a)(sp - b)(sp - c))
area = math.sqrt(sp*((sp - a)*(sp - b)*(sp - c)))

print("The perimeter of the given triangle is: ")
print(perimeter)
print("The area of the given triangle is: ")
print(area)

# solution using the input() ###########################################################
# this program calculates the perimeter and area of a valid triangle
a = int(input("Please insert the first side of a triangle: "))
b = int(input("Please insert the second side of a triangle: "))
c = int(input("Please insert the third side of a triangle: "))

# calculating perimeter and semi-perimeter
perimeter = a + b + c
sp = perimeter / 2

# calculate A with Heron's formula A = sqrt(sp - (sp - a)(sp - b)(sp - c))
area = math.sqrt(sp*((sp - a)*(sp - b)*(sp - c)))

print("The perimeter of the given triangle is: ")
print(perimeter)
print("The area of the given triangle is: ")
print(area)
