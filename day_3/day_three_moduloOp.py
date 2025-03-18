#Modulo Operator
# The modulo operator (%) returns the remainder of a division operation.
# For example, 10 % 3 returns 1 because 10 divided by 3 is 3 with a remainder of 1.

print(10 % 3)

input_number = int(input("Enter a number: "))
# Check if the number is even or odd using the modulo operator

if input_number % 2 == 0:
    print("EVEN!")
else:
    print("ODD!")