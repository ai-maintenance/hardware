'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
import grove.adc import ADC
import RPi.GPIO as GPIO
import board
import busio
import adafruit_mcp9808

class Sensor:
    def __init__(self, type, pin):
        self.pin = pin

        if(type == 'ANALOG'):
            self.adc = ADC()

        elif(type == 'DIGITAL'):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DWON)

        elif(type == 'I2C'):
            i2c = busio.I2C(board.SCL, board.SDA)
            self.mcp = adafruit_mcp9808.MCP9808(i2c)

        else:   # invalid type
            exit(1)
            
    def measureAnalog(self):
        return self.adc.read(self.pin)

    def measureDigial(self):
        return GPIO.input(self.pin)

    def measureI2C(self):
        return self.mcp.temperature