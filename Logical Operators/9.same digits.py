n=input()

first_digit = int(n[0])
second_digit=int(n[1])
third_digit = int(n[2])

all_digits_are_same = first_digit == second_digit and second_digit == third_digit

print(all_digits_are_same)