#best calculator to make so far 

def calculator(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == "/":
        try:
            return x / y
        except ZeroDivisionError:
                return "Error: Division by zero is not allowed"
    else:
         return "Unknown operator"
    
print("Calculator 2.0")
print("Available opeartor: +, -, *, -")

try:
    x = float(input("Enter First number: "))
    operator = input("Enter operator: ")
    y = float(input("Enter second number: "))

    result = calculator(x, y, operator)
    print("Result: ", result)

except ValueError:
        print("Error: please enter a valid number")
