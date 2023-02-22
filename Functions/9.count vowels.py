def count_the_vowels(word):
    # Complete this function
    count=0
    for i in word:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count+=1
    print(count)        


word = input()
# Call the count_the_vowels function
count_the_vowels(word)