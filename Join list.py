#With '+' opertor

list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

#Appending

list1 = ["a","b","c"]
list2 = [1,2,3]
for x in list2:
  list1.append(x)
print(list1)

#Extend

list1 = ["a","b","c"]
list2 = [1,2,3]
list1.extend(list2)
print(list1)