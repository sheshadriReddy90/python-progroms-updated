def len_of_list(n):
    if n==[]:
        return 0
    else:
        return 1+len_of_list(n[1:])
n=list(map(int,input().split()))
print(len_of_list(n))