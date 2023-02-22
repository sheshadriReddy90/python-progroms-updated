arr = "aabbccdd"
res=[]
for i in arr:
    if i not in res:
        res.append(i)
print("".join(res))