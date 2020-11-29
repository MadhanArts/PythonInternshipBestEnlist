import day7_task1_1 as list_file

print("My list in another file : ", list_file.my_list)
list_file.my_list.remove("tomato")
print("My list after removing 'tomato' : ", list_file.my_list)
list_file.my_list.append("mango")
print("My list after appending 'mango' : ", list_file.my_list)
list_file.my_list[list_file.my_list.index("banana")] = "grapes"
print("My list after changing 'banana' to 'grapes' : ", list_file.my_list)
