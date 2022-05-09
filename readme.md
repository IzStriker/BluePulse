#Bluepulse
PoC for attendance based off bluetooth. Detecting how close devices are isn't too straight forward via python, so isn't included. Written and tested on a Raspberry Pi.

## Install

```
sudo apt install bluetooth libbluetooth-dev bluez influxdb
pip3 install pybluez bluz python-bluez influxdb
```

## Setup

```
sudo service influxdb start
influxd
python3 setupDB.py
```

## Run
The following to read local bluetooth devices
```
python3 main.py
``` 
Then the following to ouput the data
```
python3 readData.py
```
