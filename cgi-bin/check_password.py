#!/usr/bin/env python3
import cgi
import pickle
import os
import sys
import hashlib
import json

# Ensure project root is in Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from features import extract_features   # <-- from features.py

# Path to your saved ML model
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "password_strength_model.pkl")

# Load trained model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Handle form input
form = cgi.FieldStorage()
password = form.getvalue("password", "")

if password:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
else:
    hashed_password = "(empty)"

# Extract features
features = extract_features(password)
features = [features]

# Predict strength
prediction = model.predict(features)[0]

# Suggestions if weak
suggestions = []
if len(password) < 8:
    suggestions.append("Use at least 8 characters.")
if password.islower() or password.isupper():
    suggestions.append("Mix uppercase and lowercase letters.")
if not any(char.isdigit() for char in password):
    suggestions.append("Add some numbers.")
if not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/\\|" for char in password):
    suggestions.append("Add at least one special symbol.")
if password.lower() in ["password", "123456", "qwerty"]:
    suggestions.append("Avoid common patterns like 'password' or '123456'.")

# Output HTML response
print("Content-Type: application/json\n")
print(json.dumps({
    "password": password,
    "hashed_password": hashed_password,
    "prediction": prediction,
    "suggestions": suggestions
}))