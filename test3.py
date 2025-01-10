#3  Improved Password Strength Checker with feedback on what is missing


import string

def check_password_strength(password):
    # Criteria flags
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    no_spaces = " " not in password

    # Calculate strength score
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

    # Classify strength and provide feedback
    feedback = []
    if not length_ok:
        feedback.append("- Password should be at least 8 characters long.")
    if not has_upper:
        feedback.append("- Add at least one uppercase letter.")
    if not has_lower:
        feedback.append("- Add at least one lowercase letter.")
    if not has_digit:
        feedback.append("- Include at least one number.")
    if not has_special:
        feedback.append("- Use special characters (e.g., !, @, #, $).")
    if not no_spaces:
        feedback.append("- Remove any spaces.")

    if score == 6:
        return "Strong password"
    elif 4 <= score < 6:
        return "Moderate password\nSuggestions:\n" + "\n".join(feedback)
    else:
        return "Weak password\nSuggestions:\n" + "\n".join(feedback)

# Input from user
password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)