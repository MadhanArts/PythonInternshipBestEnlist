# To get inputs using lambda
n = int(input("Enter the size of list : "))
my_list = list(map(lambda x: int(input()), range(n)))
print("My list: ", my_list)

# To get numbers divisible by 9
new_list = list(filter(lambda x: x % 9 == 0, my_list))
print("My list of number divisible by 9 : ", new_list)
