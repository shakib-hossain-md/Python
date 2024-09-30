thislist = ["apple","banana","cherry"]
print(thislist)

# Allows Duplicate
thislist = ["apple","banana","apple","cherry",]
print(thislist)

#List Length

thislist = ["apple","banana","apple","cherry",]
print(len(thislist))

#List Items- Data Types

list1 = ["apple","banana","cherry"]
list2 = [1,3,5,9,11]
list3 = [True,False,False]

print(list1)
print(list2)
print(list3)

#A list can conatin different data types

list1 = ["apple",1,True,12,"banana"]
print(list1)

print(type(list1)) 


#The list() constructor

thislist = list(("apple","banana","cherry"))
print(thislist)