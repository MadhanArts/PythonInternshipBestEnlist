a = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug']
b = list(range(1, 9))
z = list(zip(a, b))
print("List 1 : ", a)
print("List 2 : ", b)
print("List of tuples after merging : ")
for t in z:
    print(t)
