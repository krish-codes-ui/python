# returning multiple values from a tuple using a function

def Min_Max(x):
    a = min(x)
    b = max(x)
    return(a,b)

num = (1,65,94,663,848,9494,49499)
(small,big) = Min_Max(num)
print("The smallest number in the tuple is ",small)
print("The biggest number in the tuple is ",big)