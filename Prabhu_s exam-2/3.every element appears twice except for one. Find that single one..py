lst=[4,1,2,1,2]
new_lst=[]

for i in lst:
    if i not in new_lst:
        new_lst.append(i)
    else:
        new_lst.remove(i)
print(new_lst[0])
