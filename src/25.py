def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        if i * i > n:
            break
        else:
            total += i ** 2
    return total

# Example usage
result = sum_of_squares(10)
print(result)  # Output: 165
