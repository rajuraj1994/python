# The syntax for creting an attribute is 

# self.attribute=something

# there is a special method called:
# __init__()

class Dog:
    def __init__(self,breed):
        self.breed= breed

x=Dog(breed='German')
print(x)

# __init__() : this is a special method which is called automatically right after  an object has been created 

# def __init__(self,breed)
# each attribute in a class defination begins with a reference to the instance of object. By convention named self.The breed is a argument.The value is passed during class instantation. self.breed=breed 

# we created instance of Dog class and we can access the these attribute from class like this

print(x.breed)



