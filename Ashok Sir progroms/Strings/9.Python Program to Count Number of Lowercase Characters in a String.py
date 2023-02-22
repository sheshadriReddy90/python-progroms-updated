string=input()
count=0

for i in string:
    if 97<=ord(i)<=122:
        count+=1
print("The number of lowercase letters present in string are",count)