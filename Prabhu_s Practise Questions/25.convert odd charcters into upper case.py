a="hello world"
s=''

for i in range(len(a)):
    if i % 2==1:
        s=s+a[i].upper()
    else:
        s=s+str(a[i])
print(s)