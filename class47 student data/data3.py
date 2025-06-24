a = ("----------------------------------------------")
class student:
    # we created a constructor for the student class
    def __init__(self,name,age,m1,m2,Id): 
        self.name = name
        self.age = age  
        self.m1 = m1
        self.m2 = m2
        self.Id = Id

    # adding a student to the data
    def add_student(self,name,age,m1,m2,Id):
        add = student(name,age,m1,m2,Id)
        student_data.append(add)

    # printing one students data
    def print_student(self,add):
        print(add.name)
        print(add.age)
        print(add.m1)
        print(add.m2)
        print(add.Id)
        print()
    
    # Searching a student with the id
    def Search_student(self,search_id):
        for x in range(student_data.__len__()):
            if student_data[x].Id == search_id:
                return x 

    def Delete_student(self,del_student):
        i = st.Search_student(del_student)
        del student_data[i]

student_data = []
    
while 3>0:
    st = student("harold",23,49,97,234)

    option = int(input("""Pick the number of the option you want
                          Option 1 can print a students data, 
                          Option 2 can add a student to the data, 
                          Option 3 can search and print a students data with the roll number
                          Option 4 can delete a student from the database
"""))

    if option == 1:  # Option 1 can print a students data
        print(a)
        for i in range(student_data.__len__()):
            st.print_student(student_data[i])
        print(a)
    elif option == 2:   # Option 2 can add a student to the data
        print(a)
        sname = input("Enter name : ")
        age = input("Enter age : ")                               
        m1 = input("Enter grade 1 : ")
        m2 = input("Enter grade 2 : ")
        Id = input("Enter roll number : ")
        st.add_student(sname,age,m1,m2,Id)
        print(a)
    elif option == 3:   # Option 3 can search and print a students data with the roll number
        print(a)
        search_id = input("Give Id to search for student : ")
        roll_no = st.Search_student(search_id)
        st.print_student(student_data[roll_no])
        print(a)
    elif option == 4:   # Option 4 can delete a student from the database
        print(a)
        del_student = input("Give the Id for the student you want to delete : ")
        for x in range(student_data.__len__()):
            st.print_student(student_data[x])  
        print(a)
    else:   # If the user didn't pick one of the options

        print("You didn't pick 1??,2??? or 3????  or 4????????")
        break
