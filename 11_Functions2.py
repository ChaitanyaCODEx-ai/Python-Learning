# Defining a function helps you to
def my_function():
    return ["apple","banana","cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def function():
    return(10,20)

x,y = function()
print("x:",x)
print("y:",y)

#POSITIONAL ARGUMENTS
# / enforces positional-only parameters for everything to its left
# * enforces keyword-only parameters for everything to its right.
def func(name,/):
    print("hello",name)
func("Emil")

def funk(*,name):
    print("hello", name)
funk(name = "DUNIYA")

def funct(a,b,c,d):
    return a+b+c+d
result = funct(5,10,c=15,d=20)
print(result)

