# Movie Rating Prediction (Beginner Level)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
# Make sure CSV file is in same folder
data = pd.read_csv("movies.csv")

# Show first rows
print("Sample Data:")
print(data.head())

# Select important columns
# (Assume dataset has these columns)
data = data[["genre", "director", "actors", "rating"]]

# Convert text data into numbers (simple encoding)
data["genre"] = data["genre"].astype("category").cat.codes
data["director"] = data["director"].astype("category").cat.codes
data["actors"] = data["actors"].astype("category").cat.codes

# Input and output
X = data[["genre", "director", "actors"]]
y = data["rating"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Error check
mse = mean_squared_error(y_test, y_pred)

print("\nModel Mean Squared Error:", mse)

# ---- USER INPUT PREDICTION ----
print("\nEnter Movie Details:")

genre = int(input("Genre code (0-...): "))
director = int(input("Director code (0-...): "))
actors = int(input("Actors code (0-...): "))

prediction = model.predict([[genre, director, actors]])

print("Predicted Movie Rating:", prediction[0])