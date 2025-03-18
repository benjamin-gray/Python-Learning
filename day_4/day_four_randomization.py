# Randomizaaation Module

# Deteministic: same input will always produce the same output

import random

#rando_int = random.randint(1,10)
#print(rando_int)

#random_number = random.random() * 10
#print(random_number)

#random_float = random.uniform(1,10)
#print(random_float) 

# Heads or Tails

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")