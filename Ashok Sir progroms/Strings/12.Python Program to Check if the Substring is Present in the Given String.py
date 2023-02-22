string=input()
sub_string=input()
count=0

for i in range(len(string)):
    if sub_string in string[i:i+len(sub_string)]:
        count+=1
print(count)