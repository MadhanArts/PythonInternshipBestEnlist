choice = int(input("1. Addition"
                   "\n2. Subtraction"
                   "\n3. Multiplication"
                   "\n4. Division"
                   "\nEnter your choice :"))
if choice == 1:
    try:
        a = float(input("Enter 1st number : "))
        b = float(input("Enter 2nd number : "))
        print(a + b)
    except ValueError:
        print("Inappropriate value")
    except ArithmeticError:
        print("Arithmetic exception occurred")
    except TypeError:
        print("Inappropriate data type occurred")
    except:
        print("Error occurred")
elif choice == 2:
    try:
        a = float(input("Enter 1st number : "))
        b = float(input("Enter 2nd number : "))
        print(a - b)
    except ValueError:
        print("Inappropriate value")
    except ArithmeticError:
        print("Arithmetic exception occurred")
    except TypeError:
        print("Inappropriate data type occurred")
    except:
        print("Error occurred")
elif choice == 3:
    try:
        a = float(input("Enter 1st number : "))
        b = float(input("Enter 2nd number : "))
        print(a * b)
    except ValueError:
        print("Inappropriate value")
    except ArithmeticError:
        print("Arithmetic exception occurred")
    except TypeError:
        print("Inappropriate data type occurred")
    except:
        print("Error occurred")
elif choice == 4:
    try:
        a = float(input("Enter 1st number : "))
        b = float(input("Enter 2nd number : "))
        print(a / b)
    except ValueError:
        print("Inappropriate value")
    except ZeroDivisionError:
        print("Can't divide by 0")
    except TypeError:
        print("Inappropriate data type occurred")
    except ArithmeticError:
        print("Arithmetic exception occurred")
    except:
        print("Error occurred")
else:
    print("Invalid choice")
