n=int(input())

for i in range(n):
    print("  "*i+(str(i+1)+' '),end='')

    if i!=(n-1):
        print("  "*(2*n-2*i-3)+(str(i+1)),end='')
    print()