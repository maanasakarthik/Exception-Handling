# Using a try and except
try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
# Using Value Error
except ValueError as ex:
    print("Please enter a valid number.")