string_1=input()
string_2=input()

result=list(set(string_1)^set(string_2))

for i in result:
    print(i,end='')