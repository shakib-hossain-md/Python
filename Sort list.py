#Sort list Alphanumerically (ascending by default)
#Sort the list alphabetically

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist.sort()
print(thislist)

#Sort list numerically

thislist = [100,50,65,82,23]
thislist.sort()
print(thislist)

#Sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

#Numerical descending 

thislist = [100,50,65,82,23]
thislist.sort(reverse=True)
print(thislist)

#Customize sort function
#Sort the list based on how close the number is to 50

def myfunc(n):
  return(n-50)
thislist = [100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)

#Case In-sensitive sort
#By default the sort() method is case sensitive

thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort()
print(thislist)

"""So if you want a case in-sensitive sort function, use str.lower as key function"""

thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort(key=str.lower)
print(thislist)

#Reverse order

thislist = ["banana","Orange","Kiwi","cherry"]
thislist.reverse()
print(thislist)