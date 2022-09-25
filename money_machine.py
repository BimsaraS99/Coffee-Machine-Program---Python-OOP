class MoneyMachine:
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):  # attributes of the coffee maker
        self.profit = 0
        self.money_received = 0

    def report(self):  # gives the report about the profit if the user ask
        print(f"Profit :${self.profit}")

    def process_coin(self):  # getting user inputs of coins and return the total value of money here
        print("Please insert coin")
        for coin in self.COIN_VALUES:
            coin_input = int(input(f"How many {coin} : "))
            self.money_received += (coin_input * self.COIN_VALUES[coin])
        return self.money_received

    def make_payment(self, cost):  # return true if the user has input enough money otherwise return false
        self.process_coin()
        if self.money_received > cost:
            print(f"Here is ${round(self.money_received - cost,2)} in charge.")
            self.profit += cost
            self.money_received = 0
            return True

        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
