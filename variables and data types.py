a = 134673

a1 = 9
b = "Sakib Hossain"
c = True
d = None
print(a)
print(b)
print(a + a1)
print("The type of a is :", type(a))
print("The type of b is :", type(b))
print("The type of c is :", type(c))
print("The type of d is :", type(d))

list1 = [8,2.3, [-4,5],["Apple", "banana"]]
print(list1)

tuple1=(("parrot","sparrow"),("lion","tiger"))
print(tuple1)

dict1= {"name": "sakib", "age": 23, "canVote":True}
print(dict1)

def myfunc():
  global x
  x = "Awesome"

myfunc()
print("Python is " + x)


y = "Helo world"
print(type(y))
y = 20
print(type(y))
y = 20.5
print(type(y))
x = 1j
print(type(y))
x = ["apple","banana","cherry"]
print(type(y))
y =("apple", "banana","cherry")
print(type(y))
y = range(6)
print(type(y))
y = {"name": "sakib", "age": 23}
print(type(y))
y = {"apple", "banana","cherry"}
print(type(y))
y = frozenset({"apple","banana","cherry"})
print(type(y))
y = True
print(type(y))
y = b"Hello"
print(type(y))
y = bytearray(5)
print(type(y))
y = memoryview(bytes(5))
print(type(y))
y = None
print(type(y))