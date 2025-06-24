prime_points = 0
num = int(input("Enter number to check if it's prime: "))
for num1 in range(1,100):
    if num%num1 == 0:
        prime_points+=1
    else:
        prime_points+=0
if prime_points >=3: 
    print("your number is not prime")
else: 
    print("your number is prime")
