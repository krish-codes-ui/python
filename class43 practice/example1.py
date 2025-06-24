class Circle:
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * self.radius**2
    
    def circumference(self):
        return 2*Circle.pi*self.radius
    
radius = int(input("Enter the radius of the circle : "))

# create a circle object
circle = Circle(radius)

# calculate and print the area and circumference
print("The area of your circle is : ",circle.area())
print("The circumference of your circle is : ",circle.circumference())