is_prime = True
input = 291
middle_number=int((input/2)//1)
for i in range(2,middle_number,1):
    mod = input%i
    if mod == 0:
        is_prime=False
        break
  
if is_prime == True:
    print("the number is prime")
else:
    print("the number isn't prime")