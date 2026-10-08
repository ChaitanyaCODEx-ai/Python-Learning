#import package 
#package like random is used to generate random numbers.
import random

print(random.randrange(1, 10))
print(random.randint(1, 10))
print(random.shuffle([1, 2, 3, 4, 5, 6])) #random.shuffle(list)
print(random.sample([1, 2, 3, 4, 5, 6], 2)) #random.sample(list, no. of elements to be selected)
print(random.random()) #random.random() : returns a random float number between 0.0 to 1.0
print(random.uniform(1, 10)) #random.uniform(a, b) : returns a random float number between a to b
'''can be used as comment to write multiple lines of comments.'''

#strings are arrays in python. we can access the characters of a string using index numbers.
a = 'Hello, World!'
print(a[1]) #prints the second character of the string
#for loop to iterate through the string
for x in "banana":
    print(x)    # for looping for is used to iterate through the string and print each character of the string in a new line.
#string lenght -  check length of a string
a = "Hello, World!"
print(len(a)) #len() : returns the length of a string/ tells the no. of characters in a string.

#Check string - to check if a certain phrase or character is present in a string we use the keyword in.
txt = 'The best things in life are free!'
print("free" in txt) #returns True if the phrase is present in the string, otherwise returns False.
if 'world' in txt:
    print("Yes, world is present.")
else:
    print("No, world is not present.")
print("world" not in txt) #returns True if the phrase is not present in the string, otherwise returns False.

b = 'Chaitanya'
print(b[2:5]) #prints the characters from index 2 to 5 (not included)
print(b[:5]) #prints the characters from the beginning to index 5 (not included)
print(b[2:]) #prints the characters from index 2 to the end
print(b[-5:-2]) #prints the characters from index -5 to -2 (not included)

print(a.upper()) #upper() : converts the string to upper case
print(a.lower()) #lower() : converts the string to lower case
print(a.strip()) #strip() : removes any whitespace from the beginning or the end

b = "Luck to u everyone"
print(b.replace("L", "F")) #replace() : replaces a string with another string
print(b.split("v")) #split() : splits the string into a list

print(a + b) #concatenation : concatenates two strings
print(a + " " + b) #concatenation : concatenates two strings with a space in between