from Menu import coffee_machine, menu, resources

def check_drink(user_input):
    """This function takes the users input and check for the availability of the ingredients and its cost"""
    global drink_cost, drink_coffee, drink_milk, drink_water
    
    user_drink = menu[user_input]

    drink_ingredients = user_drink["ingredients"]   
    drink_water = drink_ingredients['water']
    drink_milk = drink_ingredients['milk']
    drink_coffee = drink_ingredients['coffee']

    drink_cost = user_drink["cost"]

    if drink_water > machine_water:
        print("Sorry there is not enough water")
        return True
    elif drink_milk > machine_milk:
        print("Sorry there is not enough milk")
        return True
    elif drink_coffee > machine_coffee:
        print("Sorry there is not enough coffee")
        return True


def insert_coins():
    """This function is used to calculate the amount of counts the user inserted"""
    global user_coins
    print("Please Insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    user_coins = round((quarters + dimes + nickles + pennies), 2)


machine_water = resources["water"]
machine_milk = resources["milk"]
machine_coffee = resources["coffee"]
machine_money = 0

drink_ingredients = 0
drink_water = 0
drink_milk = 0
drink_coffee = 0 
user_coins = 0
drink_cost = 0
machine_on = True

print(coffee_machine)
while machine_on:
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print(f"Water: {machine_water}ml\nMilk: {machine_milk}ml\nCoffee: {machine_coffee}g\nMoney: ${machine_money}")
    elif user_input == "off":
        machine_on = False
    elif user_input not in menu:
        print(f"This Machine doesn't produce {user_input}")
    else:
        if check_drink(user_input) == True:
            continue
        else:
            insert_coins()

        if user_coins >= drink_cost:
            balance = round((user_coins - drink_cost), 2)
            print(f"Here is your warm {user_input} ☕")
            print(f"Your balance is ${balance}")

            machine_water -= drink_water
            machine_milk -= drink_milk
            machine_coffee -= drink_coffee
            machine_money += (round((user_coins - balance), 2))
        else:
            print(f"Sorry ${user_coins} is not enough for {user_input}. Money refunded.")
        
