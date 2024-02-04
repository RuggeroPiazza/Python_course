"""
Code snippets and examples for Module 3
"""

# Escape characters

s = 'Hey, what\'s up?'
print(s)

print("Multiline strings\ncan be created\nusing escape sequences.")

print("This is on one line")
print("This is too close")

print('''Dear Alice,

Eve’s cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

print("C:\\Users\\Pat\\Desktop")


# string concatenation

name = "John"
last_name = "Smith"
print(name + last_name)

print("Hi, my name is " + name + ' ' + last_name)


# f-strings and string.format()

name = "Bob"
age = 30

print("Hello, my name is {} and I’m {} years old".format(name, age))

print(f"Hello, my name is {name} and I’m {age} years old")



# indexing and slicing

test = "hello world"
print(test[6])
print(test[0:6])
print(test[2:4])

# starting from the end of the string
print(test[-5])
print(test[-2])
print(test[-5:-2])

# no values
print(test[:])
print(test[:5])

# stepping
print(test[::2])
nums = '0123456789'
print(nums[::2])
print(nums[::3])


# string.split() method
cheers = "This is module 3 in the Python course"
print(cheers.split())

cheers = "This-is-module-3-in-the-Python-course"
print(cheers.split())
print(cheers.split('-'))

cheers = "This is module 3 , in the Python course"
print(cheers.split())
print(cheers.split(','))


# ' '.join() method
countries = ['Italy', 'UK', 'India', 'France', 'Spain', 'Portugal']
print('-'.join(countries))

# example of useful case:
# combining tuples
t = ('quarter-final', 'semi-final', 'final')
print(",".join(t))


# exercise
user_inp = input("please insert a word: ").lower()
if user_inp[::-1] == user_inp:
    print(f"The world {user_inp} is a palindrome.")
else:
    print(f"The world {user_inp} is not a palindrome.")

# variation on palindrome program:
user_inp = input("please insert a word: ").lower()
#new_str = [i for i in reversed(user_inp)] # makes an iterator to loop through
new_str = ''
for char in reversed(user_inp):
    new_str += char
if ''.join(new_str) == user_inp:
    print("palindrome")
else:
    print("not a palindrome")


# split a string and display all the sub-strings
str1 = "Emma-is-a-data-scientist"
print(f"Original String is: {str1}")

# split string
sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)


# eliminates all the extra spaces from a text
paragraph = "Argentina  wins   football   world cup 2022 in a nail biting final match that led to a \
spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most\
 memorable   matches."

split_paragraph = paragraph.split()
print(' '.join(split_paragraph))


# generator example

def my_generator(n):
    # initialize counter
    value = 0
    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value
        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
# for value in my_generator(3):
#     # print each value produced by generator
#     print(value)


x = my_generator(3)
print(next(x))
print(next(x))
print(next(x))

