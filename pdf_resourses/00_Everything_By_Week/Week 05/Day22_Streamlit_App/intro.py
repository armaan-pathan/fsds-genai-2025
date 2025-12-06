#import streamlit
import streamlit as st

#add a title
st.title("First Streamlit App")

#add text
st.write("Welcome! This app calculates the square of a number.")

#create an interactive slider
st.header("Select a Number")
number = st.slider("Pick a number", 0,100,25) #min,max,default

#calculate and display the result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")



#import streamlit as st: This line imports the Streamlit library, which is the only dependency you need.
#st.title(): This command sets the main title that appears at the top of your web app.
#st.write(): A versatile command used to write text, numbers, or even dataframes to the app.
#st.header() and st.subheader(): These are for creating section headings of different sizes.
#st.slider(): This is an interactive widget. It creates a slider that lets the user select a number. The selected value is stored in the number variable.
