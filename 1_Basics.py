#This is print statement
print("My name is Chaitanya Bhardwaj")

#This is an if statement
#Identation is very important in python leaving any space will give you an error when you run the code.
if 5>2:
    print("Five is greater than two!")
if 5<2:
    print("Five is less than two!")

#Variable in python
x = "Hello World"
y = 5
print(x)
print(y)

# This will give you an error because you cannot write two print statements in one line. 
# You have to write them in two different lines.    
#print("My name is Chaitanya Bhardwaj") print("I want to become a Data Scientist")

#if we put a seperator ; then it will work
print("My name is Chaitanya Bhardwaj"); print("I want to become a Data Scientist")

#If you want to print multiple words on the same line, you can use the end parameter:
print("My name is Chaitanya Bhardwaj", end=" ")
print("and also want to become a Data Scientist")

#if you want to change the line while in between the print statements you can use the \n character.
print("My name is Chaitanya Bhardwaj\nI want to get thin and muscular 💪🏻")

#unlike texts in print() function. integers and floats are not enclosed in quotes.
print(5)
print(42341%345)
print(3.14)
print(3+7)
print(3-7)
print(3*7)
print(3/7)

#we can also mix texts and numbers in print() function but we have to use commas to separate them.
print("why was ",6," afraid of ",7,"? Because,",7," ate ",9,"!")

"""multi-line comments can be written using triple quotes.
This is a multi-line comment."""

#Variables are containers for storing data values. In Python, variables are created when you assign a value to them.
#Variable names can be of any length and can consist of letters, numbers, and underscores.

x = 4 # x is a type of int
x = 'Hello, World!' # x is now a type of str
print(x)

#Casting - we can specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3 
z = float(3)  # z will be 3.0
print(   x  ,  y  ,  z  )

#data type of a variable can be known by the type() function.
x = 5
y = 'John'
print(type(x))
print(type(y))

# "....." '.....' are the same

#Variable names must not have any spaces in them. If you want to use multiple words in a variable name, you can separate the words with an underscore character.
#also variable cannot start with a number, but can contain numbers after the first letter.
my_variable = "xyz"
print(my_variable)

#Camel Case is also allowed in python but it is not recommended. It is better to use underscores to separate words in a variable name.
myVariable = "xyz"
#Pascal Case is also allowed in python but it is not recommended. It is better to use underscores to separate words in a variable name.
MyVariable = "xyz"
#Snake Case is the recommended way to name variables in python. It is better to use underscores to separate words in a variable name.
my_variable = "xyz"