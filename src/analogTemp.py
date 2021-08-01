#Importing built in module
import machine

# Initializing the analog temperature sensor and disclosing what pin it is connected to.
adc = machine.ADC()
apin = adc.channel(pin='P16')

# Function to read the temperature from the analog sensor on the board.
def readAirTemp():
    # Reads the voltage on the pin and converts the reading to celcius.
    millivolts = apin.voltage()
    celsius = (millivolts - 500.0) / 10.0
    return celsius