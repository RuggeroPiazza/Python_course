"""
EXERCISES
- Palindrome:
Write a program that checks if a word is a palindrome.
Split a string on hyphens:

- Write a program to split a given string on hyphens and display each substring
Input:
    Str1 = “Emma-is-a-data-scientist”

Output must have each sub-string on a new line

- Remove extra spaces between words:
Given the following sentence, find a way to remove all the extra spaces
and print the same sentence with just one space between words.

paragraph = "Argentina  wins   football   world cup 2022 in a nail   biting final match that led to a
spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most
  memorable   matches."

HOMEWORKS:
- COUNTER
Count letters, digit and special symbols:
Write a program that count all letters, digits and special symbols from a given string:
Input:
    “P@#yn26at^&i5ve”
Output:
    Chars = 8
    Digits = 3
    Symbol = 4
- NAME IN A SENTENCE
Check if a name is in a sentence:
Write a script that, given a sentence and a word it will tell if the word is included in the sentence and how
many time appears in the sentence.
EXTRA: make it dynamic

- Print a staircase:
Write a script that given an integer, print a staircase made of number as shown below:
1
22
333
4444
55555
666666
hint: can you nest for loops?
"""

# PALINDROME
user_inp = input("Insert a word: ").lower()
if user_inp[::-1] == user_inp:
    print("The word is a palindrome")
else:
    print("The word is a not a palindrome")

# SPLIT A GIVEN STRING
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)

# COUNTER
user_imp = "P@#yn26at^&i5ve"
char_count = 0
digit = 0
symbols = 0

for char in user_imp:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit += 1
    else:
        symbols += 1

print(f"The string has {char_count} characters, {digit} digits and {symbols} symbols")

# NAME IN A SENTENCE
inp = input("Please insert a sentence: ")
inp2 = input("Please insert the word to search: ")

words = inp.split()
if inp2 in words:
    print(f"The word {inp2} is included in the sentence")
else:
    print(f"The word {inp2} is not included in the sentence")

# PYRAMID
# the outer loop tells the number of rows, inner loop tells the number of columns
n = 7
for num in range(1, n + 1):
    for n in range(num):
        print(num, end=" ")

    print(" ")
