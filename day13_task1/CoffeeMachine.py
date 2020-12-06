
class CoffeeMachine:
    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def generate_report(self):
        print("Report : ")
        print("Water : ", self.water, "ml", sep="")
        print("Milk : ", self.milk, "ml", sep="")
        print("Coffee : ", self.coffee, "g", sep="")
        print("Money : ", "$", self.money, sep="")

    def is_resource_sufficient(self, drink):
        is_sufficient = True
        if self.coffee < drink.coffee:
            is_sufficient = False
            print("Sorry there is not enough coffee")
        if self.milk < drink.milk:
            is_sufficient = False
            print("Sorry there is not enough milk")
        if self.water < drink.water:
            is_sufficient = False
            print("Sorry there is not enough water")

        return is_sufficient

    def process_coins(self, drink):
        print("It cost you $", drink.money, " sir", sep="")
        print("Insert Coins : ")
        try:
            quarters = int(input("Enter number of quarters : "))
            dimes = int(input("Enter number of dimes : "))
            nickles = int(input("Enter number of nickles : "))
            pennies = int(input("Enter number of pennies : "))
        except ValueError:
            print("Entered wrong value. Try again")
            return False

        total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        if total < drink.money:
            print("Sorry that's not enough money. Money refunded")
            return False
        elif total == drink.money:
            self.money += drink.money
            return True
        else:
            self.money += drink.money
            print("Here is ", "{:.2f}".format(total - drink.money), " dollars in change", sep="")
            return True

    def make(self, drink):
        if self.is_resource_sufficient(drink) and self.process_coins(drink):
            self.water -= drink.water
            self.milk -= drink.milk
            self.coffee -= drink.coffee
            print("Here is your ", drink.name, ". Enjoy!", sep="")
