import streamlit as st
import pandas as pd
import numpy as np

#app Title and Description
st.title("Streamlit App")
st.write("This is a simple app to demonstrate the basic functionalities of Streamlit.")

#interactive widgets in the sidebar
st.sidebar.header("User Input Features")

#text input
user_name = st.sidebar.text_input("What is your name?", "Arman Pathan")

#slider 
age = st.sidebar.slider("Select your age", 0,100,25)

#selectbox
favourite_color = st.sidebar.selectbox("What is your favourite color?", ["Blue", "Red", "Green", "Yellow"])

#main page content
st.header(f"Welcome, {user_name}!")
st.write(f"You are {age} years old and your favourite color is {favourite_color}.")

#displaying data
st.subheader("Here's some random data:")

#create a sample dataframe
data = pd.DataFrame(
	np.random.randn(10,5),
	columns=('col %d' % i for i in range (5))
)

st.dataframe(data)

#checkbox to show/hide content
if st.checkbox ("Show raw data"):
	st.subheader("Raw Data")
	st.write(data)

#button to trigger an action
if st.button("Say hello"):
	st.write("Hello there!")
else:
	st.write("Goodbye")
