def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           break
       greater += 1
   return lcm
num1 = int(input("first number for finding lcm-"))
num2 = int(input("second number for finding lcm-"))
print("The LCM. is", lcm(num1, num2))
