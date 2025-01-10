#2  Improved Password Strength Checker with Special Characters and Spaces


import string

def check_password_strength(password):
    
    length_ok = len(password) >= 8                              # minimum length of password should be 8
    has_upper = any(char.isupper() for char in password)    # password should contain at least one uppercase letter
    has_lower = any(char.islower() for char in password)    # password should contain at least one lowercase letter
    has_digit = any(char.isdigit() for char in password)    # password should contain at least one digit
    has_special = any(char in string.punctuation for char in password)  # password should contain at least one special character
    no_spaces = " " not in password                          # password should not contain any spaces

   
    score = 0
    if length_ok:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if no_spaces:
        score += 1

    
    if score == 6:
        return "Strong password"
    elif 4 <= score < 6:
        return "Moderate password"
    else:
        return "Weak password"

password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)