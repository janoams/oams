import streamlit as st


# App Title
st.title("🎉 Welcome to the Fun App!")


st.title("OAMS TOWER!")
st.write("Hi! Lets have some FUN!")

# Ask for the user's name
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Nice to meet you! {name}, from Mazar-e-Sharif!")

# Ask for the user's age
age = st.number_input("How old are you?", min_value=1, max_value=120, step=1)
if age:
    st.write(f"Wow, {name}, you're {age} years old!")


# Ask for the user's Weight
weight = st.number_input("How much do you weigh?", min_value=1, max_value=10000, step=1)
if weight:
    st.write(f"you're {weight} Kg!")

if weight > 100:
    st.write(f"sorry, {name} ,you might be overweight , Go to Gym, Please!")

elif (weight) < 50:
    st.write(f"Hmm, {name} , you might be thin ,but healthy!")

else:
    st.write(f"WOW, {name} , you are Perfect , Stay Healthy!")



# Add a background image
st.markdown(
    """
    <style>
    body {
        background-image: url('https://cdn.jetphotos.com/640/6/805522_1722696080.jpg');
        background-size: cover;
        color: white;  /* Text color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)



# Add a fun image
st.image(
    "https://www.airportzentrale.de/wp-content/uploads/2017/04/Mazar-1.jpg",
    caption="Let's have fun together!",
    use_container_width=True,  # Fixed warning
)

# Quiz Section
st.header("🧠 Quick Quiz!")

# Quiz question
question = st.radio(
    "What is the capital of Afghanistan?",
    options=["Berlin", "Tehran", "Mazar e Sharif", "Kabul"],
)

# Submit button for the quiz
if st.button("Submit Answer", key="quiz_button"):
    if question == "Kabul":
        st.success("Correct! 🎉 Kabul is the capital of Afghanistan.")
    else:
        st.error("Oops! That's not correct. Try again!")

# Add a fun button interaction
if st.button("Click Me for a Surprise!", key="fun_button"):
    st.balloons()  # Balloons animation for fun!



# Add fun buttons
st.write("Click one of the following button to start your Shift:")
if st.button("Button 1"):
    st.write("You are on position Alpha! 🎉")
    # Add custom HTML for animation
    st.markdown(
        """
        <style>
        @keyframes fly {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }

        .plane {
            position: relative;
            display: inline-block;
            animation: fly 5s linear infinite;
        }
        </style>

        <div style="font-size: 50px; overflow: hidden;">
            ✈️ <span class="plane">Flying Plane!</span> ✈️
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("Watch the planes fly across the screen! 🚀")
if st.button("Button 2"):
    st.write("You are on position Bravo! 🚀")
if st.button("Button 3"):
    st.write("You are on Break! Go to the Shift-room and enjoy your Sleep!")

# Footer message
st.write("Thank you for using this app! Now lets play Ludo!")
import random

st.title("🎲 Ludo Dice Roller")

if st.button("Roll the Dice"):
    dice_value = random.randint(1, 6)
    st.write(f"🎲 You rolled a {dice_value}!")

# Add fun buttons
st.write("click to say Bye")
if st.button("Good Bye"):
    st.write("🎉 JUST FUN! BEST WISHES! 🎉")
