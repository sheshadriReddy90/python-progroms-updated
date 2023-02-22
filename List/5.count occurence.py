nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100, 20, 20]
# Write your code here
n=int(input())
c=0

for i in nums_list:
    if i==n:
        c+=1
print(c)