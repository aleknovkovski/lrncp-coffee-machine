# Write your code here

class CoffeeMachine:
    active = True
    state = None

    def __init__(self, stock, menu):
        self.stock = stock
        self.menu = menu

    def run(self):
        while self.active:
            action = input("Write action (buy, fill, take, remaining, exit): \n")
            if action == "buy":
                self.buying()
            elif action == "fill":
                self.filling()
            elif action == "take":
                self.taking()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                CoffeeMachine.active = False

    def print_state(self):
        qnt = self.stock

        print("The coffee machine has:")
        print(f"{qnt['water']} ml of water")
        print(f"{qnt['milk']} ml of milk")
        print(f"{qnt['beans']} g of coffee beans")
        print(f"{qnt['cups']} disposable cups")
        print(f"${qnt['money']} of money\n")

    def check_viability(self, water, milk, beans):
        missing = None
        viable = True

        if self.stock["water"] < water:
            missing = "water"
            viable = False
        elif self.stock["milk"] < milk:
            missing = "milk"
            viable = False
        elif self.stock["beans"] < beans:
            missing = "milk"
            viable = False

        return viable, missing

    def fulfill(self, item):
        # Shortcuts
        product = self.menu[item]
        req = product["requirements"]

        # Variables
        price = product["price"]
        water = req["water"]
        milk = req["milk"]
        beans = req["beans"]

        # Check viability
        viable, missing = self.check_viability(water, milk, beans)

        if viable:
            print("I have enough resources, making you a coffee!\n")

            # Process
            self.stock["money"] += price
            self.stock["water"] -= water
            self.stock["milk"] -= milk
            self.stock["beans"] -= beans
            self.stock["cups"] -= 1

        if not viable:
            print(f"Sorry, not enough {missing}")

    def buying(self):
        purchase = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n")

        if purchase == "back":
            return
        else:
            self.fulfill(int(purchase))

    def filling(self):
        self.stock["water"] += int(input("Write how many ml of water you want to add:\n"))
        self.stock["milk"] += int(input("Write how many ml of milk you want to add:\n"))
        self.stock["beans"] += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.stock["cups"] += int(input("Write how many disposable cups of coffee you want to add:\n"))

    def taking(self):
        print(f"I gave you {self.stock['money']}\n")
        self.stock['money'] = 0

    def remaining(self):
        self.print_state()


# === INVENTORY

my_stock = {
    "water": 400,
    "milk": 540,
    "beans": 120,
    "cups": 9,
    "money": 550
}

my_menu = {
    1: {"name": "espresso", "price": 4, "requirements": {
        "water": 250,
        "milk": 0,
        "beans": 16
    }},
    2: {"name": "latte", "price": 7, "requirements": {
        "water": 350,
        "milk": 75,
        "beans": 20
    }},
    3: {"name": "cappuccino", "price": 6, "requirements": {
        "water": 200,
        "milk": 100,
        "beans": 12
    }}
}

# Run the machine
my_machine = CoffeeMachine(my_stock, my_menu)
my_machine.run()
