n=int(input())

for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(0,i):
        print((n-j),end=' ')
    print()
for j in range(1,n+1):
    print(" "*j,end='')
    for k in range(0,(n-j)):
        print((n-k),end=' ')
    print()