for row in range(7):
    for col in range(5):
        if col in {0,4} and row in {1,2,4,5,6}:
            print("*",end=" ")
        elif row==3 and col in {0,1,2,3,4}:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()