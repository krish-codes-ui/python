def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num=int(input("pick a number"))
print(check_odd_even(num))  
