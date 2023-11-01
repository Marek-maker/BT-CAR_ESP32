from machine import Pin, ADC

class IR_SENSOR:
    def __init__(self, pin):
        self.pin = ADC(Pin(pin))
        self.pin.atten(ADC.ATTN_11DB)
        
    def read(self):
        # return self.pin.read()
        
        
        
        if self.pin.read() < 3:
            return "black"
        else:
            return "white"
        



