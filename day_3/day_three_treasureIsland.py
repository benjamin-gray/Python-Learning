# Treasure Island Game

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice_one = input('You are at a crossroad. Do you want to go "left" or "right"?: ').lower()

if choice_one == "left":
    choice_two = input('You have come to a lake. '
    'Do you want to "swim" or "wait" for a boat?: ').lower()

    if choice_two == "wait":
        choice_three = input('You arrive at the island unharmed. '
        'There is a house with three doors. '
        'One "red", one "yellow", and one "blue". '
        'Which color do you choose?: ').lower()

        if choice_three == "red":
            print("You were burned by fire. Game Over.")
        elif choice_three == "yellow":
            print("You found the treasure! You win!")
        elif:
            print("You were attacked by an ocelot. Game Over.")
        else:
            print("Invalid door, game over.")

    else:
        print("You were attacked by an alligator. Game Over.")


if choice_one == "right":
    print("You fell into a hole. Game Over.")
