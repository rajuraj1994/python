

def square(nums):
    return nums**2

numbers=[2,4,6,8,10]
# testresult=map(square,numbers)
testresult=list(map(square,numbers))
print(testresult)

def splice(mynames):
    if len(mynames)%2==0:
        return mynames
    else:
        return ('Odd',mynames[0])


names=['Yogesh','Yanzi','Ganesh','Shiva','Rojust','Sachin']
newlist=list(map(splice,names))
print(newlist)


