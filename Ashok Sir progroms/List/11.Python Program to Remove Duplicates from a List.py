array=list(map(int,input().split()))

lst=[]

for i in array:
    if i not in lst:
        lst.append(i)
print(lst)