'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from input.sensor import Sensor
import os
from python_dotenv import load_dotenv

load_dotenv()
PIN = int(os.environ.get("PIN_VIBRATION"))

class Vibration (Sensor):
    def __init__(self):
        super().__init__("DIGITAL", PIN)

    def getName(self):
        return __name__
    
    def getValue(self):
       return self.measureDigial()