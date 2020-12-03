my_list = [1, 2, 3, 4, 5, 6]
my_odd_list = list(filter(lambda x: x % 2 != 0, my_list))
print("My list : ", my_list)
print("My list after filtering even numbers : ", my_odd_list)
