from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()


def work():
    choice = input(f"Welcome! what would you like? {menu.get_items()}").lower()

    while choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
        choice = input(f"Please select a valid item? {menu.get_items()}").lower()

    if choice == "off":
        return True

    elif choice == "report":
        print(coffee.report())

    else:
        drink = menu.find_drink(choice)

        if coffee.is_resource_sufficient(drink):

            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)


turn_off = False
while not turn_off:
    turn_off = work()