n=int(input())

for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()
for x in range(1,n):
    print(" "*x,end='')
    for k in range(1,(n-x)+1):
        print(chr(64+n-k),end=' ')
    print()