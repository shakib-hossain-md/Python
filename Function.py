def my_function():
  print("Hello from a function")

my_function()

# Arguments

def my_function(fname):
  print(fname + "Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Numbers of arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil","Refsnes")


# Arbitary Arguments,*args

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil","Tobias","Linus")

# Keywords Arguments
def my_function(child3,child2,child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2="Tobias",child3="Linus")


# Arbitary keyword arguments

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname="Tobias", lname="Refsnes")


# Default parameter value

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("Bangladesh")
my_function()
my_function("Argentina")


# Passing a list as an argument

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple","banana","cherry"]
my_function(fruits)

# Return values

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass statement
def my_function():
  pass


# Positional-only Arguments

def my_function(x,/):
  print(x)
my_function(3)

""" without the ,/ you are allowed to keyword argument even if the function expects postional arguments"""

def my_function(x):
  print(x)
my_function(x = 3)

# Keyword-inly arguments
def my_function(*,x):
  print(x)
my_function(x=3)

# Combine Positional-only and keyword-only arguments

def my_function(a,b,/,*,c,d):
  print(a+b+c+d)
my_function(5,6,c=7,d=8)


# Function Recursion

def tri_recursion(k):
  if(k>0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)