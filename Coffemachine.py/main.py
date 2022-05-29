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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_r(o_i):
    for i in o_i:
        if o_i[i] >= resources[i]:
            print(f"Sorry there is not enough {i}. ")
            return False
    return True
        

is_on = True
while is_on:
    choice = input("What would you like to have espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
    elif choice =="report":
       print(f"water: {resources['water']}ml")
       print(f"milk: {resources['milk']}ml")
       print(f"coffee: {resources['coffee']}g")
       print(f"money:{profit}$")
    else:
        drink=MENU[choice]
        enough_r(drink["ingredients"])