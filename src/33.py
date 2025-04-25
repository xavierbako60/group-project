import numpy as np

def check_solution(func):
    # Example usage: 
    result = func([1, 2, 3])
    print(result)  # This line is commented out as it's not part of the solution
    if isinstance(result, tuple):  # Example logic to verify the type and contents of the returned value
        print("Function executed successfully.")
    else:
        print("Error: Function did not return a tuple.")
        
def square(x):
    # Implementing a function that squares the input x
    return x ** 2

check_solution(square)
