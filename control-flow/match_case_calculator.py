"""
A pyhton script that will prompt the user to enter two numbers and select an operation (addition
,subtraction. multiplication or division).
The script will perform the selected operation usinf a Match case statement and display the results.

Input will be an int type.
variables.
First and second number.
Operand
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator =input("Choose the operation (+, -, *, /):")

match operator:
    case '+':
        print(f"The result is {num1 + num2}.")
    case '-':
        print(f"The result is {num1 - num2}.")
    case '*':
        print(f"The result is {num1 * num2}.")
    case '/':
        try:
            result = num1 / num2
            print(f"The result is {result}.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")

    case _:
        print("Incorrect operation entered")
