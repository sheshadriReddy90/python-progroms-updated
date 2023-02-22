array=list(map(int,input().split()))
first_max=array[0]
second_max=array[0]

for i in range(len(array)):
    if array[i]>first_max:
        second_max=first_max
        first_max=array[i]
    elif array[i]>second_max and array[i]!=first_max:
        second_max=array[i]
print(second_max)