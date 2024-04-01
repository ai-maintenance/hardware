from sensor import Sensor

class Loudness (Sensor):
    def __init__(self):
        pass

    def getName(self):
        return __name__
    
    def getValue(self):
        print("get from " + __name__)