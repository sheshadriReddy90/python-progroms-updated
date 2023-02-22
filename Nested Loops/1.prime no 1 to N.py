m=int(input()) #7

for i in range(2,m+1): #2 3 4 5 6 7
    factors=0
    for j in range(2,i): #2 3
        if i % j ==0:
            factors+=1
    if factors==0:
        print(i)
        