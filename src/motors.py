from machine import PWM

class Motor:
    def __init__(self, pin1, pin2):  #pinx = Pin(y, Pin.OUT)  
        self.pin1 = PWM(pin1)
        self.pin1.freq(256)
        self.pin2 = PWM(pin2)
        self.pin2.freq(256)
        
    def forward(self, speed):
        self.pin1.duty(speed) # speed : 0 - 1023, 1023 = 100%    min cca 150 -> weak motor
        self.pin2.duty(0)
    
    def backward(self, speed):
        self.pin1.duty(0)
        self.pin2.duty(speed) # speed : 0 - 1023, 1023 = 100%
        
    def stop(self):
        self.pin1.duty(0)
        self.pin2.duty(0)
        

