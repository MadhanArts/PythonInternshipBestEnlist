# To get inputs using lambda
n = int(input("Enter the size of list : "))
my_list = list(map(lambda x: int(input()), range(n)))
print(my_list)

# To get Even counts in list using lambda
count = len(list(filter(lambda x: x % 2 == 0, my_list)))
print("Even numbers count : ", count)
