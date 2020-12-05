from day13_task1.CoffeeMachine import CoffeeMachine
from day13_task1.drinks import drinks

my_machine = CoffeeMachine(3000, 2000, 1000, 0)

while True:
    print("****** Welcome sir ******")
    print("What would you like? ([1] espresso/[2] latte/[3] cappuccino)")
    choice = input("Enter your choice or option : ")

    if choice.lower() == "espresso" or "1":
        my_machine.make(drinks["espresso"])
    elif choice.lower() == "latte" or "2":
        my_machine.make(drinks["latte"])
    elif choice.lower() == "cappuccino" or "3":
        my_machine.make(drinks["cappuccino"])
    elif choice.lower() == "report":
        my_machine.generate_report()
    elif choice.lower() == "off":
        exit(1)
    else:
        print("No option like that sir! Try again")
