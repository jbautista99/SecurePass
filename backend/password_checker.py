import re


def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Password should include at least 1 uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Password should include at least 1 lowercase letter.")

    # Number Check
    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Password should include at least 1 number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        feedback.append("Password should include at least 1 special character.")

    # Bonus Points
    if len(password) >= 16:
        score += 15

    # Common Password Check
    common_passwords = ["password", "password123", "qwerty", "admin", "123455"]

    if password.lower() in common_passwords:
        score = max(score - 30, 0)
        feedback.append("This password is commonly used and easily guessable. Consider using a more unique password.")

    # Determine Strength
    if score >= 80:
        strength = "Strong"
    elif score >= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }