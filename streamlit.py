import streamlit as st
st.title("hello world")
st.write("helo world")
st.header("hello world")

name = st.text_input("Enter your name: ")
st.write("hello",name)
age = st.number_input("enter the age", min_value=0,max_value=120)
option = st.seclectbox("How would you connected?"),
("email","home phone","mobile phone")

st.file_upload
