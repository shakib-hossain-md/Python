thisdict = {
  "brand" : "Ford",
  "model" : "Mustung",
  "year" : 1964,
  "year" : 2020,
  "colours" : ["Red","Black","Blue","White"]

}
print(thisdict)
print(thisdict["brand"])

# Ordered,changeable,don't allow duplicates
# Duplicate value overwrite the existing value

print(thisdict)

# Dictionaries can be of any data type

thisdict = {
  "brand" : "Ford",
  "model" : "Mustung",
  "year" : 1964,
  "year" : 2020,
  "electric" : False,
  "colours" : ["Red","Black","Blue","White"]

}
print(thisdict)

# Can also use dict() constructor to make dictionaries

thisdict = dict(name = "Sakib", age = 23, country = "Bangladesh")
print(thisdict)