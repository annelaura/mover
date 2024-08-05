import streamlit as st
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
motor_pins = {
    'forward': [17, 27],  # Motor 1 forward and Motor 2 forward
    'backward': [18, 22], # Motor 1 backward and Motor 2 backward
    'left': [17, 22],     # Motor 1 forward and Motor 2 backward
    'right': [18, 27],    # Motor 1 backward and Motor 2 forward
}

# Set all motor pins to output
for pin_list in motor_pins.values():
    for pin in pin_list:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

# Function to stop all motors
def stop_motors():
    for pin_list in motor_pins.values():
        for pin in pin_list:
            GPIO.output(pin, GPIO.LOW)

# Streamlit app
st.title("Motor Control")

if st.button('Forward'):
    stop_motors()
    for pin in motor_pins['forward']:
        GPIO.output(pin, GPIO.HIGH)
    st.write('Motors moving forward')

if st.button('Backward'):
    stop_motors()
    for pin in motor_pins['backward']:
        GPIO.output(pin, GPIO.HIGH)
    st.write('Motors moving backward')

if st.button('Left'):
    stop_motors()
    for pin in motor_pins['left']:
        GPIO.output(pin, GPIO.HIGH)
    st.write('Motors turning left')

if st.button('Right'):
    stop_motors()
    for pin in motor_pins['right']:
        GPIO.output(pin, GPIO.HIGH)
    st.write('Motors turning right')

if st.button('Stop'):
    stop_motors()
    st.write('Motors stopped')

# Cleanup on exit
st.write("Use Ctrl+C in the terminal to stop the app")
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
