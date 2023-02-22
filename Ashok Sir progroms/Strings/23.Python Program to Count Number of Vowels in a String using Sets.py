string=input()
count=0
vowels=set("aeiou")

for i in string:
    if i in vowels:
        count+=1
print(count)