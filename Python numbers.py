x = 1       #int
y = 2.8     #float
z = 1j      #complex

#convert from int to float

a = float(x)

#convert from float to int

b = int(y)

#convert from int to complex

c = complex(x)

#convert from complex to int

d = int(abs(z))


print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))


import random
print(random.randrange(1,10))