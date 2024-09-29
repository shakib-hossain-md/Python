a = 200
b = 33

if b>a:
  print("b is greater than a")
else:
  print("b is not greater than a")



#Evaluate values and variables

print(bool("Hello"))
print(bool(15))


print(bool("abc"))
print(bool(123))
print(bool(["apple","cherry","banana"]))


class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))


#Function can return Boolean

def myFunction():
  return True
print(myFunction())

#Yon can execute code based on the Boolean answer of a function

def myFunction():
  return True
if myFunction():
  print("Yes!")
else:
  print("No!")


x = 200
print(isinstance(x,int))