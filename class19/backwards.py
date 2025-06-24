string = input("give a word")
lower_string = string.lower()
reversed_string=lower_string[::-1]


if lower_string == reversed_string:
    print(string,"is a palindrome")
else:
    print(string," is not a palindrome")