"""
Examples and code snippets for Mod 4
"""

# ex of immutable data type
test = 'hello'
letter = test[2]
test[2] = 'p' # the string can't be changed

my_tuple = (2, 3)
x = my_tuple[1]
sliced = my_tuple[0:1]
my_tuple[1] = 5  # the tuple can't be changed

# ex of mutable object
my_list = [0, 1, 2, 3]
my_list[0] = 29

# ex of unordered data type
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(set(letters))

# lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(set(list_of_lists))

# creating lists
empty_list = [] # by simply using square brackets
new_list = [1, 2, 3.5, True, ['bread', 'milk', 'butter']] # by simply creating the list
name = 'Ruggero'
my_tuple = ('hello', 'Ruggero', 'Bob')
print(list(my_tuple)) # by using the list() function to convert one data structure into a list

# accessing data inside a list
my_list = [1, 2, 3.5, True, ['bread', 'milk', 'butter']]

print(my_list[0])
print(my_list[3])
print(my_list[4])
print(my_list[4][0])

# list methods
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.index('banana')
fruits.reverse()  # notice that there is no returns

# example
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
for items in fruits:
    print(items)

fruits.reverse()
print('*****************')
for items in fruits:
    print(items)

fruits.append('grape')
fruits.pop()  # it returns the item
fruits.sort()

# list comprehension
# [expression for item in iterable if condition]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
empty_lst = []

for num in lst:
    if num < 6:
        empty_lst.append(num * 2)

print(empty_lst)

compr_list = [num * 2 for num in lst if num < 6]
print(compr_list)

# dictionaries
# creation:
sups = (('Batman', 'Bruce Wayne'),
        ('Superman', 'Clark kent'),
        ('Spiderman', 'Peter Parker'))

print(dict(sups))

sups_list = [('Batman', 'Bruce Wayne'),
             ('Superman', 'Clark kent'),
             ('Spiderman', 'Peter Parker')]

# create a dictionary from a sequence of key pairs values
print(dict([('eggs', 2), ('bacon', 1), ('milk', 3)]))

# accessing data in a dictionary
sups = {'Batman': 'Bruce Wayne', 'Superman': 'Clark kent', 'Spiderman': 'Peter Parker'}
print(sups['Batman'])
print('Batman' in sups)
print(sorted(sups))

sups['Batman'] = 'Rug'

# getting keys, values and items
# it returns view objects (memory efficient and faster because it doesn't create a list), can be turned into lists
print(sups.keys())
print(sups.values())
print(sups.items())

# changing key
ini_dict = {'player1': 1, 'player2': 5, 'player3': 10, 'player4': 15}
print("initial dictionary", ini_dict)
ini_dict['player3'] = ini_dict.pop('player4')
print("final dictionary", str(ini_dict))

# dict comprehension
# making a new dict
my_list = ['a', 'b', 'c', 'e']
new_dict = {}
for letter in my_list:
    new_dict[letter] = letter.upper()

new_dict = {x: x.upper() for x in my_list}
print(new_dict)

# mapping two lists
keys = ['a', 'b', 'c', 'e']
values = [1, 2, 3, 4]

new_dict = {k: v for (k, v) in zip(keys, values)}
print(new_dict)

# looping through dictionaries
for names in sups:
    print(names)

for k, v in sups.items():
    print(k, v)

for v in sups.values():
    print(v)

# tuples
# creation:
l = [1, 2, 3, 4]
print(type(l))
t = tuple(l)
print(type(t))

t = (12345, 54321, 'hello!')
x, y, z = t  # unpacking

print(t[0])
t[0] = 88888  # trying assign a new value

v = ([1, 2, 3], [3, 2, 1])

# if you want to change tuple values:
tup_to_list = list(t)
tup_to_list[1] = "new_value"
back_to_tuple = tuple(tup_to_list)

print(back_to_tuple)

# sets
# creation:
# First way: using the set() function on an iterable object
set1 = set([1, 1, 1, 2, 2, 3])  # from a list
set2 = set(('a', 'a', 'b', 'b', 'c'))  # from a tuple
set3 = set('anaconda')  # from a string

# Second way: using curly braces
set4 = {1, 1, 'anaconda', 'anaconda', 8.6, (1, 2, 3), None}

print('Set1:', set1)
print('Set2:', set2)
print('Set3:', set3)
print('Set4:', set4)

# Incorrect way: trying to create a set with mutable items (a list and a set)
set5 = {1, 1, 'anaconda', 'anaconda', 8.6, [1, 2, 3], {1, 2, 3}}
print('Set5:', set5)


# creating an empty set (can't use the curly brackets only)
empty1 = {}  # this creates a dictionary instead
empty2 = set()

print(type(empty1))
print(type(empty2))

# accessing values in a set
# because unordered and not indexed, can't access values by indexing or slicing
my_set = {'a', 'b', 'c', 'd'}
print(my_set[0])

for item in my_set:
    print(item)

# set methods
# Initial set
my_set = set()

# Adding a single immutable item
my_set.add('a')
print(my_set)

# Adding several items
my_set.update({'b', 'c'})  # a set of immutable items
print(my_set)
my_set.update(['d', 'd', 'd'])  # a simple list gets converted into a set and remove duplicates if present
print(my_set)
my_set.update(['e'], ['f'])  # several lists of immutable items
print(my_set)
my_set.update('fgh')  # a string
print(my_set)
my_set.update([[1, 2], [3, 4]])  # an attempt to add a list of mutable items (lists)
print(my_set)

# union, intersection, difference, symmetric difference
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

# union
# returns a new set of all the unique items for both sets
print(a | b)
print(b | a)
print(a.union(b))
print(b.union(a))

# intersection
# returns a new set of the items common to both sets
print(a & b)
print(b & a)
print(a.intersection(b))
print(b.intersection(a))

# difference
# returns a new set containing all the items from the first set that are absent in the second set
# (in the case of more than two sets, the operation is performed from left to right)

print(a - b)
print(b - a)
print(a.difference(b))
print(b.difference(a))

# symmetric difference
# returns a set that contains all items from both set, but not the items that are present in both sets.
print(a ^ b)
print(b ^ a)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# exercise
# ex 1
string = 'thisistheteststring'
lst = []

for letter in string:
    lst.append(letter)

print(lst)

# with list comprehension
splitted_string = [x for x in string]
print(splitted_string)

# Alternatives:
# Typecasting:
print(list(string))

# Unpack method:
print([*string])

# Extend method:
lst = []
lst.extend(string)
print(lst)

# Ex 2:
# With for loop:
list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = []

for num in list1:
    if num != 20:
        list2.append(num)

print(list2)

# With list comprehension:
list1 = [5, 20, 15, 20, 25, 50, 20]

list2 = [num for num in list1 if num != 20]

print(list2)

# With while loop:
list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)

print(list1)

# ex 3
# sol 1
my_dict = {'a': 100, 'b': 200, 'c': 300}
my_list = []
for i in my_dict:
    my_list.append(my_dict[i])

print(sum(my_list))

# sol 2
total = 0

for i in my_dict.values():
    total += i

print(total)







