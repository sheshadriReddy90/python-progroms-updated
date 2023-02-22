def getSum(ele):
    if len(ele)==0:
        return 0
    else:
        return ele[0] + getSum(ele[1:]) 
print(getSum([1, 3, 4, 2, 5]))