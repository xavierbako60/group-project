def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_numbers(2, 3, 4))  # Output: 24
