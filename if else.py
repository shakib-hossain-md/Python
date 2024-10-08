a = 200
b = 33

if b>a:
  print("b is greater than a")
elif a==b:
  print("a and b are equal")
else:
  print("a is greater than b")


# Short hand if

if a>b: print("a is greater than b")

# Short hand if else

a = 2
b = 330
print("A") if a>b else print("B")


# One line if else statement
a = 300
b = 330
print("A") if a>b else print("=") if a == b else print("B")

# AND

a = 200
b = 33
c = 500
if a>b and c>a:
  print("Both condition are true.")


# OR

if a<b or c>a:
  print("At least one condition is true")

# NOT
if not a>c:
  print("a is NOT greater than c")


# Nasted if
x = 41
if x>10:
  print("Above ten")
  if x>20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Pass statement

a = 33
b = 200
if b>a:
  pass