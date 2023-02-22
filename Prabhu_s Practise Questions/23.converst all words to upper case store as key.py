keys = ['hi','happy','new','year']
res1=[]
res=[]
for i in keys:
    l=len(i)
    res.append(l)
    r=i.upper()
    res1.append(r)
    
dict1=dict(zip(res1,res))
print(dict1)