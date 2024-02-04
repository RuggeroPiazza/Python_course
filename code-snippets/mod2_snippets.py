"""
Code snippets and examples from Module 2
"""


# if statements
price = 50

if price < 100:
    print("price is less than 100")

if price > 100:
    print("price is greater than 100")

if price == 100:
    print("price is 100")

if price < 100:
    print("price is less than 100")

# if, else statements
# if the condition evaluates to False, the block of code following the else statement gets executed

if price >= 100:
    print("price is greater than 100")
else:
    print("price is less than 100")

# nesting statements

answer = 'hello'

if answer == 'yes':
    print("awesome")
else:
    if answer == 'no':
        print("too bad")
    else:
        print("whatever")

# if-if vs if-elif
# the elif-statement gets evaluated ONLY if the if-statement evaluates to False
# so if-elif is mutually exclusive

raining = True
cold = True

# in the following example there is a mistake:
n = 6
# n = 4
if n % 2 == 0:
    print("divisible by 2")
elif n % 3 == 0:
    print("divisible by 3")
else:
    print("not divisible by two or three")

# given n = 6 the output should be both divisible by 2 and divisible by 3
# to fix that we need to change elif into if
# if we use n = 4, the else statement gets executed
# to fix this we need to change the indentation, as follow:

n = 6
# n = 4, n = 11
if n % 2 == 0:
    print("divisible by 2")
    if n % 3 == 0:
        print("divisible by 3")
else:
    print("not divisible by two or three")


# try, except
# comment out/delete x = 3 to trigger the except block
x = 3
try:
    result = x + 2
except NameError:
    print("uh oh, something went wrong")
else:
    print("all good with our code")
    print(result)
finally:
    print("This will be printed no matter what")

# explanation
# try: block of code that might generate an error

# except: block of code gets executed if the try block return an error

# else: executed if try block is error-free

# finally: executed irrespective of exception occurred or not


# loops


# ex on how to avoid having to write the print command multiple times
# using a while loop
i = 1

while i < 6:
    print("hello")
    i += 1

# while loops
# the program keep asking to insert the name unless you type the string 'your name'
name = ''
while name != 'your name':
    print('Please, type your name: ')
    name = input()
print('Thank you')

# brake
i = 1
while 1 < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# sentinel variable
sentinel = True

while sentinel:
    letter = input("give me a letter")
    if letter == 'x':
        sentinel = False

# for loops
name = 'Charly'
for char in name:
    print(char)

# using break and continue
name = "Charly"
for char in name:
    if char == 'l':
        break
    print(char)

for char in name:
    if char == 'l':
        continue
    print(char)

for number in range(11):
    print(number)

# example of using a loop as a counter
word = "thisisaverylongwordomgiwishtoknowhowmanyletters"
counter = 0
for letter in word:
    counter += 1

print(counter)

# print(len(word))

# nested loop
for i in range(11):
    for j in range(11):
        print(i, j)

for number in range(0, 11, 2):
    print(number)

for i in range(1, 25, 6):
    for j in range(i, i + 6):
        print(j, end="\t")
    print()

size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")

# solution for GUESS NUMBER program using flags
import random

flag = True
to_guess = random.randint(1, 50)
guess = ''

print("Guess a number between 1 and 50")

while flag:
    guess = int(input("Enter your guess: "))
    if guess == to_guess:
        print("Well done!!")
        flag = False
    elif guess > to_guess:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

# other solution without using a flag
import random

to_guess = random.randint(1, 50)
guess = ''

print("Guess a number between 1 and 50")

while guess != to_guess:
    guess = int(input("Enter your guess: "))
    if guess == to_guess:
        print("Well done!!")
    elif guess > to_guess:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

# solution including attempts
import random

to_guess = random.randint(1, 50)
print(to_guess)
guess = ''
attempt = 5
print("Guess a number between 1 and 50")

while attempt > 0:
    guess = int(input("Enter your guess: "))
    if guess == to_guess:
        print("Well done, you won!!")
        attempt = 0
    elif guess > to_guess:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    if attempt != 0:
        attempt -= 1
        print("You have " + str(attempt) + " attempt left")

print("Game Over")


# password checker
password = "superpassword1234"

pw_inserted = input("Please insert the password: ")
if pw_inserted != password:
    print("access denied")
else:
    print("access granted")

# password checker solution with loop
password = "superpassword1234"

pw_inserted = ''

while pw_inserted != password:
    user_imp = input("Please insert the password: ")
    pw_inserted = user_imp
    if pw_inserted == password:
        print("access granted")
    else:
        print("access deniend")