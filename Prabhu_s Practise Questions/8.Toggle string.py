w=input()
s=''
for i in w:
    if i.upper()==i:
        i=i.lower()
        s=s+i
    else:
        i=i.upper()
        s=s+i
print(s)