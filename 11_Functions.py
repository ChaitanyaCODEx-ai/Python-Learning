def my_funciton():
    print("Hello from MY FUNCTION")

my_funciton()
my_funciton()
my_funciton()

print("You can convert you temperature from celsius scale to Fahrenhite scale")
def FtoC(F):
    return(F-32)*5/9

response = int(input("Enter value of F temperature you want to convert to celsius: "))
FtoC(F = response)
print(FtoC(response))

def name(fname):
    print(fname + " " + "Refsnes")

name("Emil")
name("Tobias")
name("Linus")

def naam(FirstName,Lastname):
    print(FirstName + " " + Lastname)

naam("Emil","Refsnes")

def friend(name = "friends"):
  print("Hello", name)

friend("Emil")
friend("Tobias")
friend()
friend("Linus")

def fruit_func(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["Apple","Banana","Mango"]
fruit_func(my_fruits)

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)
