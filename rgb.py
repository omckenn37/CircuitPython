import simpleio
import pulseio
import board
import time

class RGB:
    kind="colors"
    def __init__(self, r, g, b):
        self.pwm_r = pulseio.PWMOut(r, frequency=1000, duty_cycle=0)
        self.pwm_g = pulseio.PWMOut(g, frequency=1000, duty_cycle=0)
        self.pwm_b = pulseio.PWMOut(b, frequency=1000, duty_cycle=0)


    def change_name(self, newName):
        self.name = newName

    def change_pins(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def red(self):
        self.pwm_r.duty_cycle = 0
        self.pwm_g.duty_cycle = 2**16-1
        self.pwm_b.duty_cycle = 2**16-1

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

    def rainbow(self, rate):

        for i in range(0,2**16,128):
            self.pwm_r.duty_cycle = 0 + i
            self.pwm_g.duty_cycle = 2**16-1-i
            self.pwm_b.duty_cycle = 2**16-1
            time.sleep(rate)
        for i in range(0,2**16,128):
            self.pwm_r.duty_cycle = 2**16-1
            self.pwm_g.duty_cycle = 0+i
            self.pwm_b.duty_cycle = 2**16-1-i
            time.sleep(rate)
        for i in range(0,2**16,128):
            self.pwm_r.duty_cycle = 2**16-1-i
            self.pwm_g.duty_cycle = 2**16-1
            self.pwm_b.duty_cycle = 0+i
            time.sleep(rate)