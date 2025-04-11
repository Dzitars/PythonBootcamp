import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


#option 1
paying = random.choice(friends)

#option 2
#random_number = random.randint(0,len(friends)-1)
#paying = friends[random_number]


print(f"It is {paying}'s turn to pay today!")