import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    return True

# Prompt the user to enter a password
password = input("Enter a password: ")

# Check the validity of the password
validity = is_valid_password(password)

# Display the result
if validity:
    print("Valid password!")
else:
    print("Invalid password!")
