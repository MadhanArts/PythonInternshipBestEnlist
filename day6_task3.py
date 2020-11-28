x1 = -1
x2 = 1
n = int(input("Enter the nth term :"))      # getting nth term from user
for i in range(n):
    t = x1 + x2                             # calculating the term value t
    print(t)                                # printing the value
    x1 = x2                                 # changing x1 to x2
    x2 = t                                  # changing x2 to t
