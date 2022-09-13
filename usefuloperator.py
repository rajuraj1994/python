#min and max 
my_list=[10,12,5,9,22,30,4,8,15]
print(min(my_list))
print(max(my_list))

#random 
from random import shuffle
shuffle(my_list)
print(my_list)

#printing random integer 
from random import randint
print(randint(0,100))

# in operator
demo= 'x' in ['x','y','z','hello']
print(demo)

# not in 
demo_list=['x','y','z','hello']
result= 'y' not in demo_list
print(result)

