n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
for i in range(1,n):
    for k in range(0,(n-i)):
        print((n-i),end=' ')
    print() 