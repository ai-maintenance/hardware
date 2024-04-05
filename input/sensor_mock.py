'''
author: GAL ASHKENAZI
date:   04/04/2024
'''

class Sensor:
    def __init__(self, type, pin):
        self.pin = pin
        
        if(type == 'ANALOG'):
            print(f'Setup analog {pin}')

        elif(type == 'DIGITAL'):
            print(f'Setup digital {pin}')
            
        elif(type == 'I2C'):
            print(f'Setup i2c')
        else:   # invalid type
            exit(1)
            
    def measureAnalog(self):
        return 999

    def measureDigial(self):
        return 999

    def measureI2C(self):
        return 999