array=list(map(int,input().split()))
result=0
length=len(array)
for i in array:
    result+=i
res=result//length

print(res)
