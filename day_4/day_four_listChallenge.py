#Who will pay the bill

import random

friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
random_friend = (random.choice(friends))
print(f"{random_friend} will pay the bill today.")

#OR

random_index = random.randint(0, 4)
print(f"{friends[random_index]} will pay the bill today.")