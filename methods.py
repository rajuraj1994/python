# methods are function define inside the body of the class.They are used to perform operations with attribute of our objects.Methods are  a key concept  of OOP paradigm.For large application methods are essential.

class Circle:
    pi=3.14 

    # circle get instantiated with a radius (default 1)
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi
    
    # method for resettting radius 
    def setRadius(self,newradius):
        self.radius=newradius
        self.area = newradius*newradius*self.pi
    
    def getCircumference(self):
        return 2*self.pi*self.radius

        


a=Circle()
print('area is: ',a.area)
a.setRadius(7)
print('radius is: ',a.radius)
print('area is: ',a.area)
print('circumference is : ',a.getCircumference())