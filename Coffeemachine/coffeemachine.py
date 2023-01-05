class CoffeeMachine:

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def fill(self):

        while True:
            try:
                self.water += int(input("Write how many ml of water you want to add:\n"))
                self.milk += int(input("Write how many ml of milk you want to add:\n"))
                self.beans += int(input("Write how many grams of coffee beans you want to add:\n"))
                self.cups += int(input("Write how many disposable coffee cups you want to add:\n"))
                return

            except ValueError:
                print("you must enter the quantity")

    def remaining(self):
        print(f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} of coffee beans
{self.cups} of cups
{self.money} of money
""")

    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def buy(self):
        print("What do you want to buy?\n1 - espresso\n2 - latte\n3 - cappuccino\n4 – to main menu")

        while True:
            choose = input()

            if choose == "1":
                if self.water < 250 or self.beans < 16 or self.cups < 1:
                    print("not enough ingredients\n")

                else:
                    self.water -= 250
                    self.beans -= 16
                    self.money += 4
                    self.cups -= 1
                    print("I have enough resources, making you a coffee!\n")

                return

            elif choose == "2":
                if self.water < 375 or self.beans < 20 or self.cups < 1 or self.milk < 75:
                    print("not enough ingredients")

                else:
                    self.water -= 375
                    self.milk -= 75
                    self.beans -= 20
                    self.money += 7
                    self.cups -= 1
                    print("I have enough resources, making you a coffee!")

                return

            elif choose == "3":
                if self.water < 200 or self.beans < 12 or self.cups < 1 or self.milk < 100:
                    print("not enough ingredients")

                else:
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.money += 6
                    self.cups -= 1
                    print("I have enough resources, making you a coffee!")

                return

            elif choose == "4":
                return

            else:
                print("choose one of the proposed values")


coffee_machine = CoffeeMachine()


def start():

    while True:
        print("Write action (buy, fill, take, remaining, exit):\n")
        start_input = input().lower()

        if start_input == "buy":
            coffee_machine.buy()

        elif start_input == "fill":
            coffee_machine.fill()

        elif start_input == "take":
            coffee_machine.take()

        elif start_input == "remaining":
            coffee_machine.remaining()

        elif start_input == "exit":
            exit()


start()
