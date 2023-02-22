S=input()
first_three_char = S[0:3]
equal_s=first_three_char=="NXT"
l=len(S)
l1=l-3
remaining_char= S[-l1:]
convert=int(remaining_char)
div_2= convert % 2==0
div_7 = convert % 7==0
res=div_2 or div_7
if res and equal_s:
    print("Special String")
else:
    print("Not a Special String")