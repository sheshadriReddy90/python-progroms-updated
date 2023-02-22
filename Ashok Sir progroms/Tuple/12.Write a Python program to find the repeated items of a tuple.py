tuple_a=(1,2,3,4,5,1,2)

list_a=[]

for ele in tuple_a:
    if tuple_a.count(ele)>1:
        if ele not in list_a:
            list_a.append(ele)
print(list_a)