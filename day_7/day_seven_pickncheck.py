# Pick a random word from a list of words and check if the word is in the list

import random

words_list= ["dog", "cat", "fish", "bird", "elephant", "giraffe", "lion", "tiger", "bear", "zebra"]

#TODO: Randomly choose word from the list
chosen_word = random.choice(words_list)  # Randomly select a word from the list
print(f"Chosen word: {chosen_word}")  

#TODO: Ask the user to guess a letter and assign it to the var guess
guess = input("Guess a letter: ").lower()  # use lower case because a user can input upper case letters, and the word list only have lower case
print(guess)

#TODO: Check if the letter the user guessed is one of the letters in the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("Correct!")
    else:
        print("Incorrect!")