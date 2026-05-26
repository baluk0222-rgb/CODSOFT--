# Password Generator Program

import random
import string

print("Password Generator")

# User enters password length
length = int(input("Enter password length: "))

# Characters to use in password
characters = string.ascii_letters + string.digits + string.punctuation

password = ""

# Generate password
for i in range(length):
    password = password + random.choice(characters)

# Display password
print("Generated Password:", password) 