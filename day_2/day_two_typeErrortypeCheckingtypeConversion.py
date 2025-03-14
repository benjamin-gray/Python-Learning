#type Error, Checking, Conversion

#len(12345) #TypeError: object of type 'int' has no len()
print(len("12345")) #this will give the length of the string, which is 5

#type checking
print(type(12345)) #this will give the type of the variable, which is int
print(type("hello")) #this will give the type of the variable, which is str
print(type(3.14)) #this will give the type of the variable, which is float
print(type(True)) #this will give the type of the variable, which is bool

#type conversion/casting = changing the type of a variable
print("123")
print(int("123") + int("345")) #this will give the sum of the two integers, which is 468

#we can convert into int(), float(), str(), bool()

print("Number of letters in your name: " + str(len(input("What is your name? ")))) #this will give the length of the string, which is 5
