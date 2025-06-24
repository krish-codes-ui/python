class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def print_name(self):
        print(self.firstname,self.lastname)

class student(person):
    pass

Obj1 = person("John","Doe")
Obj1.print_name()

Obj2 = student("Christopher","Colombus")
Obj2.print_name()