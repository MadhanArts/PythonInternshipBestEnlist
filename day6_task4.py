"""
Armstrong number is a number which is equal to the sum of its
own digits raised to the power of the number of digits
"""
import math


def is_armstrong_number(n, length):
    t = n
    temp = 0
    while t > 0:
        last_digit = t % 10
        temp = temp + math.pow(last_digit, length)
        t = t // 10

    if temp == n:
        return True
    return False


num = int(input("Enter the number : "))
num_length = math.floor(math.log10(num)) + 1
if is_armstrong_number(num, num_length):
    print(num, "is armstrong number")
else:
    print(num, "is not armstrong number")
