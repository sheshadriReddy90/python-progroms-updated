string=input()
vowels=['a','e','i','o','u']
result=''
for i in string:
    if i in vowels:
        r=ord(i)+1
        res=chr(r).upper()
        result=result+res
    else:
        result=result+i
print(result)