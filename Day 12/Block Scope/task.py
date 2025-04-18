# There is no block scope in python
# If statements, loops etc don't have their own scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()