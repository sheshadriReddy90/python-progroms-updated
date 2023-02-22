dict_a={1:"a",2:"b",3:"c",4:"d"}
key=int(input())

if key in dict_a.keys():
    print(dict_a[key])
else:
    print("key is not present in a dict")