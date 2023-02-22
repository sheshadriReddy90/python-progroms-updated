num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
list_a=input().split()

for item in list_a:
    num=int(item)
    num_set.discard(num)
nums_list=list(num_set)
nums_list.sort()
print(nums_list)
