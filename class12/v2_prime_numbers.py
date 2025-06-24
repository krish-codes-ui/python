is_prime = True
input = int(input("Enter the number : "))
for i in range(2,input,1):
    mod = input%i
    if mod == 0:
        is_prime=False
        break 
if is_prime == True:
    print("the number is prime")
else:
    print("the number isn't prime")