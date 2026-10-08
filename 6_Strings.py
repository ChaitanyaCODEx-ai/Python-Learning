#F-Strings : F-strings are a way to format strings in python in such a way that we can embed multiple variables in a single scentence.
age = 20
txt = f"My name is John, and I am {age}"
print(txt)

price = 10000
tst = f"The price is {price} dollars"
print(tst)

# when we try to quote inside the quotes it will show error while executing.
#We can do \"write your text here\"
print("My name is \"John\" and I am 20 years old.")
# OR
print('My name is "John" and I am 20 years old.')

