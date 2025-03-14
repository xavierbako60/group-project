import random

def get_random_code():
    numbers = "1234567890"
    letters = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!@#$%^&*()-=+[{]};:'\"<>,./?\\"
    code = ""
    for i in range(16):
        if i % 2 == 0:
            code += random.choice(letters)
        elif i % 3 == 0:
            code += random.choice(numbers)
        else:
            code += random.choice(symbols)
    return code
