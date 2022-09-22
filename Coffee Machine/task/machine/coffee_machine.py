class CoffeeMachine:
    def __init__(self):
        self.money = 550
        self.cups = 9
        self.water_available = 400
        self.milk_available = 540
        self.beans_available = 120

    def is_sufficient(self, w=0, m=0, b=0, c=1):
        ret = True
        if self.water_available < w:
            print("Sorry, not enough water!")
            ret = False
        if self.milk_available < m:
            print("Sorry, not enough milk!")
            ret = False
        if self.beans_available < b:
            print("Sorry, not enough coffee beans!")
            ret = False
        if self.cups < c:
            print("Sorry, not enough cups!")
            ret = False
        return ret

    def fill(self, water, milk, coffee_beans, cup):
        self.water_available += water
        self.milk_available += milk
        self.beans_available += coffee_beans
        self.cups += cup

    def buy(self, coffee_type):
        can_buy = False
        if coffee_type == '1' and self.is_sufficient(250, 0, 16):
            self.water_available -= 250
            self.beans_available -= 16
            self.cups -= 1
            self.money += 4
            can_buy = True
        elif coffee_type == '2' and self.is_sufficient(350, 75, 20):
            self.water_available -= 350
            self.milk_available -= 75
            self.beans_available -= 20
            self.cups -= 1
            self.money += 7
            can_buy = True
        elif coffee_type == '3' and self.is_sufficient(200, 100, 12):
            self.water_available -= 200
            self.milk_available -= 100
            self.beans_available -= 12
            self.cups -= 1
            self.money += 6
            can_buy = True
        if can_buy:
            print('I have enough resources, making you a coffee!')

    def take(self):
        earning = self.money
        self.money = 0
        print(f"I gave you ${earning}")

    def remaining(self):
        message = (f"The coffee machine has:"
                   f"\n{self.water_available} ml of water"
                   f"\n{self.milk_available} ml of milk"
                   f"\n{self.beans_available} g of coffee beans"
                   f"\n{self.cups} disposable cups"
                   f"\n${self.money} of money")
        print(message)

    def main(self):
        while True:
            query = input("\nWrite action (buy, fill, take, remaining, exit):")
            if query == 'buy':
                order_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                if order_type == 'back':
                    continue
                else:
                    self.buy(order_type)
            elif query == 'fill':
                water_ = int(input("Write how many ml of water you want to add:"))
                milk_ = int(input("Write how many ml of milk you want to add:"))
                cf_beans = int(input("Write how many grams of coffee beans you want to add:"))
                cup_ = int(input("Write how many disposable cups you want to add:"))
                self.fill(water_, milk_, cf_beans, cup_)
            elif query == 'take':
                self.take()
            elif query == 'remaining':
                self.remaining()
            elif query == 'exit':
                break


if __name__ == "__main__":
    CoffeeMachine().main()
