import streamlit as st
import pandas
st.title("Marks Prediction App")
hrs = st.slider("enter hrs",min_value=0,max_value=24)
st.write("this is final hrs",hrs)
df=pandas.read_csv("marks.csv")
import pandas
from sklearn.linear_model import LinearRegression
df=pandas.read_csv("marks.csv")
print(df)
x=df["hrs"].values.reshape(-1,1)
y=df["marks"].values.reshape(-1,1)
brain=LinearRegression()
brain.fit(x,y)
marks=brain.predict([[hrs]])
st.write("this is my final marks:",marks)