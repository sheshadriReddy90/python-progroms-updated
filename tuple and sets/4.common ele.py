def converting_string_to_int(num_list):
    new_list=[]
    for item in num_list:
        num=int(item)
        new_list.append(num)
    return new_list
    
    
list_a=input().split(",")
list_b=input().split(",")   

list_a=converting_string_to_int(list_a)
list_b=converting_string_to_int(list_b)

set_a=set(list_a)
set_b=set(list_b)

result_set=set_a.intersection(set_b)
result_list=list(result_set)
result_list.sort()
print(result_list)