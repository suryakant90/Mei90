import streamlit as st
import numpy as np
import time

# Set up the game constants
WIDTH = 600
HEIGHT = 400
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
BALL_RADIUS = 10
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Initialize the game variables
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y

# Set up the main Streamlit app
st.title("Ping Pong Game")

canvas = st.empty()

# Main game loop
while True:
    # Update the paddles based on user input
    key_pressed = st.session_state.keys_pressed if "keys_pressed" in st.session_state else []
    if "up" in key_pressed and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if "down" in key_pressed and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_dy *= -1

    # Check for collisions with paddles
    if ball_x <= PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
        ball_dx *= -1
    if ball_x >= WIDTH - PADDLE_WIDTH and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
        ball_dx *= -1

    # Clear the canvas
    canvas.clear()

    # Draw the paddles and ball
    canvas.rectangle((0, paddle1_y, PADDLE_WIDTH, paddle1_y + PADDLE_HEIGHT), color="blue")
    canvas.rectangle((WIDTH - PADDLE_WIDTH, paddle2_y, WIDTH, paddle2_y + PADDLE_HEIGHT), color="red")
    canvas.circle((ball_x, ball_y), BALL_RADIUS, color="green")

    # Pause briefly to control the speed of the game
    time.sleep(0.02)

    # Update the Streamlit app
    st.session_state.keys_pressed = []

    # Exit the game if the user closes the Streamlit app
    if not canvas:
        break
