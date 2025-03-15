import random

def get_random_python_code(lines=10):
    code = []
    for i in range(lines):
        code.append(f"print('Random number {i}:', random.randint(1, 100))")
    return "\n".join(code)
