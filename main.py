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

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        break
    
    elif user_choice == "report":
        for item, quantity in resources.items():
            print(f"{item}: {quantity}")
        continue
              
    elif user_choice not in MENU:
        print("Invalid choice. Please try again.")
        continue
    
    drink = MENU[user_choice]
    
    if drink["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
        continue
    elif drink["ingredients"].get("milk") and drink["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        continue
    elif drink["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        continue
    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_amount = quarters + dimes + nickels + pennies
    
    if drink["cost"] < total_amount:
        remain_amount = total_amount - drink["cost"]
        print(f"Here is {remain_amount:.2f} in change.")
        print(f"Here is your {user_choice} ☕")
        
        # Deduct the required ingredients from the resources
        resources["water"] -= drink["ingredients"]["water"]
        if "milk" in drink["ingredients"]:
            resources["milk"] -= drink["ingredients"]["milk"]
        resources["coffee"] -= drink["ingredients"]["coffee"]
    elif drink["cost"] > total_amount:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        print(f"Here is your {user_choice} ☕")
        
        # Deduct the required ingredients from the resources
        resources["water"] -= drink["ingredients"]["water"]
        if "milk" in drink["ingredients"]:
            resources["milk"] -= drink["ingredients"]["milk"]
        resources["coffee"] -= drink["ingredients"]["coffee"]
