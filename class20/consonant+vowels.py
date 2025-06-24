str1 = input("Please Enter Your Own String : ")
vowelscount = 0
consonants = 0
vowels=('a','e','i','o','u','A','E','I','O','U')
for i in str1:
    for vowel in vowels:
        if(i == vowel):
            vowelscount+=1
print("Total Number of Vowels in this String = ", vowelscount)
print("Total Number of Consonants in this String = ", len(str1)-vowelscount)
