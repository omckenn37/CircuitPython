import digitalio #pylint: disable-msg=import-error
import board #pylint: disable-msg=import-error
import time #pylint: disable-msg=import-error
import random

class FancyLED:

    def __init__(self, p1, p2, p3): # This __init__ gets the pins for a LED
        # Next 3 lines set each LED to each given pin
        self.led1 = digitalio.DigitalInOut(p1)
        self.led2 = digitalio.DigitalInOut(p2)
        self.led3 = digitalio.DigitalInOut(p3)

        # Basic LED setup
        self.led1.direction = digitalio.Direction.OUTPUT
        self.led2.direction = digitalio.Direction.OUTPUT
        self.led3.direction = digitalio.Direction.OUTPUT
        
    def alternate(self): # This function alternates which LEDs are on (on, off, on and off, on, off)
        
        # These lines set on, off, on
        self.led1.value = True
        self.led2.value = False
        self.led3.value = True
        time.sleep(.1)

        # These lines set off, on, off
        self.led1.value = False
        self.led2.value = True
        self.led3.value = False
        time.sleep(.1)

    def blink(self): # This function turns all of the LEDs off or all on

        # All of the LEDs on
        self.led1.value = True
        self.led2.value = True
        self.led3.value = True
        time.sleep(.1)

        # All of the LEDs off
        self.led1.value = False
        self.led2.value = False
        self.led3.value = False
        time.sleep(.1)

    def chase(self): # This function turns one on, then off, then next one on, then off. This keeps repeating

        # First LED on
        self.led1.value = True
        self.led2.value = False
        self.led3.value = False
        time.sleep(.1)

        # First LED off, second on
        self.led1.value = False
        self.led2.value = True
        self.led3.value = False

        # Second LED off, third on
        time.sleep(.1)
        self.led1.value = False
        self.led2.value = False
        self.led3.value = True
        time.sleep(.1)
    
    def sparkle(self):

        n = random.randint(1, 3) # This selects a random number between 1 and 3, including 1 and 3

        if n == 1: # If the random number is 1, turn 1st LED on then off
            self.led1.value = True
            time.sleep(.5)
            self.led1.value = False
        elif n == 2: # If the random number is 2, turn 2nd LED on then off
            self.led2.value = True
            time.sleep(.5)
            self.led2.value = False
        elif n == 3: # If the random number is 3, turn 3rd LED on then off
            self.led3.value = True
            time.sleep(.5)
            self.led3.value = False
            