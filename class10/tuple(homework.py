a=(6,8,9)
b=(6,7,4,8,)
result = [x
       for x in a
            for y in b if x == y]
print(result)