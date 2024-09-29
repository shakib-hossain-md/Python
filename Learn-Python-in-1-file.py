# This hash sign in for commenting in codes

''' This is 
multiline comment '''

'''
 Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, 
the indentation in Python is very important.
'''


  # Printing
''' 
print("Hi Universe") # For string use cotation 
print(2**3)  
'''

  # Variables
'''
 Python has no command for declaring a variable.

Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
-A variable name must start with a letter or the underscore character
-A variable name cannot start with a number
-A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
-Variable names are case-sensitive (age, Age and AGE are three different variables)
-A variable name cannot be any of the Python keywords.
'''

'''
x = 5        # x is of type int
y = "John"   # x is now of type str
print(x)
print(y)
'''

  # There are three numeric types in Python:
'''
x = 3   # int
y = 3.8 # float
z = 3j  # complex
'''

# type casting (There may be times when you want to specify a type on to a variable. This can be done with casting.)
'''
x = str(3)    # x will be '3'
print(x)
y = int(3.8)    # y will be 3
print(y)
z = float(3)  # z will be 3.0
print(z)
'''

  # String

'''
x="hello"  # In double quotes is string
y=' world' # In single quotes is also 
z=""" I am 
a programmer
"""        # In triple quotes multiline string
a="joy"
print(x+y)
print(z)
print(len(a)) # The len() function returns the length of a string

txt = 'I am a student'
print('I' in txt) # in for presence of string
'''

# Specify the start index and the end index, separated by a colon, to return a part of the string.

'''
b = "Hello, World!"
print(b[2:5])
'''

# Modify Strings

'''
a = "I am a programmer"
print(a.upper())
print(a.lower())
print(a.replace('a','z'))
print(a.split(' '))
'''

# We cannot combine strings and numbers,the format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
    
'''
a = "Joy"
b = 25
c = "I am {} and my age is {}"
print(c.format(a,b))
'''

# String methods 

'''
a = "I am a programmer, i love programmer"
b = a.count("programmer")
print(b)
'''

# Python operators
'''
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''

'''
# Arithmetic operators
a = 10
b = 5
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)
print("Modulus:", a % b)

# Comparison operators
x = 10
y = 20
print("\nComparison Operators:")
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)

# Logical operators
p = True
q = False
print("\nLogical Operators:")
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

# Assignment operators
z = 5
print("\nAssignment Operators:")
z += 3
print("Add and assign:", z)
z -= 2
print("Subtract and assign:", z)
z *= 4
print("Multiply and assign:", z)
z /= 2
print("Divide and assign:", z)
z %= 3
print("Modulus and assign:", z)
z **= 2
print("Exponentiation and assign:", z)
z //= 3
print("Floor Division and assign:", z)

# Identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("\nIdentity Operators:")
print("Is:", list1 is list2) # returns False because x is not the same object as y, even if they have the same content
print("Is not:", list1 is not list2)

# Membership operators
print("\nMembership Operators:")
print("In:", 1 in list1)
print("Not in:", 4 not in list1)
'''

# Python Collections (Arrays)

# List example
'''
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuple example
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Set example
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionary example
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Dictionary:", my_dict)
'''


'''
 List vs Tuples vs Sets vs Dict

- **Lists**: Ordered, mutable collections with duplicate elements. Use for ordered data that needs modification.
- **Tuples**: Ordered, immutable collections with duplicate elements. Use for fixed data that should not change.
- **Sets**: Unordered, mutable collections with unique elements. Use for unique data and set operations.
- **Dictionaries**: Unordered, mutable collections of key-value pairs. Use for associative data and fast lookups based on keys.
'''

 # List methods 
'''
# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Append method
my_list.append(6)
print("List after appending 6:", my_list)

# Insert method
my_list.insert(2, 10)
print("List after inserting 10 at index 2:", my_list)

# Extend method
my_list.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", my_list)

# Remove method
my_list.remove(3)
print("List after removing 3:", my_list)

# Pop method
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("List after popping:", my_list)

# Index method
index_of_4 = my_list.index(4)
print("Index of element 4:", index_of_4)

# Count method
count_of_2 = my_list.count(2)
print("Count of element 2:", count_of_2)

# Reverse method
my_list.reverse()
print("Reversed list:", my_list)

# Sort method
my_list.sort()
print("Sorted list:", my_list)
'''



  #condition
'''
age=int(input("enter age")) 
if age>=30:
    print("senior") # Python uses indentation to indicate a block of code.
else:
    print("junior")
'''

  #short condition
'''
a=1;b=2
print(b if a>b else b>a)
'''

  #for loop
'''
for x in range(1,15,2): # starting 1 , upto 15 ,  skip 2
    print(x)
'''

  #while loop
'''
a=1
while a<=10:
        print("joy")
        a=a+1
print("end")
'''


'''
i=1
sum=0
while i<100:
    sum+=i
    i+=2
print(sum)
'''

  #series loop
''' 1+2+3+.....n '''

'''
n=int(input("Enter number"))
sum=0

for x in range(1,n+1,1):
    sum=sum+x

    print(sum) 
'''

  #pattern printing shortcut method
'''
n=3
for x in range(n+1):
 print(x*"0")

'''

  #User input
'''
name = input("Enter name ")
print("Hey",name)
'''

# Function

'''def multiply(x):
    return x*5
    
print(multiply(2))
'''
# Lambda

'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
'''

# Module
'''
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
'''

'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
Python has a built-in package called json, which can be used to work with JSON data.
'''

# RegEx
'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
'''

# PIP
'''
PIP is a package manager for Python packages, or modules if you like.
If you have Python version 3.4 or later, PIP is included by default.
'''

# Error handling

'''
try:
    print(x)
except:
    print("name 'x' is not defined")
'''

# Python Classes/Objects
'''
A Class is like an object constructor, or a "blueprint" for creating objects.
Classes and objects in Python are important because they provide a structured and modular way to organize code, promote code reuse, encapsulate data and behavior, and facilitate key principles of object-oriented programming such as inheritance and polymorphism. 
They contribute to cleaner, more maintainable, and flexible code.
'''
'''
# Define a class named Person
class Person:
    # Constructor method (__init__) to initialize object attributes
    def __init__(self, name, age):
        # Set the 'name' attribute of the object to the provided 'name' parameter
        self.name = name
        # Set the 'age' attribute of the object to the provided 'age' parameter
        self.age = age

# Create an instance of the Person class with the name "John" and age 36
p1 = Person("John", 36)

# Print the 'name' attribute of the p1 object
print(p1.name)  # Output: John

# Print the 'age' attribute of the p1 object
print(p1.age)   # Output: 36
'''

# pass
'''The pass statement does nothing and allows the program to continue execution without raising any errors.'''

'''
for i in range(5):
    pass
'''

