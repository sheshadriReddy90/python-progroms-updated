n=int(input())
keys=[]
values=[]

for i in range(n):
    ele=int(input())
    keys.append(ele)
for j in range(n):
    ele_1=int(input())
    values.append(ele_1)
dict_a=dict(zip(keys,values))
print(dict_a)