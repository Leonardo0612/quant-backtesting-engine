import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = list("!£$&@+?%/")
numbers = list("0123456789")

nr_letters = int(input("How many letters would you like in your password? (max 26) "))
nr_symbols = int(input("How many symbols would you like? (max 9) "))
nr_numbers = int(input("How many numbers would you like? (max 10) "))

password = ""
for i in range(1, nr_letters + 1):
    password += random.choice(letters)


for i in range(1, nr_symbols + 1):
    password += random.choice(symbols)


for i in range(1, nr_numbers + 1):
    password += random.choice(numbers)

password_list = list(password)
random.shuffle(password_list)
shuffled_password = "".join(password_list)

print(f"Your password is {shuffled_password}")