a=int(input())
b=int(input())
if a>b:
    greatest_num=b
else:
    greatest_num=a
lcm_found=False
for number in range( greatest_num , (a*b+1)):
    if not lcm_found:
        if((number%a)==0) and((number%b)==0):
            lcm_found=True
            lcm=number
print(lcm)            
            
    
    
    
    