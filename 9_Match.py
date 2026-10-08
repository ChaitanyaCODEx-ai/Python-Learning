import random
print("")
response = input("Do yo want to know what day it is?\nenter (y/n)")
#if response == "y":
day = random.randint(1,7)
match response:
    case "y":    
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
    case "n":
        print("You don't want to know the day")
    case _:       #-------------> case _ last case value if you want a code block to exectue when there are no other matches
                print("INVALID INPUT")

match response:
     case "y":
        match day:
            case 1|2|3|4|5:  #-------------> check more than 1 one cases for same output
                print("Today is a weekday")
            case 6|7:
                print("Today is a weekend")

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")