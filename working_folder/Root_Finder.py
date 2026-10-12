#A program that finds the root of any quadratic equation
import math 

print("suppose you have a quadratic equation fot the form ax² + bx + c")
a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))
D = b**2 - 4*a*c

if D > 0:
    z = math.sqrt(D)
    numerator1 = -b + z
    numerator2 = -b - z
    denominator = 2*a
    root1 = numerator1/denominator
    root2 = numerator2/denominator
    print("The roots of the equation are real and unequal")
    print("Root 1 : ", root1)
    print("Root 2 : ", root2)
elif D==0:
    z = math.sqrt(D)
    numerator2 = -b
    denominator = 2*a
    root1 = numerator2/denominator
    print("The roots of the equation are equal")
    print("Root of the equation is : ", root1)
else:
    print("The roots for the equation are complex/imaginary roots")

