# To get inputs using lambda
n = int(input("Enter the size of list : "))
my_list = list(map(lambda x: int(input()), range(n)))
print(my_list)

# To multiply each element in a list with multiple
multiple = int(input("Enter multiple to multiply : "))
my_list = list(map(lambda x: x * multiple, my_list))
print(my_list)
