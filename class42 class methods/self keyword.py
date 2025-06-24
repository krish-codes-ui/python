# program to find total and average marks using class

class student:
    s1=89
    s2=83
    s3=13
    s4=84
    s5=48
    s6=56

    def result(self):
        total = student.s1 + student.s2 + student.s3 + student.s4 + student.s5 + student.s6 
        avg=total/6
        print("Total marks is :",total)
        print("Average marks is :",avg)
        return
    
obj1 = student()    
obj1.result()