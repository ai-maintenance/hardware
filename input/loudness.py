'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from input.sensor import Sensor
import os

PIN = os.environ["PIN_LOUDNESS"]

class Loudness (Sensor):
    def __init__(self):
        super("ANALOG", PIN)

    def getName(self):
        return __name__
    
    def getValue(self):
        return self.measureAnalog()