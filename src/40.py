import numpy as np

def square_array(array_1d):
    """
    Function to square an array of one-dimensional integers.
    
    Parameters:
    - array_1d: A 1D array of integers.

    Returns:
    - A new 1D array with each element squared.
    """
    return np.square(array_1d)

def main():
    # Example usage
    sample_array = [1, 2, 3]
    square_array_result = square_array(sample_array)
    print(square_array_result)

if __name__ == "__main__":
    main()
