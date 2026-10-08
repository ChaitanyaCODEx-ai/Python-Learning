#def : Tells Pythone to define a new function
# myfunc(): The name of the function, followed by empty parentheses showing it takes no input parameters.
x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()
print("Python is " + x)

#GLOBAL VARIABLES: Variables that are created outside of a function (as in all of the examples above) are known as global variables.
def myfunc():
    global y
    y = "fantastic"

#A FUCKING STUPID MISTAKE THAT I MADE:
#myfunc() should stick to the left line no identation space :(
myfunc()
print("Python is " + y)

# def myfunc():
#   global y
#   y = "fantastic"

#   myfunc()    ← inside function ❌
#myfunc()    ← outside function ✅

#print(... y)

x = 'awesome'
                             #-
def myfunc():                # |
    global x                 # |  between def myfunc()  variable x 
    y = 'easy'               # |  and myfunc() .
    x = 'fantastic'          # | 
    print('Python is ' + y)  # |
myfunc()                     #-
print('Python is ' + x)

#print(x[whole number]) : extracts and prints the fourth character of the string stored in the variable x
#The first character is at index 0, the second at index 1, and so on.
x = 'welcome'
print(x[3])

#len() : returns the length of a string/ tells the no. of characters in a string.
x = 'welcome'
print(len(x))
txt = "who"
x  = txt[2]
print(x)

#txt : a variable that holds a string value.
x = 'welcome'
print(x[3:5])

x = str("chaitanya260118")
print(x)