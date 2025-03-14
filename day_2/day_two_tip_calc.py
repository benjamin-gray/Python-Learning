#day two tip calc
# This program calculates the tip for a meal based on user input.
print("Welcome to Ben's Tip Calculator!")
# Get the total bill amount from the user
total=float(input("What was the total bill? $"))

# Get the percentage of tip the user wants to give
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Calculate the total amount to be paid including tip
tip=total * (tip_percentage / 100)

total_with_tip=total + tip

# Get the number of people to split the bill
people=int(input("How many people to split the bill? "))

# Calculate the amount each person needs to pay
per_person=round(total_with_tip / people,2)

# Display the results to the user
print(f"Each person should pay: ${per_person}") #this will give the amount each person needs to pay, rounded to 2 decimal places
