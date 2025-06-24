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
Dict['class'] = '6'
print("The class is: ",Dict['class'])
print("The School is: ",Dict['School'])
print("The Reg. number is: ",Dict['Registration number'])

for key,value in Dict.items():
    print(f"{key}:{value}")


# Deleting a paticular element in dictionary
del Dict['Name']
print(Dict)

# Deleting all elements

Dict.clear()
print(Dict)

# Deleting entire dictionary

del Dict

