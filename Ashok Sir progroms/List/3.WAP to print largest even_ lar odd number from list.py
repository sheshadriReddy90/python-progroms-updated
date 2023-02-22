array=list(map(int,input().split()))

even_num=[]
odd_num=[]

for i in array:
    if i% 2 ==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(max(even_num))
print(max(odd_num))