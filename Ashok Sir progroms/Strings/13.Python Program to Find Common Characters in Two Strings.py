
string_1=input()
string_2=input()

common=[]

for i in string_1:
    for j in string_2:
        if i==j:
            common.append(i)
print(set(common))



print(set(string_1).intersection(set(string_2)))