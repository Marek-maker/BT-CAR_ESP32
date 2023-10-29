class Motor:
    def __init__(self, pin1, pin2):  #pinx = Pin(y, Pin.OUT)  
        self.pin1 = pin1
        self.pin2 = pin2
        
    def forward(self):
        self.pin1.value(1)
        self.pin2.value(0)
    
    def backward(self):
        self.pin1.value(0)
        self.pin2.value(1)
        
    def stop(self):
        self.pin1.value(0)
        self.pin2.value(0)
        
