def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

print(add_numbers(5, 3))
print(subtract_numbers(10, 4))
print(multiply_numbers(8, 2))
try:
    print(divide_numbers(4, 0))
except ValueError as e:
    print(e)
