def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers.
    """
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    """
    Subtract two numbers.
    """
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers.
    """
    return a * b

def divide_numbers(a: float, b: float) -> float:
    """
    Divide two numbers.
    """
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")

# Example usage
num1 = 5.0
num2 = 3.0

result_addition = add_numbers(num1, num2)
print(f"Addition result: {result_addition}")

result_subtraction = subtract_numbers(num1, num2)
print(f"Subtraction result: {result_subtraction}")

result_multiplication = multiply_numbers(num1, num2)
print(f"Multiplication result: {result_multiplication}")

try:
    result_division = divide_numbers(num1, num2)
    print(f"Division result: {result_division}")
except ValueError as e:
    print(e)
