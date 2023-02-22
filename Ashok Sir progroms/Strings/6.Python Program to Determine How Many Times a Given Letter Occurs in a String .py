string=input()
char=input()
count=0

for i in string:
    if i==char:
        count+=1
print(char,"presents",count,"times in a string")