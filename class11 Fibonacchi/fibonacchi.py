Max_number = 10
num1 = 0
num2 = 1
count = 0
while(count<Max_number):
    print(num1)
    next_number = num1 + num2
    num1,num2 = num2,next_number
    count+=1
