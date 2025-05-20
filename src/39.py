def print_rangoli(size):
    # Create a list of characters from 'a' to 'z'
    char_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    # Sort the list in reverse order and remove any repeated characters
    sorted_chars = ''.join(sorted(char_list, reverse=True))
    result_string = []

    # Iterate through the sorted characters in reverse order
    for char in sorted_chars:
        # Add square brackets to form the inner circle of the range
        result_string.append(f"{'-' * 2*size - 1}{''.join(char_list[:size])+'-'}")
        # Add right and left circles with alternating colors
        for i in range(size):
            result_string.append(f"{char}{' '*(size-i-2)}{char}")
    return "\n".join(result_string[::-1])

# Example usage: Print the first 5 rows of a random range (range(5))
print(print_rangoli(size=5))
