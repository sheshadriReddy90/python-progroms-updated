n=input()
length=len(n)
total=0
for digit in n:
    total=total + (int(digit) ** length)
if total==int(n):
    print("True")
else:
    print("False")