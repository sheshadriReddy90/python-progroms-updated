n=int(input())

for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(0,i):
        print(chr(64+n-j),end=' ')
    print()

for x in range(1,n):
    print(" "*x,end='')
    for k in range(0,(n-x)):
        print(chr(64+n-k),end=' ')
    print()