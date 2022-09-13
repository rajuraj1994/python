# *args -> when a function parameter start with a asterik, it allows for an arbitary number of arguments and  function takes them in the tuple  of values 

# def myFunction(a,b,c,d,e):
#     return a+b+c+d+e

def myFunction(*args):
    return sum(args)

x=myFunction(10,25,30,50,100)
print(x)