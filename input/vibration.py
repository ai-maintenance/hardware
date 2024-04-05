'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from input.sensor import Sensor
import os

PIN = os.environ["PIN_VIBRATION"]

class Vibration (Sensor):
    def __init__(self):
        super("DIGITAL")

    def getName(self):
        return __name__
    
    def getValue(self):
       return self.measureDigial(PIN)