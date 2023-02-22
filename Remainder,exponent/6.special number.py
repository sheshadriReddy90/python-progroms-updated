number=int(input())
remainder= number % 7
is_div_by_7=(remainder==0)
number=str(number)
first_digit=int(number[0])
second_digit=int(number[1])
is_any_digit_7= (first_digit==7) or (second_digit==7)
sum_of_two_digits=(first_digit + second_digit)
is_sum_equal_7= (sum_of_two_digits==7)
is_spl_no= is_div_by_7 or is_any_digit_7 or is_sum_equal_7
if is_spl_no:
     print("Special Number")
else:
    print("Normal Number")
 