# 1  Very Basic Password Strength Checker


def check_password_strength(password):
   
    length_ok = len(password) >= 8                           # minimum length of password should be 8
    has_upper = any(char.isupper() for char in password)     # password should contain at least one uppercase letter
    has_lower = any(char.islower() for char in password)     # password should contain at least one lowercase letter
    has_digit = any(char.isdigit() for char in password)     # password should contain at least one digit

    
    if length_ok and has_upper and has_lower and has_digit:
        return "Strong password"
    else:
        return "Weak password"

# Input from user
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)
