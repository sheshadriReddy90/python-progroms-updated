lst=input().split(",")
largest=int(lst[0])

for i in lst:
    if int(i) > int(largest):
        largest=i
print(largest)        