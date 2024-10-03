#Remove specified item

thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

#Remove specified index

thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item

thislist = ["apple","banana","cherry"]
thislist.pop()
print(thislist)


#The del keyword also remove the specified index

thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely

thislist = ["apple","banana","cherry"]
del thislist


#Clear the list

thislist = ["apple","banana","cherry"]
thislist.clear()
print(thislist)