'''
my_list=[[1],[2,3],[4,5,6,7]]

flatten_list=[num for sublist in my_list for num in sublist ]

print(flatten_list)
'''
my_list=[[1],[2,3],[4,5,6,7]]
lst=[]
for i in my_list:
    for j in i:
        lst.append(j)
print(lst)
