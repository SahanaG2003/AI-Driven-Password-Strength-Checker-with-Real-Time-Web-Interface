import random
import string
import hashlib
import pandas as pd

# Common weak patterns
COMMON_PATTERNS = ["password", "123456", "qwerty", "abc123"]

# Function to generate a random password
def generate_password():
    length = random.randint(5, 16)
    chars = string.ascii_letters + string.digits + "@$!%*?&#"
    return ''.join(random.choice(chars) for _ in range(length))

# Function to hash password
def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

# Function to evaluate strength
def evaluate_password(pw):
    reasons = []
    length = len(pw)
    upper = any(c.isupper() for c in pw)
    lower = any(c.islower() for c in pw)
    digit = any(c.isdigit() for c in pw)
    symbol = any(c in "@$!%*?&#" for c in pw)

    # Common patterns
    if pw.lower() in COMMON_PATTERNS:
        return "Weak", "Contains common pattern (e.g., 'password', '123456')"

    # Length check
    if length < 8:
        return "Weak", "Too short (<8 characters)"

    # Character type checks
    if not upper:
        reasons.append("Add at least one uppercase letter")
    if not lower:
        reasons.append("Add at least one lowercase letter")
    if not digit:
        reasons.append("Include at least one number")
    if not symbol:
        reasons.append("Include at least one special character (@, #, $, etc.)")

    # Strength classification
    if reasons:  # Missing requirements
        return "Medium", ", ".join(reasons)
    elif length >= 12 and upper and lower and digit and symbol:
        return "Very Strong", "Good balance of characters"
    else:
        return "Strong", "Good balance of characters"

# Generate dataset
def generate_dataset(n=1000):
    data = []
    for _ in range(n):
        pw = generate_password()
        hashed = hash_password(pw)
        strength, reason = evaluate_password(pw)
        data.append([pw, hashed, strength, reason])
    return pd.DataFrame(data, columns=["password", "hashed_password", "strength", "weak_property"])

# Generate 1000 rows
df = generate_dataset(1000)
df.to_csv("password_dataset.csv", index=False)

print(df.head(10))
print("\nDataset saved as 'password_dataset.csv' with", len(df), "rows.")
