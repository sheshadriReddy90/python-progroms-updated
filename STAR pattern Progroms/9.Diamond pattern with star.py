n=int(input())

for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(1,i+1):
        print("*",end=' ')
    print()
for j in range(1,n+1):
    print(" "*j,end='')
    for k in range(1,(n-j)+1):
        print("*",end=' ')
    print()  