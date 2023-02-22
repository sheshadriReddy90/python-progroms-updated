array=input().split()
res=0

for i in array:
    res=res^int(i)
print(res)