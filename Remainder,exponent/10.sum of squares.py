A=int(input())
B=int(input())
sum_of_square = A**2 + B**2
greater_than_60 = sum_of_square >=60

if greater_than_60:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")