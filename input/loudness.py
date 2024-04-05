'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from input.sensor import Sensor
import os
from dotenv import main

main.load_dotenv()
PIN = int(os.environ.get("PIN_LOUDNESS"))

class Loudness (Sensor):
    def __init__(self):
        super().__init__("ANALOG", PIN)

    def getName(self):
        return __class__.__name__
    
    def getValue(self):
        return self.measureAnalog()