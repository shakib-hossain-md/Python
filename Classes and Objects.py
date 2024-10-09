# Create a class

class MyClass:
  x = 5
p1 = MyClass() #Create object
print(p1.x)

# The __init__() function

"""All classes have a function called __init__() which is always executed  when the class object is being initiated."""

class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
p1 = Person("John",36)
print(p1.name)
print(p1.age)

"""The __init__() function is called automatically every time the class is being used to create a new object."""


# The __str__() function
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John",36)
print(p1)


# Object Methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
  