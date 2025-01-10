import string
import math
import os
# print("Current Working Directory:", os.getcwd())

# Load RockYou.txt and check for common passwords
def check_against_rockyou(password, rockyou_path="C:/Users/Manas/Desktop/Winter Projects/Password_Strength_Checker/rockyou.txt"):
    print("Checking path:", rockyou_path)
    if not os.path.exists(rockyou_path):
        print("rockyou.txt not found! Skipping common password check.")
        return False
    
    with open(rockyou_path, 'r', encoding='latin-1') as file:
        for line in file:
            if password.strip() == line.strip():
                return True
    return False

# Calculate brute-force time
def calculate_brute_force_time(entropy):
    guess_rates = {
        "Slow attack (1,000 guesses/sec)": 1_000,
        "Moderate attack (1 million guesses/sec)": 1_000_000,
        "Fast attack (1 billion guesses/sec)": 1_000_000_000,
    }
    times = {}
    combinations = 2 ** entropy
    for attack_type, guesses_per_second in guess_rates.items():
        seconds = combinations / guesses_per_second
        times[attack_type] = seconds_to_human_readable(seconds)
    return times

# Convert seconds into human-readable format
def seconds_to_human_readable(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} days"
    else:
        return f"{seconds / 31536000:.2f} years"

# Calculate entropy
def calculate_entropy(password):
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

    if char_sets == 0:
        return 0
    return len(password) * math.log2(char_sets)

# Determine password strength with suggestions
def classify_strength(brute_force_times, is_in_rockyou, password):
    if is_in_rockyou:
        return "Critical: This password is in a commonly used password list. It is very unsafe to use."+ "\n " +" Suggestion: Try using a unique password with a mix of characters, and avoid common passwords."

    fast_attack_time = brute_force_times["Fast attack (1 billion guesses/sec)"]
    suggestion = ""

    if "seconds" in fast_attack_time or "minutes" in fast_attack_time:
        suggestion = " Suggestions: Use at least 12 characters and include a mix of upper and lower case letters, numbers, and symbols."
        return "Very Weak: This password is so weak that even a novice hacker can crack it in no time! " +"\n" +suggestion
    elif "hours" in fast_attack_time or "days" in fast_attack_time:
        suggestion = "Suggestions: Try adding more characters and special symbols to make your password stronger."
        return "Weak: This password might hold up for a while, but it's still vulnerable to a determined hacker. " + suggestion
    elif "years" in fast_attack_time:
        years = float(fast_attack_time.split()[0])
        if years < 100:
            suggestion = "Suggestions: This password is decent but can be improved by adding more characters or symbols."
            return "Moderate: This password is decent, but advanced hackers or computers could still crack it. " + suggestion
        elif years < 1000:
            suggestion = "Great job! You're doing well, but consider adding more characters or using a password manager to generate stronger passwords."
            return "Strong: This password would take centuries to crack. You're doing great! " + suggestion
        else:
            return "Excellent: Even the world's most powerful computers would take millennia to crack this password! Keep it up!"

# Main password strength checker
def check_password_strength(password, rockyou_path="C:/Users/Manas/Desktop/Winter Projects/Password_Strength_Checker/rockyou.txt"):
    is_in_rockyou = check_against_rockyou(password, rockyou_path)
    entropy = calculate_entropy(password)
    brute_force_times = calculate_brute_force_time(entropy)
    strength_message = classify_strength(brute_force_times, is_in_rockyou, password)

    print(f"\nPassword Entropy: {entropy:.2f} bits")
    print("\nEstimated Brute-Force Times:")
    for attack_type, time in brute_force_times.items():
        print(f"- {attack_type}: {time}")
    print(f"\nPassword Strength: {strength_message}")

# Input from user
password = input("Enter a password to check its strength: ")
check_password_strength(password)




















# DISCLAIMER


# The code you provided does not lie, but it makes an assumption about entropy and brute force time based on that assumption. Let's break down how the calculations work and why you might see discrepancies:

# Entropy and Brute Force Time:
# The entropy calculation in your code is based on the assumption of a perfect mix of character types (lowercase, uppercase, digits, special characters, etc.). For an 8-character password, the code assumes that all these character sets are used in the password. This is a simplified model and does not account for factors like the actual password's composition, making it an approximation rather than an exact prediction.

# Key Points to Consider:
# Entropy Calculation:

# The code calculates entropy by using a logarithmic scale based on the possible character sets. For a typical password using uppercase, lowercase, digits, and special characters, the entropy will be higher.
# The formula used is:
# entropy
# =
# length of password
# ×
# log
# ⁡
# 2
# (
# number of character sets used
# )
# entropy=length of password×log 
# 2
# ​
#  (number of character sets used)
# For an 8-character password, with a mix of all possible character sets (lowercase, uppercase, digits, and special characters), the entropy is calculated as around 52.8 bits. This would indicate a vast number of possible combinations.
# Brute-Force Time:

# Your code uses a 1 billion guesses per second brute-force speed, which is indeed quite fast for a real-world attack, but it assumes this speed is maintained constantly.
# Based on the entropy and the possible combinations, the code calculates the time required for brute-forcing the password. For an 8-character password with high entropy (if all character sets are used), the brute-force time could range from minutes to days or even months, depending on the entropy.
# Discrepancy in Time Calculations:

# If the password is composed of only lowercase letters or a small set of characters, the entropy is lower, and thus, the brute-force time is significantly shorter. This is why an 8-character password with strong entropy (using all character sets) would require a lot of time to crack with 1 billion guesses per second.
# If the password uses weak patterns or common phrases (like those found in datasets like RockYou.txt), the check against that dataset would result in a much quicker attack time.
# To Summarize:
# The code is correct, but it simplifies the problem. It calculates brute-force times based on entropy and assumes 1 billion guesses per second, which is idealized for the sake of estimation. In reality, real-world attacks may not always reach this speed, but the model gives you a rough idea of the time involved.

# Suggestions:
# To improve the estimation:

# You could refine the entropy calculation by considering the actual password structure (e.g., if the password contains only lowercase letters, digits, etc.).
# Consider adding additional datasets or even real-time attack simulations to give more accurate predictions of password strength.