prime_points = 0
is_prime = False
is_even = False

num = int(input("Enter number to check if it's prime and odd or even: "))
for num1 in range(1,100):
    if num%num1 == 0:
        prime_points+=1
    else:
        prime_points+=0

if prime_points >=3: 
    is_prime = False
else: 
    is_prime = True

if num%2 == 0:
    is_even = True
else:
    is_even = False

print(f"{num} is a prime number : {is_prime}"  " -- "  
        f"{num} is a even number : {is_even}")




