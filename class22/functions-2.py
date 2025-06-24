#required arguments-are the arguments passed to a function in correct positional order
def printstring(str):
    print("Example-Reqired arguments")
    print(str)
    return
printstring()
#Keyword arguments-will invoke the function after the parameters are recognized by their parameter names
def printdata(name):
    print("Example-1 keyword argument")
    print("Name:",name)
    return
printdata(name="eshan")
#default arguments-will take default value if no value assigned in function call
def printinfo(name,salary=1500):
    print("Name:",name)
    print("Salary:",salary)
    return
printinfo("Mani")
#variable-length argument -if you want to make more arguments than specified
def printos(*nos):
    for n in nos:
        print(n)
    return
print("Printing 2 values")
printos(1,2)
print("Printing 3 values")
printos(10,20,30)
    
