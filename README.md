# mover

# to set up raspberry pi:
1. connect to 5v - 2.5A power supply
2. download raspberry pi software to macbook from raspberrypi.com, install and upload software to miniSD
3. plug miniSD into raspberry pi, set up user, pwd and wifi
4. ssh from mac to raspberry based on ip address from pi: ssh annelaura@192.168.8.100, pwd: raspberrypi
5. sudo mkdir FH/mover

# create venv:
python3 -m venv mover
pip install streamlit

# setup startup service:
cp /home/annelaura/FH/mover/service_mover.service /etc/systemsd/system/service_mover.service
sudo chmod +x start_mover.sh


# hardware setup
**1. Components Overview & Wiring Considerations
Raspberry Pi 3B+: The central controller, running Streamlit and sending control signals.
8-Relay Module: Used to control the high-power relays or directly control the motors if within its rating.
80A Relays: These will handle the high current for your motors.
12V Battery: Powers the motors and the high-power relays.
DC-DC Converter: Step down the 12V from the battery to 5V for the Raspberry Pi and possibly the relay module.
Schottky Rectifying Diodes: Used for flyback protection, preventing voltage spikes when switching the motors.
**2. Power Distribution
Powering the Raspberry Pi:

Use the DC-DC converter to step down the 12V from the battery to 5V, ensuring it can provide sufficient current (at least 2.5A for the Pi 3B+).
Connect the output of the DC-DC converter to the 5V and GND pins of the Raspberry Pi.
Powering the Relays:

If your relay module requires 5V, it can share the DC-DC converter output with the Raspberry Pi. Otherwise, if it needs 12V, connect it directly to the 12V battery.
Powering the Motors:

The motors will be powered directly from the 12V battery, controlled through the 80A relays.
**3. Relay Control
Connecting the 8-Relay Module to the Raspberry Pi:

Connect the control pins of the relay module to the GPIO pins on the Raspberry Pi. Make sure to also connect the GND of the relay module to the GND of the Raspberry Pi to establish a common ground.
For example, if using GPIO17 and GPIO18 for control, connect them accordingly to the relay module inputs.
Connecting the 80A Relays:

Use the 8-relay module to control the 80A relays. The low-power relays on the module will switch the higher power 80A relays, which in turn will control the motors.
Connect the output of each relay on the relay module to the control input of the corresponding 80A relay.
**4. Motor Control Wiring
Connecting the Motors to the 80A Relays:
Wiring: Connect the battery's positive terminal to the common terminal of the 80A relay. Connect the normally open (NO) terminal of the relay to the positive terminal of the motor. The negative terminal of the motor goes directly to the battery's negative terminal.
Diodes for Flyback Protection: Place the Schottky diodes across the motor terminals (cathode to positive, anode to negative) to protect against voltage spikes caused by the inductive load of the motors.

# 

Your setup involves controlling DC motors for a robot, which requires handling both forward and reverse motion. The current setup you described for the doors involves using relays to switch the polarity of the power supplied to actuators, allowing for movement in both directions. A similar concept will apply to your robot's motors, but we need to handle higher currents, hence the use of 80A relays.

Understanding the 80A Relay Pin Configuration
For automotive-style relays with five flat pins, the typical configuration is:

Pin 30 (Common, COM): The power input pin. Connects to the positive terminal of the power source.
Pin 87 (Normally Open, NO): This terminal is connected to the common terminal (Pin 30) when the relay coil is energized. Typically connects to the load (e.g., motor terminal).
Pin 87a (Normally Closed, NC): This terminal is connected to the common terminal (Pin 30) when the relay coil is not energized.
Pin 85 (Coil Negative): Connects to the ground side of the relay coil.
Pin 86 (Coil Positive): Connects to the control signal that energizes the coil (typically from the relay module).
Wiring Diagram for Motor Control
To control the direction of the motors, you need an H-bridge configuration using the relays. Here’s a basic outline of how to wire this:

Motor Control with Relays Setup
For each motor, you will use two 80A relays in the following way:

Power Connections:

Connect the positive terminal of the 12V battery to Pin 30 of both relays.
Connect the negative terminal of the 12V battery to Pin 85 of both relays (assuming the relay module provides the 5V control signal, which is isolated from the 12V system).
Motor Connections:

Motor Positive Terminal: Connect this to Pin 87 of the first relay.
Motor Negative Terminal: Connect this to Pin 87 of the second relay.
Relay Control:

Connect Pin 86 of each relay to a respective GPIO pin via the relay module. This will allow you to control the relay state via the Raspberry Pi.
Common Ground: Ensure that the Raspberry Pi, the 8-channel relay module, and the 80A relays share a common ground.
Jumper Connections:

For reversing the motor direction, create a jumper wire that connects Pin 87a of the first relay to Pin 87 of the second relay, and vice versa.
Operational Description
Forward Motion: Energize the first relay, connecting Pin 30 (12V) to the motor's positive terminal, while the second relay remains off, connecting the motor's negative terminal to the ground.
Reverse Motion: Energize the second relay, connecting Pin 30 (12V) to the motor's negative terminal, while the first relay remains off, connecting the motor's positive terminal to the ground.
Schematic Example
Here's a simplified version:

css
Copy code
[12V Battery +] --- [Pin 30, Relay A] ------------------------+
                         |                                     |
                         +-- [Pin 87, Relay A] --> Motor +     |
                                                               |
Motor                     [Pin 87a, Relay A] -- Jumper --+     |
Motor -                                                 |     |
                                                       |     |
                         +-- [Pin 87, Relay B] --> Motor -   |
                         |                                     |
[12V Battery -] --- [Pin 30, Relay B] ------------------------+
Important Notes:

Diode Protection: Place Schottky diodes across the motor terminals (cathode to positive, anode to negative) to protect against voltage spikes.
Relay Control Circuit Isolation: Ensure that the control side of the relays (Pins 85 and 86) is properly isolated from the power circuit to protect the Raspberry Pi from high currents.
Safety: Verify all connections are correct before powering on to prevent short circuits. Use appropriately rated wires to handle the current.