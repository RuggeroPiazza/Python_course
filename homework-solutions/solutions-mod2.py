"""
- Exercise:
Write a program that takes two numbers, checks which one is the biggest and return a message.
Output should tell the biggest number or if the numbers are equals.
Extra:
Make it dynamic.
Implement exception handling

- Homeworks:
GRADE CALCULATOR
Write a program that is going to give the grade of a student according to the score obtained.
Score >= 90 : ‘A’    80<=score<=89: ‘B’    70<=score<=79 : ‘C’    60<=score<=69: ‘D’    score<59: ‘F’

FIZZ BUZZ
Write a program that, given a number, it will play the fizz buzz game
Hint: check again what the modulo operator does
Hint: check for loops and the range() function

GUESS THE NUMBER
Create a program to ask the user to guess the number that has been randomly generated.
The user will be able to try continuously until it finds the correct number.
The program should stop as soon as the number is found.
At each iteration the program will tell the user if the number is too high, too low or the correct one.
Extra:
Implement a way to assign only 5 attempts to the user. Each iteration should show the attempt left.
Hint: check what the random library does
"""

# exercise solution ############################################################
import random


print("Insert the first number: ")
first_num = int(input('> '))
print("Insert the second number: ")
second_num = int(input('> '))

if first_num == second_num:
    print("Numbers are equal.")
elif first_num > second_num:
    print(str(first_num) + " is the bigger number.")
else:
    print(str(second_num) + " is the bigger number.")

# exercise solution with extra ############################################################

try:
    print("Insert the first number: ")
    first_num = int(input('> '))
    print("Insert the second number: ")
    second_num = int(input('> '))
except ValueError:
    print("Incorrect value")
else:
    if first_num == second_num:
        print("Numbers are equal.")
    elif first_num > second_num:
        print(str(first_num) + " is the bigger number.")
    else:
        print(str(second_num) + " is the bigger number.")

# Homework solutions ############################################################

# GRADE CALCULATOR
user_inp = input("Insert your score to get your grade: ")
try:
    score = int(user_inp)
except ValueError:
    print("A score must be a number from 0 to 100")
else:
    if score < 0 or score > 100:
        print("The score inserted cannot be negative or above 100")
    else:
        if score >= 90:
            print('A')
        elif 80 <= score <= 89:  # or score >= 80 and score <= 89
            print('B')
        elif 70 <= score <= 79:
            print('C')
        elif 60 <= score <= 69:
            print('D')
        else:
            print('F')

# GRADE CALCULATOR WITH LOOP
flag = True
while flag:
    user_inp = input("Insert your score to get your grade: ")
    try:
        score = int(user_inp)
    except ValueError:
        print("A score must be a number from 0 to 100")
    else:
        if score < 0 or score > 100:
            print("The score inserted cannot be negative or above 100")
        else:
            flag = False
if score >= 90:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('F')

# FIZZ BUZZ
user_inp = input("Insert a number: ")
try:
    num = int(user_inp)
except ValueError:
    print("Make sure you are inserting a number")
else:
    for num in range(1, num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizz buzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

# GUESS THE NUMBER
# remember to import random
number = random.randint(1, 100)
guess = -1

while guess != number:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print(f"You got it!! The number is {number}")
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

# GUESS THE NUMBER WITH ATTEMPTS
number = random.randint(1, 100)
guess = ''
attempts = 5

while guess != number and attempts > 0:
    print(f"You have {attempts} attempts")
    guess = int(input("Enter your guess: "))
    if guess == number:
        print(f"You got it!! The number is {number}")
    elif guess > number:
        print("Your guess is too high")
        attempts -= 1
    else:
        print("Your guess is too low")
        attempts -= 1
if attempts == 0:
    print(f"GAME OVER! No more attempts, the number to guess was {number}")

# GUESS THE NUMBER WITH FLAG
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
