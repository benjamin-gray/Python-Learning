 #IndexErrors and Working with Nested Lists

dirty_veggies = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#print(dirty_veggies[12]) #IndexError: list index out of range because the list has 12 items, and the index starts at 0, so the last item is at index 11.  

number_of_dirty_veggies = len(dirty_veggies)
print(dirty_veggies[number_of_dirty_veggies - 1])

#Nested Lists

veggies = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
dirty_dozen = [fruits, veggies]
