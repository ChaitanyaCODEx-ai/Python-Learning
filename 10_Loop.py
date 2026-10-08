response = int(input("Tell till which number you want to count?"))
"""i = 1
while i <= response:
    print(i)
    i += 1
else:
    pass

j = 1
while j<= response:
    print(j)
    if j==50:
        break
    j += 1"""

h = 0
while h < 6:
  h += 1
  if h == 3:
    continue
  print(h)

fruits = ["Apple","Banana","Chikoo","Mango","Grapes","Watermelon"]
for x in fruits:
  if x == "Grapes":
   break
  if x == "Banana":
    continue
  print(x)

for z in range(response):
  print(z)

#NESTED LOOPS
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)