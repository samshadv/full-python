operator = input("Enter an operator (*, +, /, -): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The addition of {num1} and {num2} is = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"The subtraction of {num1} and {num2} is = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} is = {result}")

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The division of {num1} and {num2} is = {result}")
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid operator")
