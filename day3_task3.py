list1 = ["apple", "orange", "banana", "mango"]
list2 = [7, 9, 10, 15]
result = {}
for i in range(len(list1)):
    result[list1[i]] = list2[i]
print("list 1 :", list1)
print("list 2 :", list2)
print("mapped list :", result)
