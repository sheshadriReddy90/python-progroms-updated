s=input()
rev_str=""
for char in s:
    rev_str=char+rev_str
    if s==rev_str:
        print("paindrome")
    else:
        print("not a palidrome")