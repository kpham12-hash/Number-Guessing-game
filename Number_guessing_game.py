# Actual Game Code 

import random

attempts = 0

guess = random.randint(0, 100)

attempts += 1

print("I'm thinking of a number between 1 and 100. ")
guessed_number = int(input("Can you guess what number is? "))

while guessed_number != guess:
    if guessed_number > guess:
        print("You're guess is too high.")

    elif guessed_number < guess:
        print("You're guess is too low.")

    attempts += 1

    guessed_number = int(input("Try again: "))

else:
    print("You guessed the right number.")
    print(f"It took you {attempts} attempts to guess it.")
