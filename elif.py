x= 20 

if x<0:
    print('negative number')
elif x>0:
    print('positive number')
else:
    print('the number is zero')

a=int(input('please enter the value of a : '))
b=int(input('please enter the value of b :  '))

if a>b:
    print(a,'is greater')
elif b>a:
    print(f'{b} is greater')
else:
    print(f'{a} and {b} are equal')
    