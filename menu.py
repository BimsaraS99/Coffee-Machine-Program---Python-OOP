class MenuItem:
    """Menu items"""
    def __init__(self, name, water, milk, coffee, cost):  # attributes of MenuItem class
        self.name = name
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
        self.cost = cost


class Menu:
    """Controlling the menu here"""
    def __init__(self):  # making three objects using MenuItem class
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):  # return the all name of the available items here
        options = str()
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):  # return the MenuItem object if available otherwise return none
        for item in self.menu:
            if item.name == order_name:
                return item
        return None


