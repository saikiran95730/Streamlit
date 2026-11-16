import streamlit as st

# Add some title
st.title('My first streamlit app by Mr. P Sai Kiran')

# Add something inside
st.write('This is calculates square of the number, welcome')

# Create an interactive slider
st.header('Select a number')
number = st.slider('Pick a number', 0, 8, 15) # min, max, default

# calculate and display result
st.subheader('Result')
squared_number = number * number
st.write(f'The square of the **{number}** is **{squared_number}**')

# import streamlit as st: This line imports the Streamlit library, which is the only dependency you ner 
# st.title(): This command sets the main title that appears at the top of your web app. 
# st.write(): A versatile command used to write text, numbers, or even dataframes to the app. 
# st.header() and st.subheader(): These are for creating section headings of different sizes.
#st.slider(): This is an interactive widget. It creates a slider that lets the user select a number.