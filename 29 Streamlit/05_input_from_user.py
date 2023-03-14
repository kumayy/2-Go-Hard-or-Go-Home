# core pkgs
import streamlit as st

# ----INPUT FROM USER-----

# Text input
fname = st.text_input("Enter Name", max_chars=20)
st.title(fname)

# password
password = st.text_input("Entert Password", type="password")
st.title(password)

# text area
message = st.text_area("Enter Message", height=200)
st.write(message)

# number input
number = st.number_input("Enter Number")
number = st.number_input("Enter Number", 1, 100)
number = st.number_input("Enter Number", 1., 10.0)

# date input
mydate=st.date_input("Appointment")

# color picker
color = st.color_picker("Select Color")