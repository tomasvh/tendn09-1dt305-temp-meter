from lib import onewire
import time
from machine import Pin

# Initializing DS18B20 water temperature sensor with the onewire library provided by Pycom.
ow = onewire.OneWire(Pin('P10'))
waterTemp = onewire.DS18X20(ow)

#Function to read the water temperature from the digital sensor.
def readWaterTemp():
    # The measurement comes out as a 4 digit number without decimal, so by dividing it by 100 adds the needed decimal.
    waterTemp.start_conversion()
    time.sleep(1)
    actualWaterTemp =  waterTemp.read_temp_async() /100
    time.sleep(1)
    return actualWaterTemp