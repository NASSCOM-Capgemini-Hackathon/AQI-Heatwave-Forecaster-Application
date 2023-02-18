import streamlit as st

# Set page title
st.set_page_config(page_title="My Streamlit App")

# Add title and subtitle to app
st.title("My Streamlit App")
st.subheader("This is a basic app using Streamlit")

# Add text to app
st.write("Hello, world!")

# Add a slider
value = st.slider("Select a value", 0, 100)

# Add a button
button = st.button("Click me!")

# Add conditional statement for button click
if button:
    st.write(f"You selected {value}")