'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from grove.adc import ADC
import RPi.GPIO as GPIO
import board
import busio
import adafruit_mcp9808

class Sensor:
    def __init__(self, type, pin):
        self.pin = pin
        self.destructor = False
        
        GPIO.setmode(GPIO.BCM)

        if(type == 'ANALOG'):   # analog chanle init
            self.adc = ADC()

        elif(type == 'DIGITAL'):    # digital chanle init
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        elif(type == 'I2C'):    # i2c temperatore chanle init
            i2c = busio.I2C(board.SCL, board.SDA)
            self.mcp = adafruit_mcp9808.MCP9808(i2c)

        elif(type == 'SIGNAL'): # signal recording led chanle init 
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            self.destructor = True

        else:   # invalid type
            exit(1)
            
    def measureAnalog(self):
        return self.adc.read(self.pin)

    def measureDigial(self):
        return GPIO.input(self.pin)

    def measureI2C(self):
        return self.mcp.temperature
    
    def __del__(self):
        if(self.destructor == True):
            GPIO.output(self.pin, GPIO.HIGH)
            print("STOP RECORDING")