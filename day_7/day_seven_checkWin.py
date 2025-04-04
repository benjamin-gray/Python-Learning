
import random

words_list= ["dog", "cat", "fish", "bird", "elephant", "giraffe", "lion", "tiger", "bear", "zebra"]

chosen_word = random.choice(words_list)
print(f"Chosen word: {chosen_word}")  

placeholder = "" 

for position in range(len(chosen_word)): 
    placeholder += "_" 
print(placeholder)

# TODO: create while loop freo the user to guess again

game_over = False # var to help keep player guessing
correct_letters = [] # need to make list outside of loop

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(guess)

    display = "" 

# TODO: change the for loop so that you keep the previous correct guess

    for letter in chosen_word:
        if letter == guess:
            display += letter 
            correct_letters.append(letter) # add the correct letter to the list of correct letters
        elif letter in correct_letters:
            display += letter # if the letter is already guessed correctly, keep it in the display
        else:
            display += "_" 

    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")