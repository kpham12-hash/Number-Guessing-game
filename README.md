# Number-Guessing-game
Its a mini project where the user has to guess the right number the program is thinking of. If the user gets it wrong then the game ends.The program asks the user to enter a number and checks whether their guess matches the generated number. If the guess is incorrect, the program prompts the user to try again. Once the user guesses correctly, the program displays the number of attempts.

# Sequence 
1. The guess count is set to zero, and the program generates a random number.
2. The prints a statement a statement "I'm thinking of a number between 1 and 100. "
3. At the same time, The program outputs a question "Can you guess what number is? " for the user to type in their input as an integer.
4. The user's integer gets stored in a variable, and it gets checked before entering a while loop.
5. If the user's guessed number doesn't match the computer's stored integer, then it goes into the while loop to get check with each of the if/elif statements.
6. And the attempt count goes up by 1.
7. The program outputs an input question "Try again: " inside of the While Loop. (It will keep that process going until the user's integer matches with the computer's stored integer).
8. When the user guesses the computer's guessed number, it will go to the else statement.
9. 2 Print Statements will come out:
"You guessed the right number."
The 2nd statement will print out the number of attempts the user took to guess it:
"It took you {attempts} attempts to guess it."
