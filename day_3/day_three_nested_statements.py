#Nested if statements and elif statements

#if condition:
#   doTHIS
#else:
#   doTHAT

#Nested if statements allow us to check multiple conditions in a single if statement
#if condition:
#   if another_condition:
#       doTHIS
#   else:
#       doTHAT
#else:
#   doTHIS

# Example of using if / else to check a condition
print("Welcome to Ben's Roller Coaster!")

# Get the user's height
height = int(input("Please enter your height in cm: "))

# Check if the height is above or below a certain threshold
if height >= 150:
    print("You are tall enough to ride the roller coaster!")
    
    age = int(input("Please enter your age: "))

    if age <=12:
        print("You are eligible for a child ticket. Please pay $5")

    elif age <= 18:
        print("You are eligible for a teen ticket. Please pay $7")

    else:
        print("You are eligible for an adult ticket. Please pay $12")
    

else:
    print("Sorry, you need to be taller to ride the roller coaster.")