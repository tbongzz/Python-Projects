#Input validation
#optimized the function
#Redundant operations are reduced by removing the condition result is not None in the division operation, as the divide() function already handles the zero division error.

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    try:
        result = a / b
        if not result.is_integer():
            return round(result, 2)  # Round to 2 decimal places if not an integer
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

def validate_numeric_input(input_str):
    """Validate user numeric input"""
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def calculator():
    """Run the simple calculator"""
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input
    while True:
        choice = input("Select operation (1-4): ")
        if choice in ('1', '2', '3', '4'):
            break
        else:
            print("Invalid choice. Please select a valid operation.")

    while True:
        num1 = input("Enter the first number: ")
        if validate_numeric_input(num1):
            break
        else:
            print("Invalid input. Please enter a valid numeric value.")

    while True:
        num2 = input("Enter the second number: ")
        if validate_numeric_input(num2):
            break
        else:
            print("Invalid input. Please enter a valid numeric value.")

    num1 = float(num1)
    num2 = float(num2)

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {num1} / {num2} = {result}")

# Run the calculator
calculator()
