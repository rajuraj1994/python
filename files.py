my_file=open('test.txt')
print(my_file)

print(my_file.read())

my_file.seek(5)
print(my_file.read())

#readlines return a list of the lines in the file 
my_file.seek(0)
print(my_file.readlines())

#\n -> next line 

#writing to a file 
# open()->opening the file
# passing w+ let us read and write to the file
# open('test.txt','w+') -> this will truncate the original ie it will delete all the content exist previously in the file 

my_file=open('test.txt','w+')
print(my_file)

my_file.write('this is the first line write from the file method')
my_file.seek(0)
print(my_file.read())
my_file.write('\nthis is the second line of the file added')
my_file.seek(0)
print(my_file.read())

#appending to the file 
newfile=open('hello.txt','a+')
print(newfile)
newfile.write('this is added from append method')
newfile.seek(0)
print(newfile.read())

newfile.close()

