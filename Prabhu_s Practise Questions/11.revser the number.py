n = 1457
rev = 0
while n > 0: # n = 0 > 0
    rem = n % 10 # rem = 1
    rev = rev * 10 + rem # (754 * 10) + 1 | rev = 7541
    n = n // 10 # n = 0

print(rev) # 7541