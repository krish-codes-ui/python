class sample:
    num=0
    
    def __init__(self,var):
        sample.num+=1
        self.var=var
        print("The object value is : ",var)
        print("The value of class variable is : ",sample.num)

    # destructor function

    def __del__(self):
        sample.num-=1
        print("The value of class variable is : ",sample.num)
        print("Object with value %d is exit from the scope " %self.var)
               
s1=sample(4)
s2=sample(8)
s3=sample(938)
s4=sample(9349)
