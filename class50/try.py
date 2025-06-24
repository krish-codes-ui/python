def safe_divide(a,b):
    try:
        c = a//b
        print(c)
    except ZeroDivisionError:
        print("Nothing is divisible by 0")
a = int(input("What do you want the dividend to be? :"))
b = int(input("What do you want the divisor to be? : "))
safe_divide(a,b)