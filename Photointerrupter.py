# Owen McKenney
# Photointerrupter
# This code counts the number of interruptions on a photointerurper
# And prints the total interruptions every 4 seconds

import board
#import neopixel
import digitalio
import time
import adafruit_bus_device

photoPin = digitalio.DigitalInOut(board.D8)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP
interrupts = -1
initial = time.monotonic()
fread = True
lread = True

while True:
    now = time.monotonic()
    if now - initial == 4:
        print("Number of interruptions: " + str(interrupts))
        initial = time.monotonic()

    if photoPin.value:
        lread = True

    elif fread == lread:
        interrupts +=1
        lread = not lread