class LINE_SCANNER:
    def __init__(self, left_sensor, middle_sensor, right_sensor): #sensors must be entered as a ready object of the IR_SENSOR class defined in the ir_sensor.py file
        self.left_sensor = left_sensor
        self.middle_sensor = middle_sensor
        self.right_sensor = right_sensor
        
    def get_line_scan(self):
        return [left_sensor.read_digital, middle_sensor.read_digital, right_sensor.read_digital]
        

