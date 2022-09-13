# the general format of the while loop
# while test/condtion
#  code statement
# else
#   final code statement 

x=0
while x<20:
    print('x is currently:',x)
    x+=1
else:
    print(x)

#continue
y=1
while y<10:
    print('y is currently: ',y)
    print('y is still less than 10, adding 1 to y')
    y+=1

    if y==5:
        print('y==5')
    else:
        print('continuing')
        continue

#break and continue
y=1
while y<10:
    print('y is currently: ',y)
    print('y is still less than 10, adding 1 to y')
    y+=1

    if y==5:
        print('break when y==5')
        break
    else:
        print('continuing')
        continue
