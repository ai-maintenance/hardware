'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from input.sensor import Sensor
import os
from python_dotenv import load_dotenv

load_dotenv()
PIN = int(os.environ.get("PIN_LOUDNESS"))

class Loudness (Sensor):
    def __init__(self):
        super().__init__("ANALOG", PIN)

    def getName(self):
        return __name__
    
    def getValue(self):
        return self.measureAnalog()