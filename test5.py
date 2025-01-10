#5 Password Strength Checker with Entropy Calculation   (Entropy is a measure of password randomness), not very beginner friendly


import math
import string

COMMON_PASSWORDS = {"123456", "password", "123456789", "qwerty", "abc123", "password1", "12345678", "111111"}

def check_common_password(password):
  return password in COMMON_PASSWORDS

def calculate_entropy(password):
    # Define character set sizes
    char_sets = 0
    if any(char.islower() for char in password):
        char_sets += 26
    if any(char.isupper() for char in password):
        char_sets += 26
    if any(char.isdigit() for char in password):
        char_sets += 10
    if any(char in string.punctuation for char in password):
        char_sets += len(string.punctuation)
    if " " in password:
        char_sets += 1

    # Calculate entropy
    if char_sets == 0:  # Empty password
        return 0
    entropy = len(password) * math.log2(char_sets)
    return entropy

# Integrate with password strength checker
def check_password_strength(password):
    # Criteria flags
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    no_spaces = " " not in password
    not_common = not check_common_password(password)

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
    if not_common:
        score += 1

    # Entropy calculation
    entropy = calculate_entropy(password)

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
    if not not_common:
        feedback.append("- Avoid common passwords like '123456' or 'password'.")

    if score == 7 and entropy > 60:
        return f"Strong password (Entropy: {entropy:.2f})"
    elif 5 <= score < 7:
        return f"Moderate password (Entropy: {entropy:.2f})\nSuggestions:\n" + "\n".join(feedback)
    else:
        return f"Weak password (Entropy: {entropy:.2f})\nSuggestions:\n" + "\n".join(feedback)


password = input("Enter a password to check its strength: ")
result = check_password_strength(password)
print(result)
