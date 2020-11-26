n = int(input("Enter List size : "))
my_list = []
for i in range(n):
    item = int(input())
    my_list.append(item)
print(my_list)
# Add an item to list
item = int(input("Enter an item to add : "))
my_list.append(item)
print("My list after adding item :", my_list)

# delete an item in list
deleted_item = my_list.pop(2)
print("My list after deleting", deleted_item, "in 2nd index :", my_list)

# Store largest number from the list to variable
largest_value = max(my_list)
print("Largest number in my list using in-built function is ", largest_value)
# OR
largest_value = my_list[0]
for i in range(1, n):
    if my_list[i] > largest_value:
        largest_value = my_list[i]
print("Largest number in my list using loop is ", largest_value)

# Store smallest number from the list to variable
smallest_value = min(my_list)
print("Smallest number in my list using in-built function is ", smallest_value)
# OR
smallest_value = my_list[0]
for i in range(1, n):
    if my_list[i] < smallest_value:
        smallest_value = my_list[i]
print("Smallest number in my list using loop is ", smallest_value)
