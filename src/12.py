def get_random_code():
  import random
  numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
  password = ""
  for i in range(10):
    password += random.choice(numbers)
    password += random.choice(letters)
    password += random.choice(symbols)
  return password
