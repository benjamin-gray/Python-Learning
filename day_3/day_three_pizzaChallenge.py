# Pizza Challenge
print("Welcome to the Pizza Challenge!")
size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0.00

# todo: work out hhow much they need to pay pased on their size choice

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size choice. Please choose S, M, or L.")
    exit()

# todo: work out how much to add to their bill based on the pepperoni choice.

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether or not they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill:.2f}.") # todo: format the bill to 2 decimal places.