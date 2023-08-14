import re

def validate_password(password):
    # Check if the password meets the length criteria
    if len(password) < 6 or len(password) > 16:
        return False
    
    # Check if the password contains at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    
    # Check if the password contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    
    # Check if the password contains at least one digit
    if not re.search(r"\d", password):
        return False
    
    # Check if the password contains at least one special character
    if not re.search(r"[$#@]", password):
        return False
    
    return True
password = input("Enter a password: ")
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")
