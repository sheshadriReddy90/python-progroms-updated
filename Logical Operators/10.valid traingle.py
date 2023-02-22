first_side =int(input())
second_side =int(input())
third_side =int(input())

res = first_side+second_side > third_side and second_side + third_side > first_side and third_side+first_side>second_side

if res:
    print("True")
else:
    print("False")