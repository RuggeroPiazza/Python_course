import random


def run(choice):
    options = 'rock', 'paper', 'scissors'
    p1_winning = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]

    game = (choice, random.choice(options))
    print(f"game played: {game}")
    if game in p1_winning:
        return 'p1 wins the game'
    elif game[0] == game[1]:
        return "It's a draw"
    else:
        return 'COM wins the game'


def validate_input():
    choices = {'p':'paper', 'r':'rock', 's':'scissors'}
    while True:
        print("r: for rock\np: for paper\ns: for scissors\n")
        user_input = input("> ").lower()
        if user_input in choices.keys():
            return choices[user_input]
        else:
            print("Invalid input.")


if __name__ == "__main__":
    print("Hello player one, please type:")
    choice = validate_input()
    print(run(choice))
