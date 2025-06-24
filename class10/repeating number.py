a = (3,7,5,6,3,9,2,3,6,5,9,2,3,7,9,6,2)
b = int(input("what number should i find"))
count=0
for x in a:
    if x == b:
        count = count+1
print(b," repeated ",count,"times")