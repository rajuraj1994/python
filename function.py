# a function is a useful device that groups together a set of statement  so they can be run more than once.They can also let us specify parameters that can be serve as input to the functions.

# basic syntax
#  to define the function
#   def function_name():
#       ..statement...

# call the function
#   function_name()

#defining the function
def demoFunction():
    print('Hello World !')

# call function
demoFunction()

# using return type

#define the function
def add_num():
    return 5+20

# call the function
result=add_num()
print('The addition is ',result)

#argument/parameter

#define function with parameter
def multiply_num(first_value,second_value):
    return first_value*second_value


#function call with argument
total= multiply_num(5,4)
print('the multiplication is : ',total)

total= multiply_num(5,10)
print('the multiplication is : ',total)