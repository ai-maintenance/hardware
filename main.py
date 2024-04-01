from sensor import Sensor
from temperature import Temperature 
from gas import Gas 
from loudness import Loudness 
from vibration import Vibration 

def getAllSensorChild():
    sensors = set()
    sensor = [Sensor]
    
    while sensor:
            parent = sensor.pop()
            for child in parent.__subclasses__():
                if child not in sensors:
                    sensors.add(child())
                    sensor.append(child)

    return sensors

if __name__ == '__main__':
    sensors = getAllSensorChild()
    
    for s in sensors:
        print(s.getName())
