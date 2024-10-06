myfamily = {
  "child1" :{
    "name" : "John",
    "age" : 20
  },
  "child2" :{
    "name" : "Mike",
    "age" : 25
  },
  "child3" : "Mathew",
  "age" : 30
}
print(myfamily)

print(myfamily["child2"]["name"])

# Multiple dictionary in one dictionary


child1 = {
    "name" : "John",
    "age" : 20
  }
child2 = {
    "name" : "Mike",
    "age" : 25
  }
child3 = {
  "name" : "Mathew",
  "age" : 30
}
myfamily1 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily1)

# Loop through nasted dictionary

for x, obj in myfamily1.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])