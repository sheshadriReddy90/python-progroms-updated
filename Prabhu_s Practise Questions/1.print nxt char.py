string="hello world"
n=string.split()
lis=[]
string_one=""
for i in n:
    string=""
    for j in i:
        string=string+chr(ord(j)+1)
    string_one=string_one+string+" "
    lis=lis+[string]
    
print(lis)
print(string_one)