# Accesing values using keys
Dict = {'Address':'12387 spanish trace drive',
        'Phone number':'7038687122',
        'Name':'Krish',
        'School':'parkway north east',
        'Registration number':12986}

print(Dict)
print("The Adress is: ",Dict['Address'])
print("The Phone number is: ",Dict['Phone number'])
print("The Name is: ",Dict['Name'])
print("The School is: ",Dict['School'])
print("The Reg. number is: ",Dict['Registration number'])

# Dictionary comprehensions

cubes = {num:num*num*num for num in range(1,11,1) }
print(cubes)