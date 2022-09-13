# in python everything is an objects ie we use type() methods to check the type of objects 

print(type(20))
print(type([1,2,3,4,5]))

# to create own objects use class keyword 

# class : User defined objects are created using class keyword.The class is a blueprint that defines the nature of future objects. From classes can construct instances. An instance is a specific object created from the particular class.For example,above we created the object list which was an instance of list object.

# let create new object type called Demo
class Demo:
    pass
# instance of Demo
x=Demo()
print(type(x))

# Inside class we currently have onle pass but we can  define class attributes and methods.

#attribute : it is a characteristics of of an object
#method : it is an operation we can  perform with the object 

# Example: we can create a class called Dog. An attribute of a  dog may be  its breed or its name, while a method of a dog  may be defined by .bark() method which returns the sound.



