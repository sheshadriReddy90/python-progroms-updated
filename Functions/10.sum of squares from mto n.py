def sum_of_squares_m_to_n(m, n):
    # Complete this function
    res=0
    for i in range(m,n+1):
        square=i*i
        res+=square
    print(res)


m = int(input())
n = int(input())
# Call the sum_of_squares_m_to_n function
sum_of_squares_m_to_n(m,n)