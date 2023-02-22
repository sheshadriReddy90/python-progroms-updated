n_list=list(map(int,input().split()))

new_list=[]

for i in n_list:
    if i not in new_list:
        new_list.append(i)
new_list.sort()
print(new_list)