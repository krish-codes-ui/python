Input = input("Give a string-")
vowels =  ["a", "e", "i", "o", "u"]
for i in Input:
    if i.lower() in vowels:
        print (i, end=' ')


