arr = [1, 2, 3, 1, 10]
res = {}
for i in arr: 
    if i in res:
        res[i] = res[i] + 1
    else:
        res[i] = 1
for key, value in res.items():
    print(key, 'is present for', value, 'times')