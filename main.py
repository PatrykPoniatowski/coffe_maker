from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    drink = menu.find_drink(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(money_machine.report())
        print(coffee_maker.report())
    elif drink is None:
        print("Sorry, we don't have this drink.")
    elif drink is not None:
        if coffee_maker.is_resource_sufficient(drink):
            customer_money = money_machine.process_coins()
            if customer_money < money_machine.make_payment(drink.cost):
                print("Sorry you didn't give sufficient amount of money")
            elif customer_money >= money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("There was a typo. Please choose what would you like? (espresso/latte/cappuccino): ")
