n=int(input())

for i in range(1,n+1):
    print(" "*(n-i)+(chr(64+i)+" ")*i)