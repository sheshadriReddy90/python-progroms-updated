stones = "aaa"
jewels = "a"
count=0


for i in stones:
   if i in jewels:
       count=count+1
   else:
       break
print(count)