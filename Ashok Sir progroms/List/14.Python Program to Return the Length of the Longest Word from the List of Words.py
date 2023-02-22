array=list(map(str,input().split()))
lenght=len(array)
maximum=len(array[0])

for i in range(1,lenght):
    if maximum<len(array[i]):
        maximum=len(array[i])
for i in array:
    if maximum==len(i):
        print(i)

