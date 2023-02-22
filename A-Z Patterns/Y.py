for row in range(5):
    for col in range(5):
        if row==0 and col in {0,4}:
            print("*",end=' ')
        elif row==1 and col in {1,3}:
            print('*',end=' ')
        elif row in {2,3,4} and col==2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()