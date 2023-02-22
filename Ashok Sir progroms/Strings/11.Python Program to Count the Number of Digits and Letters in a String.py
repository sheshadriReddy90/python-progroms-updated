string=input()
digits=0
letters=0

for i in string:
    if i.isdigit():
        digits+=1
    else:
        letters+=1
print(digits)
print(letters)
