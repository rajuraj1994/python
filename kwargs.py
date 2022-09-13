# **kwargs -> it builds a dictionary of key/value pairs

def my_function(**kwargs):
    if 'fruit' in kwargs:
        print(f"my favorite fruit is {kwargs['fruit']}")
    else:
        print("not a favourite fruit")

my_function(fruit='apple')