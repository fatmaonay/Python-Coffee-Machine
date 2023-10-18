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

def enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    cost = int(input("How many quarters? ")) * 0.25
    cost += int(input("How many dimes? ")) * 0.1
    cost += int(input("How many nickles? ")) * 0.05
    cost += int(input("How many pennies? ")) * 0.01
    return cost

def check_transaction_success(inserted_coins, order_cost):
    """Return True when payment is accepted, False otherwise."""""
    if inserted_coins < order_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(inserted_coins - order_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += order_cost
        return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ️. Enjoy!")

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino)\n")
    if order == "off":
        is_on = False
        
    elif order=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[order]
        if enough_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction_success(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
