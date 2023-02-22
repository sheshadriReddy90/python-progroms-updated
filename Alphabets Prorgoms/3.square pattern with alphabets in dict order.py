n=int(input())
ascii=65
for i in range(n):
    for j in range(n):
        print(chr(ascii+j),end=' ')
    print()    