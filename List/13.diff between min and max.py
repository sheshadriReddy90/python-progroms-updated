lst=input().split(",")
largest=int(lst[0])
smallest=int(lst[0])

for i in lst:
    if int(i)>largest:
        largest=int(i)
    elif int(i)<smallest:
        smallest=int(i)
    else:
        pass
        
print(largest-(smallest))        