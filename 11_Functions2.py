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

def kids(*kid):
    print("The youngest child is "+kid[2])

kids("Ace","Sabo","Luffy")

def my_function(*args):      #---------------> This type of Arguments are tuple data types
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#We can also use *args with regular parameters
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
    print(greeting,names[1])

my_function("Hello", "Emil", "Tobias", "Linus")

def my_function(*numbers):
   total = 0
   for num in numbers:
      total += num
      return total
   
print(my_function(1,2,3))
print(my_function(10,20,30,40,50))
print(my_function(5))