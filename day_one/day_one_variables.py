#learning variables
#variables are used to store information

name = input("what is your name? ") #prompt for user to input name(data)
print(name)

name = "Vini" #reassigning the variable name to a new value
print(name)

#challenge - figure out how many characters are in the name variable

name = input("what is your name? ") 
print(name,len(name)) #len() is a built-in function that returns the number of characters in a string

#or

username = input("Enter your username: ")
length = len(username)
print(length)
