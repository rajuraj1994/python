#loop -> iteration/repeatation

mylist=[2,5,9,7,12,15,18,20]

for num in mylist:
    print(num)

# print only even number
for num in mylist:
    if num%2==0:
        print(num)

# calculate total sum
total_sum=0
for num in mylist:
    total_sum+=num 
print(total_sum)

text="high level programming language"
for letter in text:
    print(letter)
    




