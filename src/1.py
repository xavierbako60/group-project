import random

def get_random_code():
    """Generates a random string of characters"""
    length = random.randint(3, 7)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for i in range(length))