import streamlit as st

st.title("Welcome to the Fun Web App!")
st.write("Hi! Let's play a quick game.")

# Ask for the user's name
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Nice to meet you!")

# Ask for the user's age
age = st.number_input("How old are you?", min_value=1, max_value=120, step=1)
if age:
    st.write(f"Wow, {name}, you're {age} years old!")

# Add fun buttons
st.write("Click a button below to have some fun:")
if st.button("Click Right"):
    st.write("You clicked RIGHT! 🎉")
if st.button("Click Left"):
    st.write("You clicked LEFT! 🚀")