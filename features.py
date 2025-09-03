import re

def extract_features(password: str):
    
    features = {
        "length": len(password),
        "has_upper": int(any(c.isupper() for c in password)),
        "has_lower": int(any(c.islower() for c in password)),
        "has_digit": int(any(c.isdigit() for c in password)),
        "has_symbol": int(any(c in "!@#$%^&*()-_=+[]{};:,.<>?/\\|" for c in password)),
        "common_pattern": int(password.lower() in ["password", "123456", "qwerty"])
    }
    
    # Return only the values as a list (consistent order)
    return list(features.values())
   
