fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
list_a=[]
for value in fruitsDict.values():
    list_a+=[value]
print(max(list_a))
print(min(list_a))