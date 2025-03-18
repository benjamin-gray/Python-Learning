#Multiple if statements in succession

# Example of using if / else to check a condition
print("Welcome to Ben's Roller Coaster!")

# Get the user's height
height = int(input("Please enter your height in cm: "))
bill = 0

# Check if the height is above or below a certain threshold
if height >= 150:
    print("You are tall enough to ride the roller coaster!")
    
    age = int(input("Please enter your age: "))

    if age <=12:
        bill += 5
        print("You are eligible for a child ticket.")

    elif age <= 18:
        bill += 7
        print("You are eligible for a teen ticket.")

    else:
        bill += 12
        print("You are eligible for an adult ticket.")
    
    wants_photo = input("Do you ant to have a photo taken? Type y for yes or n for no. \n")

    if wants_photo == "y":
        # add $3 to the bill
        bill += 3
        print("Your photo will be taken.")

    print(f"Your total bill is ${bill}. Thank you for riding with us!")

else:
    print("Sorry, you need to be taller to ride the roller coaster.")