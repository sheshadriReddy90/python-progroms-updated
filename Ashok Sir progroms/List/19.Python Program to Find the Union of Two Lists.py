array_1=list(map(int,input().split()))
array_2=list(map(int,input().split()))

set_1=set(array_1)
set_2=set(array_2)

print(set_1.union(set_2))