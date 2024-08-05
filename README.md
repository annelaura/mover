# mover

# to set up raspberry pi:
1. connect to 5v - 2.5A power supply
2. download raspberry pi software to macbook from raspberrypi.com, install and upload software to miniSD
3. plug miniSD into raspberry pi, set up user, pwd and wifi
4. ssh from mac to raspberry based on ip address from pi: ssh annelaura@192.168.8.100, pwd: raspberrypi
5. sudo mkdir FH/mover

# create venv:
python3 -m venv myvenv
pip install streamlit

# setup startup service:
cp /home/annelaura/FH/mover/service_mover.service /etc/systemsd/system/service_mover.service
sudo chmod +x start_mover.sh


