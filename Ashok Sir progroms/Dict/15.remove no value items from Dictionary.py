mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}

dict_a={key:value for(key,value) in mutidict.items() if value is not None}

print(dict_a)