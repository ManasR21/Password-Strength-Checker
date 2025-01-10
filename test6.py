
#6 Password Strength Checker with Strength Descriptions


import string
import math

# Calculate brute-force time
def calculate_brute_force_time(entropy):
    # Guess rates (in guesses per second)
    guess_rates = {
        "Slow attack (1,000 guesses/sec)": 1_000,
        "Moderate attack (1 million guesses/sec)": 1_000_000,
        "Fast attack (1 billion guesses/sec)": 1_000_000_000,
    }
    
    times = {}
    combinations = 2 ** entropy  # Total possible combinations
    for attack_type, guesses_per_second in guess_rates.items():
        seconds = combinations / guesses_per_second
        times[attack_type] = seconds_to_human_readable(seconds)
    return times

# Convert seconds into a human-readable format
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

# Determine password strength and provide creative feedback
def classify_strength(brute_force_times):
    fast_attack_time = brute_force_times["Fast attack (1 billion guesses/sec)"]

    if "seconds" in fast_attack_time or "minutes" in fast_attack_time:
        return "Very Weak: This password is so weak that even a novice hacker can crack it in no time!"
    elif "hours" in fast_attack_time or "days" in fast_attack_time:
        return "Weak: This password might hold up for a while, but it's still vulnerable to a determined hacker."
    elif "years" in fast_attack_time:
        years = float(fast_attack_time.split()[0])
        if years < 100:
            return "Moderate: This password is decent, but advanced hackers or computers could still crack it."
        elif years < 1000:
            return "Strong: This password would take centuries to crack. You're doing great!"
        else:
            return "Excellent: Even the world's most powerful computers would take millennia to crack this password!"

# Main password strength checker
def check_password_strength(password):
    entropy = calculate_entropy(password)
    brute_force_times = calculate_brute_force_time(entropy)
    strength_message = classify_strength(brute_force_times)

    print(f"\nPassword Entropy: {entropy:.2f} bits")
    print("\nEstimated Brute-Force Times:")
    for attack_type, time in brute_force_times.items():
        print(f"- {attack_type}: {time}")
    print(f"\nPassword Strength: {strength_message}")

# Input from user
password = input("Enter a password to check its strength: ")
check_password_strength(password)
