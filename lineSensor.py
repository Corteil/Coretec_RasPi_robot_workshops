import RPi.GPIO as GPIO


class LineSensor:
    def __init__(self, left, middle, right):
        self._left = left
        self._middle = middle
        self._right = right
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([left, middle, right], GPIO.IN)

    def read(self):
        left_sensor, middle_sensor, right_sensor = 0, 0, 0
        if GPIO.input(self._left) == 1:
            left_sensor = 1
        if GPIO.input(self._middle) == 1:
            middle_sensor = 1
        if GPIO.input(self._right) == 1:
            right_sensor = 1
        values = {"left": left_sensor, "middle": middle_sensor, "right": right_sensor}
        return values
