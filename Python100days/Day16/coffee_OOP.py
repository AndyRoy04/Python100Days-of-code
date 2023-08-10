from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
find_menu = Menu()

machine_on = True

while machine_on:
    available_drinks = find_menu.get_items()
    order_name = input(f"What would you like ? ({available_drinks}): ")

    if order_name == 'off':
        machine_on = False
    elif order_name == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = find_menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)