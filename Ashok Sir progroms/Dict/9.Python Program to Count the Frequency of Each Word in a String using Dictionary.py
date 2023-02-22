string=input()
words=string.split()
result={}

for i in words:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
print(result)