import sys

if len(sys.argv) < 4:
    print("Usage: app.py <operation> <operand1> <operand2>")
    sys.exit(1)

operation = sys.argv[1]
operand1 = sys.argv[2]
operand2 = sys.argv[3]

if operation == "add":
    try:
        result = int(operand1) + int(operand2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
elif operation == "subtract":
    try:
        result = int(operand1) - int(operand2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
elif operation == "multiply":
    try:
        result = int(operand1) * int(operand2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
elif operation == "divide":
    try:
        result = int(operand1) / int(operand2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        sys.exit(1)
else:
    print("Unsupported operation. Use add, subtract, or multiply.")
    sys.exit(1)