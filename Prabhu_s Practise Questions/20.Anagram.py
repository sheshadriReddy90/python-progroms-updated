s1=input()
s2=input()
res=[]
for i in s1:
    if i in s2:
        res.append(i)
result="".join(res)
if result==s1 and len(s1)==len(result):
    print("Anagram")
else:
    print("not a anagram")