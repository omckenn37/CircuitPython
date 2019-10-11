# Owen McKenney
# RGB
# This code runs the RGB_main.py code

import simpleio
import pulseio
import board
import time

class RGB:
    kind="colors"
    def __init__(self, r, g, b): # This __init__ gets the pins to control the RGB LED
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)

    def change_pins(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def red(self): # Each of the next 6 functions gets a different color
        self.pwm_r.duty_cycle = 0 # 0 is on
        self.pwm_g.duty_cycle = 2**16-1 # While 2**16-1 is off
        self.pwm_b.duty_cycle = 2**16-1
        # Turing on different pins gets you different colors
    def blue(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0

    def green(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1

    def magenta(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 0

    def cyan(self):
        self.pwm_r.duty_cycle = 2**16-1
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 0

    def yellow(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 0
        self.pwm_b.duty_cycle = 2**16-1

    def rainbow(self, rate): # This function fades through the colors of the rainbow
        
        # Similar to going to one color, set each pin to on, off, or increasing, decreasing
        # 0 + i is increasing, so turning off
        # 0 in fully on
        # 2**16-1 is fully off
        # 2**16-i is decreasing, so turning on

        for i in range(0,2**16,128): # This for loop fades from red to green 
            self.pwm_r.duty_cycle = 0 + i 
            self.pwm_g.duty_cycle = 2**16-1-i
            self.pwm_b.duty_cycle = 2**16-1
            time.sleep(rate) # The rate can be changed in the main. It is how fast it fades
        for i in range(0,2**16,128): # This for loop fades from green to blue 
            self.pwm_r.duty_cycle = 2**16-1
            self.pwm_g.duty_cycle = 0+i
            self.pwm_b.duty_cycle = 2**16-1-i
            time.sleep(rate) 
        for i in range(0,2**16,128): # This for loop fades from blue back to red 
            self.pwm_r.duty_cycle = 2**16-1-i
            self.pwm_g.duty_cycle = 2**16-1
            self.pwm_b.duty_cycle = 0+i
            time.sleep(rate)