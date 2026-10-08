"""something = input("Enter something: ")
if (count := len(something)) > 5:  # --------> count the number of elements in the string and assign it to the variable 'count' and check if it is greater than 5
    print(f"THE Character you have entered has {count} characters")
else:
    print("you have entered less than 5 characters")

num = 6
x = 'friday' if num == 5 else 'saturday' if num == 6 else 'sunday'
print(x)

list = [1, "YOU", 3, "Dice" , "Random_shit"]
print(type(list))
Dictionary = {"Name": "John", "Age": 30, "City": "New York"}
print(type(Dictionary))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[0:4])
print(thislist[-4:-1]) #---------> the -1 is taken as the last index of the list and the -4 is taken as the 4th last index of the list
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1:3] = ["blackcurrant", "watermelon"] #----------> this will replace the elements at index 1 and 2 with the new elements in the list
print(thislist)

thislist.insert(2, "grapes") #-----------> THIS will insert the element grapes at index 2 
print(thislist)

vegetables = ["potato", "tomato", "onion"]
thislist.extend(vegetables) #-----------> this will add the elements of the vegetables list to the end of the thislist
print(thislist)

thislist.remove("orange") #-----------> this will remove the element orange from the list
print(thislist)

thislist.pop(1) #-----------> this will remove the element at index 1 from the list
print(thislist)

thislist.clear() #-----------> this will remove all the elements from the list
print(thislist)

#LOOP THROUGH A LIST
list1 = ["apple", "banana", "cherry"]
for i in range(len(list1)): #-----> len(list1) will return the number of elements in the list and 
                            #-----> range(len(list1)) will return a range object that contains the indices of the list
  print(list1[i])           #-----> basically range(3) will give i = 0,1,2 and so it will print the elements at the list according to the index number

thislist = ["apple", "banana", "cherry"]

Ye tune Basket (list) tayar kar di.

len(thislist)

len matlab Length. Basket me kitne fruits hain? Total 3.

range(len(thislist)) yaani range(3)

range(3) Python ko bolta hai: 0, 1, 2 tak count kar (jitne basket ke index hain).

for i in range(...):

Ye ek Loop hai. Ye bolta hai: "Ginti chalao aur bari-bari i ki value badlo."

Pehli baar: i = 0 → print(thislist[0]) → apple print hua.

Dusri baar: i = 1 → print(thislist[1]) → banana print hua.

Tisri baar: i = 2 → print(thislist[2]) → cherry print hua.

list2 = ["apple", "banana", "cherry"]
i = 0
while i < len(list2): #-----> basically i < elements in list2 i.e. i < 3
    print(list2[i]) #-----> print the element at index i
    i = i + 1 #-----> increment i by 1 so that the loop can move to the next index so the loop can go on until i < 3 or i = 2 is the last one.
[print(x) for x in list2] #--------> The brackets [] are there because that line is using a Python feature called a List Comprehension.
#A list comprehension is designed to create a new list on the fly.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x) #---> is a list method in Python that adds the item x to the end of newlist
print(newlist)

for y in fruits:
 if "b" in y:
    newlist.append(y)
print(newlist) 

#OR

newlist = [x for x in fruits if "e" in x]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
# if x is not equal to banana, then add x to the newlist but if x is banana then add orange to it hahahah
print(newlist) 

cities = ["Mumbai", "delhi", "Bangalore", "hyderabad", "Chennai", "Bilaspur"]
countries = ["India", "USA", "UK", "Australia", "Canada"]
vehicles = ["Car", "Bike", "Bus", "Truck", "Cycle"]
Friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cities.sort() #----------> a - z ordering of the list
print(cities)
numbers.sort() #----------> increasing order of the list
print(numbers)
countries.sort(reverse=True) #----------> z - a ordering of the list
print(countries)
numbers.sort(reverse=True) #----------> decreasing order of the list
print(numbers)

def myfunc(n): #-------> here i defined a function named myfunc
    return abs(n - 50) #-------> this function will return the absolute value of n - 50

numbers1 = [100, 50, 65, 82, 23]
numbers1.sort(key=myfunc, reverse=True) #-------> here i am sorting the list numbers1 based on the key myfunc which is defined above
print(numbers1) #-------> this will print the sorted list based on the key myfunc
cities.sort()
print(cities)
cities.sort(key=str.lower) #-------> this will sort the list based on the lowercase of the string
print(cities)
big_cities = cities.copy() #-------> this will create a copy of the list cities and assign it to big cities
print(big_cities)
yourlist = vehicles[:] #-------> this will create a copy of the list vehicles and assign it to yourlist
print(yourlist)

#JOINING LISTS
#1
Close_Hearts = Friends + cities
print(Close_Hearts) #-------> this will concatenate the two lists Friends and cities and assign it to Close_Hearts
#2
for x in cities:
    Friends.append(x) #-------> this will append the elements of the list cities to the list friends
print(Friends)
#3
cities.extend(Friends) #-------> this will extend the list cities by adding the elements of the list Friends to it
print(cities)

#WE CAN MULTIPLY TUPLES
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#joining set and tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#Frozenset
# From a list
numbers = frozenset([1, 2, 3, 3, 4])
print(numbers)  # Output: frozenset({1, 2, 3, 4})

# From a string
letters = frozenset("hello")
print(letters)  # Output: frozenset({'h', 'e', 'l', 'o'})

#Dictionaries
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
x = thisdict["brand"] #-------> this will retrieve the value associated with the key "model" from the dictionary thisdict
print(x)
y = thisdict.get("year")
print(f"The {x} started in the year {y}")
z = thisdict.keys() #-------> this will return a view object that displays a list of all the keys in the dictionary
print(z)

x = thisdict.keys()
thisdict["Colors"] = "RED"
print(thisdict)

q = thisdict.items()
print(q) #-------> this will return a view object that displays a list of a dictionary's key-value tuple pairs

p = thisdict.update({"month": "January"}) #-------> this will update the value associated with the key "colors" in the dictionary thisdict to a new list of colors
print(thisdict)

for x,y in thisdict.items(): #-------> this will loop through the dictionary and print the key and value of each item in the dictionary
  print(x,y)

for x in thisdict.keys():
    print(x)

mydict = dict(thisdict) #----------------> Copy thisdict
print(mydict)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

for x,obj in family.items():
    print (x)
    for y in obj:
      print(y , ":" , obj[y])

