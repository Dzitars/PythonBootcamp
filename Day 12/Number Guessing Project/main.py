import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
COMPUTER_NUMBER = random.randint(1,100)

def set_difficulty():
    dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if dif == "easy":
        return EASY_LEVEL_TURNS
    elif dif == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return -1

def check_guess(num):
    if num == COMPUTER_NUMBER:
        print(f"You got it! the answer was {COMPUTER_NUMBER}.")
        return -1
    elif num > COMPUTER_NUMBER:
        print("Too High.")
        return 0
    elif num < COMPUTER_NUMBER:
        print("Too Low.")
        return 0
    else:
        print("This shouldn't run")
        return 0

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    guesses_left = -1
    while guesses_left <= 0:
        guesses_left = set_difficulty()
        if guesses_left <= 0:
            print("That is an invalid selection")

    print(f"pssst, the number is {COMPUTER_NUMBER}")
    guess = 0
    while guesses_left > 0:
        print(f"You have {guesses_left} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        check = check_guess(guess)

        if check < 0:
            guesses_left = 0
        elif check == 0:
            guesses_left -= 1
            if guesses_left > 0:
                print("Guess again!")

    if guess == COMPUTER_NUMBER:
        print("You win!")
    else:
        print("You've run out of guesses, you lose!")

game()