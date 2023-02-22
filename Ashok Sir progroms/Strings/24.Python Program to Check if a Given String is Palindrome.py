string=input()

rev_str=""

for i in string:
    rev_str=i+rev_str
if string==rev_str:
    print("Palindrome")
else:
    print("Not a palindrome") 