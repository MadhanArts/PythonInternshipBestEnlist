choice = int(input("1. Addition"
                   "\n2. Subtraction"
                   "\n3. Multiplication"
                   "\n4. Division"
                   "\nEnter your choice :"))
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
else:
    print("Invalid choice")
