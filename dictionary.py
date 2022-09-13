# dictionary are known as objects in other programming language and they always comes in key value pair

student={"first_name":"shiva","last_name":"limbu","age":22,"height":5.6}
print(student['first_name'])

item={"value1":15,"value2":[2,5,7,11],"value3":[10,20,30]}
print(item["value2"])

#create a new dictionary
d={}
d['fruit']='apple' # value assign in d
d['vegetable']='potato'
print(d)

#nesting with dictionary
nest_dict={'key1':{'nestkey':{'subnestkey':'finalValue'}}}
print(nest_dict["key1"]["nestkey"]["subnestkey"])

# dictionary methods
#keys() -> it only print the key of the dictionary

print(student.keys())

#values() -> it only print all the value of the dictionary
print(student.values())


