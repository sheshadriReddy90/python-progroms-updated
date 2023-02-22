num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
number=int(input())
new_list=[]
for tuple_a in num_list:
    update_tuple=tuple_a[:-1] +(number,)
    new_list.append(update_tuple)
print(new_list)    