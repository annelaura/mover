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

# Create toggles for motor directions
toggle_forward = st.toggle("Forward")
toggle_backward = st.toggle("Backward")
toggle_left = st.toggle("Left")
toggle_right = st.toggle("Right")

# Create toggles for individual pins
toggle_pin_17 = st.toggle("Pin 17")
toggle_pin_18 = st.toggle("Pin 18")
toggle_pin_22 = st.toggle("Pin 22")
toggle_pin_27 = st.toggle("Pin 27")

# GPIO control logic based on motor direction toggles
if toggle_forward:
    stop_motors()
    for pin in motor_pins['forward']:
        GPIO.output(pin, GPIO.HIGH)
    st.write('Motors moving forward')
else:
    for pin in motor_pins['forward']:
        GPIO.output(pin, GPIO.LOW)

if toggle_backward:
    stop_motors()
    for pin in motor_pins['backward']:
        GPIO.output(pin, GPIO.HIGH)
    st.write('Motors moving backward')
else:
    for pin in motor_pins['backward']:
        GPIO.output(pin, GPIO.LOW)

if toggle_left:
    stop_motors()
    for pin in motor_pins['left']:
        GPIO.output(pin, GPIO.HIGH)
    st.write('Motors turning left')
else:
    for pin in motor_pins['left']:
        GPIO.output(pin, GPIO.LOW)

if toggle_right:
    stop_motors()
    for pin in motor_pins['right']:
        GPIO.output(pin, GPIO.HIGH)
    st.write('Motors turning right')
else:
    for pin in motor_pins['right']:
        GPIO.output(pin, GPIO.LOW)

# GPIO control logic based on individual pin toggles
GPIO.output(17, GPIO.HIGH if toggle_pin_17 else GPIO.LOW)
GPIO.output(18, GPIO.HIGH if toggle_pin_18 else GPIO.LOW)
GPIO.output(22, GPIO.HIGH if toggle_pin_22 else GPIO.LOW)
GPIO.output(27, GPIO.HIGH if toggle_pin_27 else GPIO.LOW)

# Cleanup on exit
st.write("Use Ctrl+C in the terminal to stop the app")
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
