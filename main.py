'''
author: GAL ASHKENAZI
date:   04/04/2024
'''
from input.sensor import Sensor
from input.temperature import Temperature 
from input.gas import Gas 
from input.loudness import Loudness 
from input.vibration import Vibration 
from input.microphone import Microphone 

from output.output import CSV

import datetime
import time
import os
from python_dotenv import load_dotenv

load_dotenv()
FREQ = float(os.environ.get("FREQ"))

def getAllSensors():
    sensors = []
    sensor = [Sensor]
    
    while sensor:
            parent = sensor.pop()
            for child in parent.__subclasses__():
                if child not in sensors:
                    sensors.append(child())
                    sensor.append(child)

    return sensors

def getAllSensorsName(sensors):
     return [s.getName() for s in sensors] 
     
def getAllSensorsValue(sensors):
     return [s.getValue() for s in sensors] 

if __name__ == '__main__':
    sensors = getAllSensors()   # get all sensors exist

    directory_name = datetime.datetime.now().strftime("record %d_%m_%Y %H_%M_%S")       # call the folder by date and time (recod DAY_MONTH_YEAR HOUR_MINUTH_SECOND)
    output = CSV(directory_name= directory_name, header=getAllSensorsName(sensors))

    # run forever
    while(True):
        time.sleep(FREQ)

        output.write(getAllSensorsValue(sensors))
         