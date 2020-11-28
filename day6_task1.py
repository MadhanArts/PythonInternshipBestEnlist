n = int(input("Enter number of elements : "))
my_list = []
print("Enter the elements : ")
for i in range(n):
    my_list.append(int(input()))

print("My list : ", my_list)
for i in range(len(my_list)):
    my_list[i] += 2

print("My list after adding +2 to every elements :", my_list)
