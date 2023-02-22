for row in range(7):
    for col in range(5):
        if row==0 and col in {0,1,2,3,4}:
            print("*",end=' ')
        elif row in{0,1,2,3,4,5,6} and col==2:
            print("*",end=' ')
        elif row in {5,6} and col in {0}:
            print("*",end=' ')
        elif row==6 and col==1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()