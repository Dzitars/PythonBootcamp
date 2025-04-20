MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def check_resources(recipe):
    """Checks if there are enough resources left to make the selected drink"""
    for item in recipe["ingredients"]:
        if recipe["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def print_report():
    """Prints out a report of the 'resources' data object"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def process_coins():
    """Asks user to enter how many of each coin and returns the total amount in $"""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total

def check_transaction(money_received, drink_cost):
    """Checks if the user has entered enough money, and either gives them their change or tells them they don't have enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def update_resources(recipe):
    """Updates the resources by removing the ingredients used in the recipe that this function is sent"""
    for item in recipe["ingredients"]:
        resources[item] -= recipe["ingredients"][item]
    resources["money"] += recipe["cost"]

machine_is_on = True
while machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) ")

    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print_report()
    elif choice in MENU:
        if check_resources(MENU[choice]):
            money = process_coins()
            if check_transaction(money, MENU[choice]["cost"]):
                update_resources(MENU[choice])
                print(f"Here is your {choice}. Enjoy!")

    else:
        print("That is an invalid entry")