# Owen McKenney
# Circuitpython Servo Control
# This code allows you to turn a servo with two wires in each direction

import board
import neopixel
import digitalio
import analogio
import time
import simpleio
import pulseio
from adafruit_motor import servo
import touchio

pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
servo_angle = 0

while True:

    if touch_A1.value and servo_angle < 180:
        print("touched a1")
        servo_angle += 5
        my_servo.angle = servo_angle

    if touch_A2.value and servo_angle > 0:
        print("touched a2")
        servo_angle -= 5
        my_servo.angle = servo_angle

    time.sleep(0.01)