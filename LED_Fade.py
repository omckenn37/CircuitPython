# Owen McKenney
# LED fade
# This makes and LED fade from off to on

import board
import neopixel
import digitalio
import analogio
import time
import simpleio

led = analogio.AnalogOut(board.A0) # LED setup

while True:
    for i in range(31000, 42000, 1): # for loop to go between 31k and 42k by 1
        led.value = i # sets LED brightness to i
        print(i) # prints value in serial monitor
    for i in range(42000, 31000, -1):
        led.value = i
        print(i)