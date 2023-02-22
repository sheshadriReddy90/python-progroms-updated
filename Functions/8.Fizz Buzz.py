def fizz_buzz(number):
    # Complete this function
     if number % 3==0 and number % 5==0:
        print("FizzBuzz")
     elif number % 3==0:
        print("Fizz")
     elif number % 5 ==0:
        print("Buzz")
   
     else:
        print(number)


number = int(input())
# Call the fizz_buzz function
fizz_buzz(number)