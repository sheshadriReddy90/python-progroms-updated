array=list(map(int,input().split()))

array[0],array[-1]=array[-1],array[0]

print(array)