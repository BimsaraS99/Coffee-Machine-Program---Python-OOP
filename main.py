import coffee_maker
import menu
import money_machine

coffee_make = coffee_maker.CoffeeMaker()
coffee_menu = menu.Menu()
money_manage = money_machine.MoneyMachine()

options = coffee_menu.get_items()

while True:
    user_input = input(f"\nWhat would you like? ({options}): ")

    if user_input == 'report':
        coffee_make.report()
        money_manage.report()

    elif user_input == 'off':
        break

    else:
        drink = coffee_menu.find_drink(user_input)
        if coffee_make.is_resource_sufficient(drink):
            if money_manage.make_payment(drink.cost):
                coffee_make.make_coffee(drink)

