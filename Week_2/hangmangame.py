# Build a Python Script for the Popular Hangman Game

# In this project you will create a python project implementing the hangman game enabling the player to attempt guessing a hidden word. If you are not farmiliar with the game, check out the graphical online game here.

# In summary the user has attempts at guessing a word represented in a row of dashes and if a player guesses a letter which exists in the word, the program writes it in all correct positions, these attempts are reduced for every wrong character guess the player makes, once all are exhausted, without a matching word having been guessed, the monster eats up the player.
# Here are the steps to follow:

#     Choose some good hangman words for your program. You can go to this website and create a list of words for your game.
#     At the start of the game, use the random library to choose a random word from your hangman words and display the word's letters as dashes rather than letters.
#     Now, apply the input function to allow the user to make letter guesses. Use try... except and if statements to make sure that only valid inputs work with your script i.e. a user can only choose one letter at a time, and a user cannot choose letters that have been chosen before.
#     If the letter is in the word then it is printed in place of the corresponding dash. If the letter is not in the word, that is counted as a failed attempt, Limit the number of failed attempts for the user to 6 such that on the 6th fail, the game ends and the script prints the actual word and "You Lost". Make sure to tell the user they won if they guess all the correct letters in under 6 failed attempts.
#     If you want to take the project a notch higher, you can use the Python Turtle Library to visualize the hanging like in this website. This is optional!

import random

# List of words to choose from
word_list = ['food', 'mercy', 'mother', 'school',]

# Pick a random word
word = random.choice(word_list)

# Create a hidden version of the word using underscores
hidden_word = ['_'] * len(word)

# Keep track of guessed letters and wrong guesses
guessed_letters = []
wrong_tries = 0
max_tries = 6

print("Guess the word by guessing one letter at a time.")
print("You have 6 wrong guesses before the game ends.\n")

# Show the hidden word
print(" ".join(hidden_word))

# Start the game loop
while wrong_tries < max_tries and '_' in hidden_word:
    letter = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if letter was already guessed
    if letter in guessed_letters:
        print("You already guessed that letter. Try a guessing another one.")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(letter)

    # Check if letter is in the word
    if letter in word:
        print("Congratulations! That letter is in the word.")

        # Reveal the letter in the hidden word
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
    else:
        print("Sorry That letter is not in the word.")
        wrong_tries += 1
        print("Wrong tries left:", max_tries - wrong_tries)

    # Show the current state of the word
    print(" ".join(hidden_word))
    
# Game over: Check win or lose
if '_' not in hidden_word:
    print(" You won! Great job guessing the word:", word)
else:
    print("You lost. The word was:", word)
    
