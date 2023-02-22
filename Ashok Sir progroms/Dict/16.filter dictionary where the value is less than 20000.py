empdict = {'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}

dict_a=dict()

for (key,value) in empdict.items():
    if value<20000:
        dict_a[key]=value
print(dict_a)