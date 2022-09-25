class CoffeeMaker:
    """The coffee maker"""
    def __init__(self):  # attributes of the coffee maker
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):  # making the report here if the user ask
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):  # drink is an object which created with MenuItem class
        for item in self.resources:
            if self.resources[item] < drink.ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink_object):  # make the coffee if the user has input enough money
        print(f"Here is your {drink_object.name}. Enjoy it ;)")
        for item in self.resources:
            self.resources[item] -= drink_object.ingredients[item]

