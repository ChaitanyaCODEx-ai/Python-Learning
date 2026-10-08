import random

print("Welcome to the Number Generator!")
print("This program will generate a random number for you.")
print("Generating your random number...")
response = input("Press y to generate a random number or n to exit: ")
if response == "y":
    random_number = random.randint(1, 100)
    print(f"Your random number is: {random_number}")
elif response == "n":
    print("You don't want to generate a random number. Exiting the program......")
else:
    print("Invalid input. Please try again.")
