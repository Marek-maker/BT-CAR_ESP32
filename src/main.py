from motors import Motor
from machine import Pin, PWM
from time import sleep
from neopixel import NeoPixel
from hcsr04 import HCSR04



motor1 = Motor(Pin(15, Pin.OUT), Pin(2, Pin.OUT))
motor2 = Motor(Pin(0, Pin.OUT), Pin(4, Pin.OUT))

motor1.stop()
motor2.stop()

"""
np = NeoPixel(Pin(X), 1)
np[0] = (255, 0, 0)
np.write()


buzzer = PWM(Pin(33), freq=50, duty_u16=32768)


np = NeoPixel(Pin(13), 3)
np[0] = (255, 0, 0)
np[1] = (0, 255, 0)
np[2] = (0, 0, 255)
np.write()


dist_sensor = HCSR04(trigger_pin=x, echo_pin=y)
"""


