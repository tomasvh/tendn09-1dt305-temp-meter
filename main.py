# main.py -- put your code here!

import machine
import time
import pycom

import analogTemp
import ds18b20

# Disabling flashing led on Fipy/Lopy
pycom.heartbeat(False)

# Sleep time 15 minutes
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