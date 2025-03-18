# Logical Operators

# Logical operators are used to combine multiple conditions in a single if statement.

# if condition1 & condition2 & condition3:
#     doTHIS
# else:
#     doTHAT

a = 12

print(a > 10 and a < 15) # True, because 12 is greater than 10 and less than 15

print(a > 10 or a < 10) # True, because 12 is greater than 10 (even though it is not less than 10)

print(not(a > 10)) # False, because the condition is true, but we are negating it with not


#update the Roller Coaster to give mid-life riders a free ride
print("Welcome to Ben's Roller Coaster!")

height = int(input("Please enter your height in cm: "))
bill = 0


if height >= 150:
    print("You are tall enough to ride the roller coaster!")
    
    age = int(input("Please enter your age: "))

    if age <=12:
        bill += 5
        print("You are eligible for a child ticket.")

    elif age <= 18:
        bill += 7
        print("You are eligible for a teen ticket.")

    elif age >= 45 and age <= 55: #could be written as "45 <= age >= 55"
        print("Everything will be okay!. Please enjoy your ride on the house!")

    else:
        bill += 12
        print("You are eligible for an adult ticket.")
    
    wants_photo = input("Do you ant to have a photo taken? Type y for yes or n for no. \n")

    if wants_photo == "y":
        bill += 3
        print("Your photo will be taken.")

    print(f"Your total bill is ${bill}. Thank you for riding with us!")

else:
    print("Sorry, you need to be taller to ride the roller coaster.")