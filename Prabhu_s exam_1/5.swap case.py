string="HellO WorLd"
s=''
for i in string:
    if i.upper()==i:
        i=i.lower()
        s=s+i
    else:
        i=i.upper()
        s=s+i
print(s)