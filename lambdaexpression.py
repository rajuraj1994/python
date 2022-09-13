
def square(num):return num**2

result=square(2)
print(result)

#converting it into lambda expression
cube=lambda xyz: xyz**2

result=cube(3)
print(result)


evenNum= lambda num : num%2==0

numbers=[0,1,2,3,4,5,6,7,8,9,10]
evenlist=list(filter(evenNum,numbers))
print(evenlist)
