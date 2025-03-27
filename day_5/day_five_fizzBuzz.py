#Fizz Buzz Game which is a simple game where you count, but say "Fizz" and/or "Buzz" instead of numbers adhering to certain rules.

total = 0

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)