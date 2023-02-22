n=int(input())
c=0
a=1
b=1
if n==0 or n==1:
    print("fib")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("fib")
    else:
        print("Not an fib")