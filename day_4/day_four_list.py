#Understanding the Offset and Appending Items to Lists

#Creating a list uses square brackets [ ], and adding items to it separated by a comma, example: name_of_list = [1, 2, 3, 4, 5]
list = [1, 2, 3, 4, 5]
print(list)

fruits = ["Apple", "Orange", "Banana"]
print(fruits)

states_of_usa = ["California", "Texas", "Florida", "New York"]
print(states_of_usa)

# list order is important and determined by the offset which starts at 0

print(fruits[0])
print(fruits[1])
print(states_of_usa[0])
print(states_of_usa[-1])

#you may change the value of an item in a list by using the offset
(fruits[0]) = "Pineapple"
print(fruits)

#lists may be appended by using the append() method
fruits.append("Strawberry")
print(fruits)

states_of_usa.append("Washington")
print(states_of_usa)

list.append(6)
print(list) 