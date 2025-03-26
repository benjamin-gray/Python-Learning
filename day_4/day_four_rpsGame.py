#Rock Paper Scissors Game
import random

rock = "0"
paper = "1"
scissors = "2"

images = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\nYou chose: 2")) #0, 1, 2
user_choice = int(user_choice)
if user_choice >= 0 or user_choice <= 2:
    print(images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
print(images[computer_choice])


if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid choice. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("It's a draw :(")
