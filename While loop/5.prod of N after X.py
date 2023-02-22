x=int(input())
n=int(input())
product=1
for i in range(1,n+1):
    res=x+i
    product*=res
print(product)