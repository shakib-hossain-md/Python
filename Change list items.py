#Change second item of the list

thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the range of Item values

"""Change the values "banana" and "cherry" with the values "blackcurrant" and watermelon """

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

#Chnage the second and third value by replacing it with one value

thislist = ["apple","banana","cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items

#Insert "watermelon" as the third item

thislist = ["apple","banana","cherry"]
thislist.insert(2,"watermelon")
print(thislist)