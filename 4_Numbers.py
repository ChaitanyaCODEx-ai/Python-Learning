#There are three umeric types in Python: 
#int, float, and complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = 12E4 # float
b = 3 + 5j # complex
c = 6
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

#TYPE CONVERSION: You can convert from one type to another with the int(), float(), and complex() methods:
a = float(x) # convert from int to float
b = int(y)   # convert from float to int
c = complex(x) # convert from int to complex
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
