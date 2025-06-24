# lambda [arguments]:expression
sum = lambda arg1,arg2: arg1+arg2
a = int(input("give first number"))
b = int(input("give second number"))
print("The sum is: ",sum(a,b) )

# return[expression list]

def sub(x,y):
    q=x-y
    return q
a = int(input("give first number"))
b = int(input("give second number"))
print(sub(a,b))


def mul(x,y):
    q=x*y
a = int(input("give first number"))
b = int(input("give second number"))
print(mul(a,b))


