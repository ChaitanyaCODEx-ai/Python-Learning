import random

print("Do you want to roll a dice: (yes/no)")
response = input("Give input:(yes/no) ")

if response == "yes":
    print(random.randint(1, 6))
elif response == "no":
    print("You dont like to roll a dice")
else:
    print("Invalid input")