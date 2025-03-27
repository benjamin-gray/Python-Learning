# for loops and the range function

#example Range
# for number in range(a, b):
#     print(number)

#range has to be used with another function like a for loop to be useful

for number in range(1, 10): # this will print numbers 1-9 but will not include 10
    print(number)

for number in range(1, 11, 3): # this will print numbers 1-10 but will skip every 3rd number
    print(number)

#find total of all numbers from 1-100
total=0 # must set total to 0 before the for loop
for number in range(1, 101): #this will loop through the numbers 1-100
    total += number #adds 1 through 100
print(total) #prints the total of all numbers from 1-100