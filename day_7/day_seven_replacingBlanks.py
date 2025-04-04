# Replacing blanks in a word guessing game

import random

words_list= ["dog", "cat", "fish", "bird", "elephant", "giraffe", "lion", "tiger", "bear", "zebra"]

chosen_word = random.choice(words_list)
print(f"Chosen word: {chosen_word}")  

# TODO: Create placeholder for the word with blanks

placeholder = "" 

for position in range(len(chosen_word)): # loop through the length of the chosen word
    placeholder += "_" # add a blank for each letter in the word
print(placeholder)

guess = input("Guess a letter: ").lower()
print(guess)

# TODO: create a display for the word with blanks replaced by the guessed letter

display = "" # this will be the final display of the word with blanks replaced by the guessed letter

for letter in chosen_word:
    if letter == guess:
        display += letter # if the letter is correct, replace the blank with the letter
    else:
        display += "_" # if the letter is incorrect, keep the blank

print(display)