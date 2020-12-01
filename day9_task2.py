n = int(input("Enter n :"))
list1 = range(2, n)
fibo_list = [0, 1]
any(map(lambda x: fibo_list.append(sum(fibo_list[-2:])), list1))
print(fibo_list)
