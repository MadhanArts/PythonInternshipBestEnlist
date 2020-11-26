my_tuple = (1, 4, 12, 5, 10)
print("Method 1 :", my_tuple[::-1])     # reversing using slicing

# OR
my_tuple = list(my_tuple)   # converting my_tuple to list
new_list = []
for i in range(len(my_tuple)):  # iterating my_tuple
    new_list.insert(0, my_tuple[i])     # inserting each items at index 0

my_tuple = tuple(new_list)  # converting new list to tuple
print("Method 2 :", my_tuple)
