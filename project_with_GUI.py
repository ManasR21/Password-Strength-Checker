import tkinter as tk
from tkinter import messagebox
import string
import math
import os

# Existing functions for password checking
def check_against_rockyou(password, rockyou_path="rockyou.txt"):
    if not os.path.exists(rockyou_path):
        return False
    
    with open(rockyou_path, 'r', encoding='latin-1') as file:
        for line in file:
            if password.strip() == line.strip():
                return True
    return False

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

def classify_strength(brute_force_times, is_in_rockyou, password):
    if is_in_rockyou:
        return "Critical: This password is in a commonly used password list. It is very unsafe to use. Try a unique password with a mix of characters."

    fast_attack_time = brute_force_times["Fast attack (1 billion guesses/sec)"]

    if "seconds" in fast_attack_time or "minutes" in fast_attack_time:
        return "Very Weak: Easy to crack in seconds! Use a stronger password with a mix of characters."
    elif "hours" in fast_attack_time or "days" in fast_attack_time:
        return "Weak: Vulnerable to attacks. Add more characters or symbols."
    elif "years" in fast_attack_time:
        years = float(fast_attack_time.split()[0])
        if years < 100:
            return "Moderate: Decent, but could be stronger with more characters or symbols."
        elif years < 1000:
            return "Strong: Takes centuries to crack. Good job!"
        else:
            return "Excellent: Extremely strong! Keep it up!"

# GUI Functionality
def check_password_gui():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password!")
        return

    is_in_rockyou = check_against_rockyou(password)
    entropy = calculate_entropy(password)
    brute_force_times = calculate_brute_force_time(entropy)
    strength_message = classify_strength(brute_force_times, is_in_rockyou, password)

    # Display results in the GUI
    result_text.set(f"Password Entropy: {entropy:.2f} bits\n\n"
                    f"Estimated Brute-Force Times:\n"
                    + "\n".join(f"- {k}: {v}" for k, v in brute_force_times.items()) +
                    f"\n\nPassword Strength: {strength_message}")

# Tkinter GUI
app = tk.Tk()
app.title("Password Strength Checker")

# Widgets
tk.Label(app, text="Enter Password:", font=("Arial", 14)).pack(pady=10)
password_entry = tk.Entry(app, width=40, font=("Arial", 14), show="*")
password_entry.pack(pady=10)

check_button = tk.Button(app, text="Check Password Strength", font=("Arial", 12), command=check_password_gui)
check_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 12), justify="left", wraplength=500)
result_label.pack(pady=10)

# Run the app
app.mainloop()
