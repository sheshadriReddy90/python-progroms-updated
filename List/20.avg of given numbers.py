n=input().split()
length=len(n)
res=0

for i in n:
    res+=int(i)
avg=res / length
print(round(avg,2))
    