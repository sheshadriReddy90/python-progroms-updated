n=int(input())
c=0
for i in range(1,n+1):
    I=i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%8==0 or i%9==0 or i%10==0
    if not I:
        c+=1
print(c)        