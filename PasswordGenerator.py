import random

#Characters that will be selected
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "()[]{},;:?!@#$%^&*"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters

#To select how long the password should be
def pwd_length():
    while True:
        try:
            length = int(input("Enter the desired password length (8-20): "))
            if 8 <= length <= 20:
                return length
            else:
                print("That number isn't valid. Please enter a number between 8 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#To select how many uppercase, symbol, and number characters
def get_valid_element_count(prompt, max_value):
    while True:
        try:
            count = int(input(prompt))
            if 0 <= count <= max_value:
                return count
            else:
                print(f"Please enter a value between 0 and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Selecting the amount of passwords to generate
def get_valid_password_amount(prompt, max_value):
    while True:
        try:
            count = int(input(prompt))
            if 1 <= count <= max_value:
                return count
            else:
                print(f"Please enter a value between 1 and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Calling the def functions above
length = pwd_length()
amount = get_valid_password_amount("Enter the number of passwords to generate: ", 20)

#Calling the def functions for the different characters
while True:
    num_uppercase = get_valid_element_count("How many uppercase letters do you want inside your password: ", length)
    num_numbers = get_valid_element_count("How many numbers do you want inside your password: ", length - num_uppercase)
    num_symbols = get_valid_element_count("How many symbols do you want in your password: ", length - num_numbers)
    if num_uppercase + num_numbers + num_symbols <= length:
        break
    else:
        print("The sum of uppercase letters, numbers and symbols exceeds the total password length. Please enter your requirements again.")

#Randomly chooses characters from the inputs provided
for i in range(amount):
    password = []
    for i in range(num_uppercase):
        password.append(random.choice(uppercase_letters))
    for i in range(num_numbers):
        password.append(random.choice(digits))
    for i in range(num_symbols):
        password.append(random.choice(symbols))
        remaining_length = length - num_uppercase - num_numbers - num_symbols
    if remaining_length < 0:
        raise ValueError("The sum of num_numbers and num_symbols should not exceed the total length of the password.")
    for i in range(remaining_length):
        password.append(random.choice(lowercase_letters))

#Shuffles the characters around and prints
    random.shuffle(password)
    print(''.join(password))