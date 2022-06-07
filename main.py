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
}

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
choose_coffee = input("What would you like? (espresso/latte/cappuccino)☕: ")

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
if choose_coffee == "off".lower():
    print("Coffee machine is going to be switched off.")
    exit()
# TODO: 3. Resources report
elif choose_coffee == "report".lower():
    for key, value in resources.items():
        if key == 'coffee':
            print(f"{key}: {value}g")
        else:
            print(f"{key}: {value}ml")
    exit()
# TODO: 4. Check resources sufficient?
elif choose_coffee == "espresso".lower():
    resources["water"] -= 50
    resources["coffee"] -= 18
elif choose_coffee == "latte".lower():
    resources["water"] -= 200
    resources["coffee"] -= 24
    resources["milk"] -= 150
elif choose_coffee == "cappuccino".lower():
    resources["water"] -= 250
    resources["coffee"] -= 24
    resources["milk"] -= 100

#print(resources)
# TODO: 5. Process coins.
print("Please insert coins.")
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
quarters_count = int(input("How many quarters?: "))
dimes_count = int(input("How many dimes?: "))
nickles_count = int(input("How many nickles?: "))
pennies_count = int(input("How many pennies?: "))
money_sum = quarters_count*quarters + dimes_count*dimes + nickles_count*nickles + pennies_count*pennies
money_sum_rounded = round(money_sum,2)
print(f"Here is ${money_sum_rounded} in change.")

# TODO: 6. Check transaction successful?
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]
if choose_coffee == "espresso".lower() and money_sum_rounded > espresso_price:
    money_sum_rounded -= espresso_price
    print(f"Here is your {choose_coffee} ☕. Enjoy!")
elif choose_coffee == "latte".lower() and money_sum_rounded > latte_price:
    money_sum_rounded -= latte_price
    print(f"Here is your {choose_coffee} ☕. Enjoy!")
elif choose_coffee == "cappuccino".lower() and money_sum_rounded > cappuccino_price:
    money_sum_rounded -= cappuccino_price
    print(f"Here is your {choose_coffee} ☕. Enjoy!")
else:
    print("Sorry that's not enough money. Money refunded.")


