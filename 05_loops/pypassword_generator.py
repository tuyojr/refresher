# import string
# symbols = [symbol for symbol in string.punctuation]

import random

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password?\n"))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number_of_symbols = int(input("How many symbols would you like?\n"))
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

num_of_numbers = int(input("How many numbers would you like?\n"))
numbers = [str(num) for num in range(0,10)]

sequence = []

for letter in range(1, number_of_letters + 1):
    sequence.append(random.choice(letters))
for symbol in range(1, number_of_symbols + 1):
    sequence.append(random.choice(symbols))
for num in range(1, num_of_numbers + 1):
    sequence.append(random.choice(numbers))

random.shuffle(sequence)
password = ''

for char in sequence:
    password += char

print(f"Here is your password: {password}")