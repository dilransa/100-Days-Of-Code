play = True

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
            "water": 50,
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


def availability():
    if ask == 'espresso':
        if resources['water'] >= 200 and resources['coffee'] >= 18:
            return True
        else:
            return False

    elif ask == 'latte':
        if resources['water'] >= 250 and resources['coffee'] >= 24 and resources['milk'] >= 150:
            return True
        else:
            return False

    elif ask == 'cappuccino':
        if resources['water'] >= 50 and resources['coffee'] >= 24 and resources['milk'] >= 100:
            return True
        else:
            return False


while play:
    ask = input('What would you like? (espresso/latte/cappuccino):').lower()
    check = availability()

    while ask == 'report':
        print('Available Resources : ')
        print(f"Water :{resources['water']}")
        print(f"Milk :{resources['milk']}")
        print(f"Coffee :{resources['coffee']}")

        break

    while check:
        print('Please insert coins')
        ask_quarters = int(input('how many quarters?:'))*0.25
        ask_dimes = int(input('how many dimes?:')) * 0.25
        ask_nickels = int(input('how many nickels?:')) * 0.25
        ask_pennies = int(input('how many pennies?:')) * 0.25

        amount = ask_quarters+ask_dimes+ask_nickels+ask_pennies

        if amount >= MENU[ask]['cost']:

            # Count of milk water coffee has been used

            resources['water'] -= MENU[ask]['ingredients']['water']
            resources['coffee'] -= MENU[ask]['ingredients']['coffee']
            resources['milk'] -= MENU[ask]['ingredients']['milk']

            balance = amount - MENU[ask]['cost']
            if balance >0:
                print(f"This is your balance {balance}, Enjoy your {ask}")
            else:
                print(f"Enjoy your {ask}")

        else:
            print("Sorry that's not enough money. Money refunded.")
            check = False

        check = False

    if check == False:
        continue
