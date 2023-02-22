arr = [10, 13, 17, 11, 34, 21,30]
f=0
s=0

for i in range(0,len(arr)):
    if arr[i]>f:
        s=f
        f=arr[i]
    elif arr[i]>s and arr[i]!=f:
        s=arr[i]
print(s)