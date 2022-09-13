# the filter function returns an iterator yielding  those items of iterable for which function(item) is true.That means you need to filter by a function that returns either True or False

# defining the function
def check_even(num):
    return num%2==0


nums=[0,1,2,3,4,5,6,7,8,9,10]
#newlist=filter(check_even,nums)
newlist=list(filter(check_even,nums))
print(newlist)

