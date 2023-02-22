lst=list(map(int,input().split()))

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]<lst[j]:  # lst[i]<lst[j]
            lst[i],lst[j]=lst[j],lst[i]
for k in lst:
    print(k)