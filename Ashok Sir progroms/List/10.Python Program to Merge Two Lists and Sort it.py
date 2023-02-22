array1=list(map(int,input().split()))
array2=list(map(int,input().split()))

merge_two_arrays=array1 + array2

for i in range(len(merge_two_arrays)):
    for j in range(len(merge_two_arrays)):
        if merge_two_arrays[i]<merge_two_arrays[j]:
            merge_two_arrays[i],merge_two_arrays[j]=merge_two_arrays[j],merge_two_arrays[i]
print(merge_two_arrays)
