from day13_task1.CoffeeMachine import CoffeeMachine
from day13_task1.Drink import Drink

my_machine = CoffeeMachine(3000, 2000, 1000, 0)
latte = Drink("Latte", 200, 150, 24, 2.5)
espresso = Drink("Espresso", 150, 100, 30, 3)
cappuccino = Drink("Cappuccino", 150, 175, 20, 4)

while True:
    print("****** Welcome sir ******")
    print("What would you like? ([1] espresso/[2] latte/[3] cappuccino)")
    choice = input("Enter your choice or option : ").lower().strip()

    if choice in ("espresso", "1"):
        my_machine.make(espresso)
    elif choice in ("latte", "2"):
        my_machine.make(latte)
    elif choice in ("cappuccino", "3"):
        my_machine.make(cappuccino)
    elif choice == "report":
        my_machine.generate_report()
    elif choice == "off":
        exit(1)
    else:
        print("No option like that sir! Try again")
