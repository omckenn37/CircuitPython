# Owen McKenney
# LCD Screen
#

import board
#import neopixel
import digitalio
import time
import adafruit_bus_device

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

button = digitalio.DigitalInOut(board.D8)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
#lcd.print("McDelivery")
press = 0

while True:
    lcd.set_cursor_pos(0,0)
    lcd.print(str(press))
    if button.value:
        print("0")
        time.sleep(.05)
    else:
        print("1")
        time.sleep(.05)
        press += 1


