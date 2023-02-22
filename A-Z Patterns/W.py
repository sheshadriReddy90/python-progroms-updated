for row in range(4):
    for col in range(7):
        if row==0 and col in {0,3,6}:
            print('*',end=' ')
        elif row==1 and col in {0,2,4,6}:
            print('*',end=' ')
        elif row==2 and col in {0,1,4,6}:
            print("*",end=' ')
        elif row==3 and col in {0,6}:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()