import random

def get_random_code(length):
    char = "1234567890abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += char[random.randint(0, len(char) - 1)]
    return result
