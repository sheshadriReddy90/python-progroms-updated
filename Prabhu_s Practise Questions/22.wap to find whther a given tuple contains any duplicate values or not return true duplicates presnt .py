tuple_one=(1,2,2,2,3,4,3,4,5)
tup=()
for i in tuple_one:
    if i not in tup:
        tup=tup+(i,)
if len(tuple_one)==len(tup):
    print(True)
else:
    print(False)