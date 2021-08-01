# main.py -- put your code here!

# Importing built in modules from the device
import machine
import time
import pycom
from network import LTE

#Importing the modules for the sensors
import analogTemp
import ds18b20

# Disabling LTE so it does not draw power.
lte = LTE()
lte.deinit()

# Disabling flashing led on Fipy/Lopy
pycom.heartbeat(False)

# Sleep time 15 minutes, this is called a delay, and is actually not a sleep and will thus not save power(Deepsleep did not play well with the digital sensor).
sleepTime = 15 * 60 

# This never turns to false and as such will continue working.
while True:
    # Collecting the air temperature data from sensor.
    airCelsius = analogTemp.readAirTemp()
    time.sleep( 1 )
    # Collecting water temperature data from sensor.
    waterCelcius = ds18b20.readWaterTemp()
    time.sleep( 1 )
    # Sending collected temperature data to pybytes through internal library.
    pybytes.send_signal( 1, airCelsius )
    pybytes.send_signal( 2,waterCelcius )
    time.sleep( 1 )
    #machine.deepsleep(1000*sleepTime)
    time.sleep(sleepTime)