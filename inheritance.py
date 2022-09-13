#inheritance is to form a new classes from the classes that have been already defined.The newly formed classes are called derived class, the class that we derive from are called base class.The derive class override or extend the functionality of base class.

class Animal:
    def __init__(self):
        print('Animal class created')
    
    def WhoIs(self):
        print('Animal')
    def eat(self):
        print('Animal Who Eats')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog  class created')
    
    def WhoIs(self):
        print('Animal type of Dog')
    
    def speak(self):
        print('dog is barking')


a=Animal()
print(a)
a.WhoIs()

b= Dog()
print(b)
b.WhoIs()
b.eat()
b.speak()

