class sample:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.__n2 = n2

    def display(self):
        print("Variable 1 : ",self.n1)
        print("Variable 2 : ",self.__n2)

S = sample(15,59)
S.display()

print("Value 1 : ",S.n1)
print("Value 2 : ",S.__n2)