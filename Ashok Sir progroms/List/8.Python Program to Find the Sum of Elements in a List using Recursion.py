#sum of elements in a list in a natural way

array=list(map(int,input().split()))
result=0

for i in array:
    result+=i
print(result)

#sum of elemnts in a list using recursion
def getSum(element):
    if len(element)==0:
        return 0
    else:
        return element[0] + getSum(element[1:]) 
element=list(map(int,input().split()))
print(getSum(element))