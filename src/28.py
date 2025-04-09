def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers and returns the sum.
    
    Parameters:
    a (int): The first integer to be added.
    b (int): The second integer to be added.
    
    Returns:
    int: The sum of the two integers.
    """
    return a + b

def calculate_average(numbers: list) -> float:
    """
    Calculates the average of a list of numbers and returns the average.
    
    Parameters:
    numbers (list): A list of integers or floats.
    
    Returns:
    float: The average of the list of numbers.
    """
    return sum(numbers) / len(numbers)

def is_even(number: int) -> bool:
    """
    Checks if a number is even.
    
    Parameters:
    number (int): The integer to be checked for evenness.
    
    Returns:
    bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0
