import streamlit as st 
import joblib

model = joblib.load('my_salary.pkl')
st.title("Salary Prediction")
st.write("Enter Yours Years of experience ")
Salary = st.number_input("Enter your number of years",min_value = 0 , max_value = 100)
if st.button("Predict"):
  result = model.predict([[Salary]])
  st.success(f"Your predicted salary is ₹{result[0]:,.2f}")
