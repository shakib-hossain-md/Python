#Append items

thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

#Extend list

thislist = ["apple","banana","cherry"]
tropical = ["kiwi","blackcurrant"]
thislist.extend(tropical)
print(thislist)

#Add any iterable

thislist = ["apple","banana","cherry"]
thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)