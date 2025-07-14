import streamlit as st
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
st.title("CGPA Prediction")
name = st.text_input("Enter your name: ")
age = st.number_input("enter the age", min_value=0,max_value=120)
number = st.number_input("Enter the mobile number: ")
address = st.text_input("Enter your address:")
import streamlit as st

uploaded_files = st.file_uploader(
    "Choose a file containing your passport size photo and aadhar card pic", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
days = st.number_input("Enter the number of days you studied:", min_value=0, step=1)
base_cgpa = 5.0 
factor = 0.06
predicted_cgpa = base_cgpa + (factor * days)
predicted_cgpa = min(max(predicted_cgpa, 0), 10)
st.write(f" Predicted CGPA: **{predicted_cgpa:.2f}**")
if days < 10:
    st.info("Try to study more days to improve your CGPA.")
elif days > 100:
    st.success("Great dedication! Keep it up.")  
st.subheader(" Study Progress")
st.progress(min(days, 100) / 100)

if name and address:
    data = {
        "Name": [name],
        "Age": [age],
        "Mobile Number": [number],
        "Address": [address],
        "Days Studied": [days],
        "Predicted CGPA": [predicted_cgpa]
    }

    df = pd.DataFrame(data)

    csv = df.to_csv(index=False)

    st.download_button(" Download Info as CSV", data=csv, file_name="user_info.csv", mime="text/csv")
  

