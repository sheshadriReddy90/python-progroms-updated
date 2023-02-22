n=int(input())

for i in range(n):
    print("  "*(n-i-1)+(str(i+1)+" "),end='')

    if i>=1:
        print("  "*(2*i-1)+(str(i+1)),end='')
    print()