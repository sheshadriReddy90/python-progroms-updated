n=input()
l=len(n)
res=0
for digit in n:
    res= res + (int(digit)**l)
if res==int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")