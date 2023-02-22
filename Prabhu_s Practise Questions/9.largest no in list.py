n=input().split()
largest=int(n[0])

for i in n:
    if int(i)>largest:
        largest=int(i)
print(largest)  