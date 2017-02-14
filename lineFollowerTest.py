import lineSensor
import time

line = lineSensor.LineSensor(9, 10, 11)

while True:
    read_line = line.read()
    print (read_line)
    time.sleep(1)
