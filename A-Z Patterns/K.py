for row in range(7):
    for col in range(5):
        if col==0 and row in {0,1,2,3,4,5,6}:
            print('*',end=' ')
        elif row==0 and col==4:
            print("*",end=' ')
        elif  row==1 and col==3:
            print("*",end=' ')
        elif  row==2 and col==2:
            print("*",end=' ')
        elif row==3 and col==1:
            print("*",end=' ')
        elif row==4 and col==2:
            print("*",end=' ')
        elif row==5 and col==3:
            print("*",end=' ')
        elif row==6 and col==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()