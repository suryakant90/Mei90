import streamlit as st
import random

# Set page title and header
st.title("Number Guessing Game")
st.write("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Set number of attempts
attempts = 0
max_attempts = 5

# Create a text input for user to input their guess
guess = st.number_input("Enter your guess (between 1 and 100):", min_value=1, max_value=100, step=1)

# Check if user has made a guess
if st.button("Guess"):
    attempts += 1
    # Compare user's guess with the generated number
    if guess < number_to_guess:
        st.write("Try a higher number!")
    elif guess > number_to_guess:
        st.write("Try a lower number!")
    else:
        st.write(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts!")
        st.write("Play again!")

    # Check if user has used all attempts
    if attempts == max_attempts:
        st.write(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
        st.write("Play again!")
