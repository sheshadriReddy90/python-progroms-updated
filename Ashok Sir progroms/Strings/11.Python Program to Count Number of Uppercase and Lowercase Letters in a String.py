string=input()
lower_case_letters=0
upper_case_letters=0

for i in string:
    if 97<=ord(i)<=122:
        lower_case_letters+=1
    else:
        upper_case_letters+=1
print(lower_case_letters)
print(upper_case_letters)
