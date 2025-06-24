# yes we can connect lists
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list1 + list2
print(list3)

# Yes we can assign variables to elments in a list
[a,b,c] = [1,2,3]
print(a,b,c)

# Yes we can return multiple values from a list using a function.
def Min_Max(x):
    a = min(x)
    b = max(x)
    return(a,b)

num = [1,65,94,663,848,9494,49499]
(small,big) = Min_Max(num)
print("The smallest number in the tuple is ",small)
print("The biggest number in the tuple is ",big)