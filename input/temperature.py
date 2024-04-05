'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from sensor import Sensor

class Temperature (Sensor):
    def __init__(self):
        super("I2C", -1)

    def getName(self):
        return __name__
    
    def getValue(self):
        return self.measureI2C()