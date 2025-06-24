class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def print_name(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.dob = 1998
    
Obj1 = student("Joe","Biden")
Obj1.print_name()
print(Obj1.dob)

Obj2 = person("Bill","Clinton")
Obj2.print_name()
print(Obj2.dob)