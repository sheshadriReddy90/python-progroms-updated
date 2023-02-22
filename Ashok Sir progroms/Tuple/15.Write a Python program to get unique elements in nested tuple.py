tuple_a=[(1, 3, 5), (4, 5, 7), (1, 2, 6), (10, 9), (10,)]

list_a=[]

for i in tuple_a:
    for j in i:
        list_a.append(j)
print(list_a)
print(set(list_a))