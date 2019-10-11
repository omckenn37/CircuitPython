# Owen McKenney
# Photointerrupter
# This code counts the number of interruptions on a photointerurper
# And prints the total interruptions every 4 seconds

import board
import digitalio
import time
import adafruit_bus_device

# Pin setup for the photointerrupter
photoPin = digitalio.DigitalInOut(board.D8)
photoPin.direction = digitalio.Direction.INPUT
photoPin.pull = digitalio.Pull.UP


interrupts = -1 # This sets the inital interrupts at -1
initial = time.monotonic() # This sets the initial time to time.monotonic()
fread = True
lread = True

while True:
    now = time.monotonic()
    if now - initial == 4: # This if statement prints out the number of interruptions every 4 seconds
        print("Number of interruptions: " + str(interrupts))
        initial = time.monotonic()

    if photoPin.value: # This sees if the photointerrupter is being interrupted
        lread = True # If it is interrupter, lread is true

    elif fread == lread: # if both the booleans are true, then the interrupts increases
        interrupts +=1
        lread = not lread