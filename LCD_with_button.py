# Owen McKenney
# LCD Screen
# This code displays the number of times you clicked a button on an LCD
# You can also toggle between counting up and down

import board
#import neopixel
import digitalio
import time
import adafruit_bus_device

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

inputPin = digitalio.DigitalInOut(board.D6)
inputPin.direction = digitalio.Direction.INPUT
inputPin.pull = digitalio.Pull.UP

button = digitalio.DigitalInOut(board.D8)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
#lcd.print("McDelivery")
counter = 0
oldSwitchState = 0
newSwitchState = 1
adder = 1

while True:
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Button pressed: ")

    lcd.set_cursor_pos(1,0)
    lcd.print(str(counter))

    if button.value:
        print("0")
        time.sleep(0.05)
        oldSwitchState = 0

    elif oldSwitchState == 0 and newSwitchState == 1:
        if inputPin.value:
            adder = 1
        else:
            adder = -1
        print("1")
        time.sleep(0.05)
        counter += adder
        oldSwitchState = 1