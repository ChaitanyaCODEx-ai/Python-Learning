print("here is a calculator for you")
response = int(input("Enter your number:"))
print("Your 1st number is: " , response)
response2 = int(input("Enter your 2nd number:"))
print("Your 2nd number is: " , response2)
response3 = input("Enter your operator: (+(Addition)\n -(Subtraction)\n *(Multiplication)\n /(Division)\n %(to find the remainder)\n **(power eg: 2^3=8))\n//(floor division):")
if response3 == "+":
    print("The result is: " , response + response2)
elif response3 == "-":
    print("The result is: " , response - response2)
elif response3 == "*":
    print("The result is: " , response * response2)
elif response3 == "/":
    print("The result is: " , response / response2)
elif response3 == "%":
    print("The result is: " , response % response2)
elif response3 == "**":
    print("The result is: " , response ** response2)
elif response3 == "//":
    print("The result is: " , response // response2)
else:
    print("TUM GADHE HO!!!!")

numbers = [1, 2, 3, 4, 5]

