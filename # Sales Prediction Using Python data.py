# Sales Prediction Using Python

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create sample data
data = {
    "TV": [230, 44, 17, 151, 180, 8, 57, 120, 200, 66],
    "Radio": [37, 39, 45, 41, 10, 48, 32, 19, 25, 12],
    "Newspaper": [69, 45, 69, 58, 58, 75, 23, 11, 40, 18],
    "Sales": [22, 10, 9, 18, 15, 7, 12, 13, 20, 11]
}

# Convert data into dataframe
df = pd.DataFrame(data)

# Display data
print("Dataset")
print(df)

# Input features
x = df[["TV", "Radio", "Newspaper"]]

# Output value
y = df["Sales"]

# Split data into training and testing
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1
)

# Create model
model = LinearRegression()

# Train model
model.fit(x_train, y_train)

# Predict sales
prediction = model.predict(x_test)

# Display predictions
print("\nPredicted Sales")
print(prediction)

# Take user input
tv = float(input("\nEnter TV Advertising Budget: "))
radio = float(input("Enter Radio Advertising Budget: "))
news = float(input("Enter Newspaper Advertising Budget: "))

# Predict new sales
new_sales = model.predict([[tv, radio, news]])

# Display result
