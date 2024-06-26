'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from input.sensor import Sensor

class Temperature (Sensor):
    def __init__(self):
        super().__init__(type="I2C", pin=-1)

    def getName(self):
        return __class__.__name__
    
    def getValue(self):
        return self.measureI2C()