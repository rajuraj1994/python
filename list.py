# list are similar to array in other programming language and list are mutable ie element inside list can be changed

from numpy import append


fruits=['apple','mango','litchi','grapes','papaya']
print(fruits)

#indexing 
print(fruits[0])

#append()-> to add new element in the list
fruits.append('orange')
print(fruits)

#pop() -> remove element from the array, by default it remove the last element and to remove element from specific position use indexing ie pop(0)
fruits.pop()
print(fruits)
fruits.pop(2)
print(fruits)

# len() -> to count number of element in the list
print(len(fruits))




