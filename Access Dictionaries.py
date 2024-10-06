thisdict = {
  "brand" : "Ford",
  "model" : "Mustung",
  "year" : 1964,
  "colours" : ["Red","Black","Blue","White"]

}
x = thisdict.get("model")
print(x)

# Add a new item

x = thisdict.keys()
print(x)
thisdict["electric"] = False
print(x)

x = thisdict.values()
print(x)

# Check if key exists 

if "Mustung" in x:
  print("Yes, 'Mustung' is in the Dictionary.")