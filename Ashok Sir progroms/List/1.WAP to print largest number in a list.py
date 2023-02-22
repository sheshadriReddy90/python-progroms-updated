array=list(map(int,input().split()))
maximum_element=array[0]

for i in range(1,len(array)):
    if array[i]>maximum_element:
        maximum_element=array[i]
print(maximum_element)

