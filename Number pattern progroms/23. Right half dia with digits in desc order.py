n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print((n-j),end=' ')
    print()

for i in range(1,n):
    for k in range(0,(n-i)):
        print((n-k),end=' ')
    print() 