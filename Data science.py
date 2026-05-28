# Titanic Survival Prediction (Beginner Code)

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset (make sure CSV file is in same folder)
data = pd.read_csv("Titanic-Dataset.csv")

# Keep only useful columns
data = data[["Survived", "Pclass", "Sex", "Age", "Fare"]]

# Convert text to numbers
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

# Fill missing values
data["Age"] = data["Age"].fillna(data["Age"].mean())

# Input (X) and Output (y)
X = data[["Pclass", "Sex", "Age", "Fare"]]
y = data["Survived"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# ---- TEST NEW INPUT ----
print("\nEnter passenger details:")

pclass = int(input("Class (1/2/3): "))
sex = int(input("Sex (0=Male, 1=Female): "))
age = float(input("Age: "))
fare = float(input("Fare: "))

result = model.predict([[pclass, sex, age, fare]])

if result[0] == 1:
    print("Survived")
else:
    print("Did not survive")