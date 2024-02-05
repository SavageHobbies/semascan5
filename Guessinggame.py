# Writen by Perplexity

import random

def guessing_game(start, end):
    number = random.randint(start, end)
    guess = None
    while guess != number:
        guess = int(input(f"Guess a number between {start} and {end}: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("Congratulations! You guessed the number!")

# Call the function with the range of numbers
guessing_game(1, 100)