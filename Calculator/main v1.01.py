# ADDED ERROR HANDLING
# The divide() function uses a try-except block to catch a ZeroDivisionError when attempting to divide by zero. It displays an error message and returns None to indicate the error.
# In the calculator() function, a try-except block is used to catch ValueError when converting user input to numeric values. If the user enters non-numeric values, it displays an error message.
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

def calculator():
    """Run the simple calculator"""
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input
    try:
        choice = input("Select operation (1-4): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

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
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
