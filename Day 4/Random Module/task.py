import random
import my_module

#Generate random integer
#rand_num = random.randint(1,10)
#print(rand_num)

print(my_module.my_favorite_number)


#Inclusive of 0, not inclusive of 1. Can multiply number to get range you want
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

#Same as .random, but includes the upper range. Try to use .random and multiply if you want to be sure not to include upper
random_float = random.uniform(1,10)
print(random_float)


heads_or_tails = random.randint(1,2)
if heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")