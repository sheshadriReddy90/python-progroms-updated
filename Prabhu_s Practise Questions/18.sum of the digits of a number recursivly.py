def sum_of_the_digits(number):
    if number < 10:
        return number
    else:
        return (number % 10) + sum_of_the_digits( number// 10)    
number = int(input())
result=sum_of_the_digits(number)
print(result)