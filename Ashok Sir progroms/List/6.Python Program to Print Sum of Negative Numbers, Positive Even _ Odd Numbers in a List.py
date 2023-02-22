array=list(map(int,input().split()))

even_num=[]
odd_num=[]
negative_num=[]

for i in array:
     if i < 0:
        negative_num.append(i)
     elif i  % 2==0:
        even_num.append(i)
     else:
        odd_num.append(i)
print(negative_num,sum(negative_num))
print(odd_num,sum(odd_num))
print(even_num,sum(even_num))