import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from features import extract_features

# Load dataset
df = pd.read_csv("password_dataset.csv")

# Convert dataset into features
X = df["password"].apply(extract_features).apply(pd.Series)
y = df["strength"]

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# Save model
with open("password_strength_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")
