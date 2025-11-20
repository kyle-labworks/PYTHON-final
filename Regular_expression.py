import re

# Ask the user for a password
password = input("Enter a password: ")

# Regex rule: at least 8 characters, one uppercase, one lowercase, one digit
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

# Check if the password matches the rule
if re.match(pattern, password):
    print("Password is valid!")
else:
    print("Password is invalid. Must be at least 8 characters, include uppercase, lowercase, and a digit.")
