import sys

# Функции для выполнения операций
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Основная часть программы
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 app.py <operation> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Both num1 and num2 must be numbers.")
        sys.exit(1)

    if operation == "add":
        print(f"Result: {add(num1, num2)}")
    elif operation == "subtract":
        print(f"Result: {subtract(num1, num2)}")
    elif operation == "multiply":
        print(f"Result: {multiply(num1, num2)}")
    elif operation == "divide":
        try:
            print(f"Result: {divide(num1, num2)}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Unsupported operation. Use add, subtract, multiply, or divide.")
        sys.exit(1)