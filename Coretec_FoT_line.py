Line1.py

# import required libraries

import RPi.GPIO as GPIO
import time

# define pins for the line following sensor

leftPin = 10
middlePin = 9
rightPin = 11

# Setup pins for line following sensor

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(leftPin, GPIO.IN)
GPIO.setup(middlePin, GPIO.IN)
GPIO.setup(rightPin, GPIO.IN)

# define function for reading sensor

def readInputs():
    left = 0
    middle = 0
    right = 0

    if GPIO.input(leftPin) == False:
        left = 1

    if GPIO.input(middlePin) == False:
        middle = 1

    if GPIO.input(rightPin) == False:
        right = 1

    returnValues = [left, middle, right]
    return returnValues


# main program loop, print values from sensor to the command line

while True:

    # calls the read line following sensor function and stores it in a list called line

    line = readInputs()
    
    # prints the list line to the command line
    
    print line

   # controls how fast, line is updated 

    time.sleep(0.01) # adjust if 100 per second reads if too fast or slow
