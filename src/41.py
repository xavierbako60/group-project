import random

def random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str

print(random_string(10)) # Example usage: A 10-character long random string
