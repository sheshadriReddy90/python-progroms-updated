for row in range(7):
    for col in range(5):
        if row in {0,3,6} and col in {1,2,3,4}:
            print("*",end=' ')
        elif col==0 and row in {1,2,3,4,5}:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()