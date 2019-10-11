# Owen McKenney
# Ultrasonic Sensor
# This code gets the distance from an ultrasonic sensor
# then displays that distance as a color on the onboard LED

import board
import neopixel
import time
import adafruit_hcsr04
import simpleio

# Setup for ultrasonic sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5)

# Setup for onboard RGB LED
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = .1)

# Setting red, green, and blue to 0
r = 0
g = 0
b = 0

while True:

    try: # This tries all of the below code first
        print((sonar.distance,)) # This prints the distance in cm 
        if sonar.distance <= 20:

            # These lines map the distance to 255 so that the color can be on the range of 0-35
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 5,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        else:
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 35,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        dot.fill((int(r),int(g),int(b))) # This sets the RGB LED to the right color
    except RuntimeError: # If there is an error with gathering the distance, Error is printed
        print("Error")

    time.sleep(0.1)