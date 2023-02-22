lst=list(map(str,input().split()))
max_len=0
max_str=""
for i in lst:
    if len(i)>max_len:
        max_len=len(i)
        max_str=i
print(max_str)
