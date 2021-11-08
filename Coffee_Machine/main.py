MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 50
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


# TODO : 2. Print the report
def report(resources, money):
    return f" Water : {resources['water']} \n Milk : {resources['milk']} \n Coffee : {resources['coffee']} \n Money : ${money}"


# TODO : 3. Turn off the machine

# TODO : 4. Check if the resources are sufficient

def resources_sufficient(resources, choice):
    if MENU[choice]['ingredients']['water'] > resources['water']:
        print("Sorry there is not enough water")
        return False
    if MENU[choice]['ingredients']['milk'] > resources['milk']:
        print("Sorry there is not enough milk")
        return False
    if MENU[choice]['ingredients']['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee")
        return False
    return True


# TODO : 5. Process coins

def convert_dollar(quarters, dimes, nickles, pennies):
    total = 0.0
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


# TODO : 6. check if the transaction is successful

def transaction(amount, choice):
    change = 0
    if amount < MENU[choice]['cost']:
        print('​Sorry that\'s not enough money. Money refunded.​')
        return change
    elif amount > MENU[choice]['cost']:
        change = amount - (MENU[choice]['cost'])
        return round(change, 2)


# TODO : 7. Make coffee
# TODO : 1. Ask the user input “What would you like? (espresso/latte/cappuccino):”

# choice = input('What would you like? (espresso/latte/cappuccino):').lower()
# print(choice)
money = 0.0
should_continue = True
while should_continue:
    choice = input('What would you like? (espresso/latte/cappuccino):').lower()
    if choice == 'report':
        print(report(resources, money))
    elif choice == 'off':
        should_continue = False
    else:
        sufficient = resources_sufficient(resources, choice)
        print(sufficient)
        if not sufficient:
            pass
        else:
            print("Please insert coins")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            amount_paid = convert_dollar(quarters, dimes, nickles, pennies)
            change = transaction(amount_paid, choice)
            if change > 0.0:
                print(f'Here is ${change} dollars in change.')
            money += amount_paid
            resources['water'] -= MENU[choice]['ingredients']['water']
            resources['milk'] -= MENU[choice]['ingredients']['milk']
            resources['coffee'] -= MENU[choice]['ingredients']['coffee']
            if change != 0:
                print(f"Here is your {choice} ☕️. Enjoy!")

#option + shift drags the cursor to multiple lines
