a=int(input())
b=int(input())

add= a + b
mul= a*b

if len(str(add)) < 3 and len(str(mul)) < 3:
    print("True")
else:
    print("False")