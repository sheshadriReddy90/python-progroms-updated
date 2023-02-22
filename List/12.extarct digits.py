string=input()
lst=[]
for i in string:
    if i.isdigit():
        lst+=[int(i)]
res=lst
smallest=res[0]
largest=res[0]

for i in res:
    if i >largest:
        largest=i
    elif i<smallest:
        smallest=i
print(sum(res))
print(smallest)
print(largest)