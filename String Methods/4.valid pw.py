string=input()

is_digit=False
for i in string:
    contains_digit=i.isdigit()
    if contains_digit:
        is_digit=True
        
if is_digit:
    print("Valid Password")
else:
    print("Invalid Password")
    
    
    
    
        
 