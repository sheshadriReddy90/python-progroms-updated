n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=' ')
    print()
    
for i in range(1,n):
    for k in range(0,(n-i)):
        print(chr(64+n-i),end=' ')
    print()     