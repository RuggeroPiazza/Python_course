"""
Here the solutions for the exercises in module 4. The homework solutions are written in separated files
in the same \homework-solutions folder.
"""

# EXERCISE 1
# Take all the letters of a given string and split each character into a list.
string = 'thisistheteststring'
lst = []
 
for letter in string:
    lst.append(letter)
 
print(f"this is lst after appending: {lst}")

# with list comprehension
splitted_string = [x for x in string]
print(f"this is the splitted string: {splitted_string}")

# ALTERNATIVES
# typecasting
print(f"with typecasting: {list(string)}")

# unpack method
[*string]

# extend method
lst = []
lst.extend(string)
print(f"with extend: {lst}")

# EXERCISE 2
# Given the following list of numbers, remove all occurrences of item 20
list1 = [5, 20, 15, 20, 25, 50, 20]

# with while loop
while 20 in list1:
    list1.remove(20)
print(f"Ex 2, with a while loop: {list1}")

# with for loop
for num in list1:
    if num == 20:
        list1.pop(num)
print(f"Ex 2, with a for loop: {list1}")

# list comprehension
new_list = [num for num in list1 if num != 20]
print(f"Ex 2, with a list comprehesion: {new_list}")

# using sets
my_set = set(list1)
print(f"Ex 2, using properties of sets: {my_set}")

# EXERCISE 3
# Given a dictionary, calculate the sum of all items.

my_dict = {'a': 100, 'b': 200, 'c': 300}
my_list = []
for i in my_dict.values():
    my_list.append(i)

print(f"this is the sum of all the values in the dictionary {sum(my_list)}")
