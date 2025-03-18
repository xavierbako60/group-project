import random

def get_random_code():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special_chars = '#@$%^&*()_+-=[]{}|;:",./<>?'
    all_chars = letters + numbers + special_chars
    code = ''
    for i in range(10):
        code += random.choice(all_chars)
    return code
