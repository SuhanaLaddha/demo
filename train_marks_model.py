import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("student_scores.csv")  
print("Dataset preview:\n", data.head())

X = data[['Hours']]   # Input feature
y = data['Marks']     # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "marks_predictor.pkl")
print("✅ Model trained and saved as marks_predictor.pkl")
