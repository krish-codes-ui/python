numbers = [1,2,5,3,4,5]

#define a function to be used later
def double(x):
    return x*2

#use map() to apply the function to each element in the list
doubled_numbers = list(map(double,numbers))
doubled_numberss = set(map(double,numbers))


print("The original numbers are : ",numbers)
print("The doubled numbers are : ",doubled_numbers)
print("The doubled numbers as a set are : ",doubled_numberss)