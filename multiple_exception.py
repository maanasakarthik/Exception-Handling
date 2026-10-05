try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is an error!😬")
except ValueError:
    print("Please enter valid whole numbers.")
except:
    print("Incorrect Input")
else:
    print("No exceptions!")
finally:
    print("This will execute no matter what.")