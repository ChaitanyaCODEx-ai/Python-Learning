#FINDING THE MAX VALUE
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print("Enter numbers one by one. Type 'NO' when you are done.")
while True:
  response = input("Enter a number [if you don't want to than press NO] : ")
  if response.strip().upper() == "NO": #----> .strip() : is a string method that removes any leading (at the beginning) and trailing (at the end) whitespace—such as spaces, tabs, or newlines.
        print("Exiting loop...")
        break
