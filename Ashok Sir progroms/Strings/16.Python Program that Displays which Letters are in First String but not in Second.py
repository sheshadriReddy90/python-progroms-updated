string_1=input()
string_2=input()
arr=[]
for i in string_1:
    if i not in string_2:
        arr.append(i)
print(arr)
