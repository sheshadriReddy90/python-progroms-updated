n=int(input())

for i in range(n):
    print(" "*i,end='')
    for j in range(0,(n-i)):
        print(chr(64+n-j),end=' ')
    print()