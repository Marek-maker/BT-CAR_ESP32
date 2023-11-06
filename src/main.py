from motors import Motor
from machine import Pin, PWM, ADC
from time import sleep
from neopixel import NeoPixel
from hcsr04 import HCSR04
from ir_sensor import IR_SENSOR
from time import sleep
from line_scanner import LINE_SCANNER



motor_R = Motor(Pin(15, Pin.OUT), Pin(2, Pin.OUT))
motor_L = Motor(Pin(0, Pin.OUT), Pin(4, Pin.OUT))

motor_L.stop()
motor_R.stop()

np = NeoPixel(Pin(5), 1)
np[0] = (0, 0, 0)
np.write()


ir_snsr = IR_SENSOR(34)

motor_R.forward(150)
motor_L.forward(1023)







"""
buzzer = PWM(Pin(33), freq=50, duty_u16=32768)


np = NeoPixel(Pin(13), 3)
np[0] = (255, 0, 0)
np[1] = (0, 255, 0)
np[2] = (0, 0, 255)
np.write()


dist_sensor = HCSR04(trigger_pin=x, echo_pin=y)
"""




