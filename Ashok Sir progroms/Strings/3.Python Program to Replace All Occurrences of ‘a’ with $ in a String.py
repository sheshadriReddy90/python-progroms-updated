string=input()
char=input()

for i in string:
    if i==char:
        result=string.replace(i,"$")
print(result)